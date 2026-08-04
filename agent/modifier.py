from pathlib import Path
import shutil
import subprocess
import json
import re
from datetime import datetime

from agent.prompts import MODIFIER_PROMPT
from agent.llm import LLMClient
from rich.console import Console

console = Console()

class Modifier:

    def __init__(self):
        self.llm = LLMClient()

    def validate_js(self, file_path):
        """
        Validate JavaScript syntax using Node.js
        """
        try:
            result = subprocess.run(
                ["node", "--check", str(file_path)],
                capture_output=True,
                text=True
            )

            if result.returncode == 0:
                return True, ""

            return False, result.stderr

        except Exception as e:
            return False, str(e)

    def log_modification(self, filepath, backup, status, validation, error=""):

        log_file = Path("logs/modification_log.json")

        log_file.parent.mkdir(exist_ok=True)

        log_entry = {
            "file": str(filepath),
            "backup": str(backup),
            "status": status,
            "validation": validation,
            "error": error,
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        logs = []

        # Read existing log if present
        if log_file.exists():

            try:
                with open(log_file, "r", encoding="utf-8") as f:

                    content = f.read().strip()

                    if content:
                        logs = json.loads(content)

            except json.JSONDecodeError:
                logs = []

        logs.append(log_entry)

        with open(log_file, "w", encoding="utf-8") as f:
            json.dump(logs, f, indent=4)

    def modify_file(self, filepath, summary, plan):

        filepath = Path(filepath)

        console.print(
            f"\n[yellow]🔧 Modifying[/yellow] [bold]{filepath.name}[/bold]"
        )

        # Read original file
        code = filepath.read_text(encoding="utf-8")

        # Create backup
        backup = filepath.with_suffix(filepath.suffix + ".bak")
        shutil.copy(filepath, backup)

        prompt = MODIFIER_PROMPT.format(
            summary=summary,
            plan=plan,
            filename=filepath.name,
            code=code
        )

        updated_code = self.llm.ask(prompt)

        # Remove markdown if Gemini returns it
        updated_code = re.sub(
            r"```(?:javascript|js)?",
            "",
            updated_code,
            flags=re.IGNORECASE
        )

        updated_code = updated_code.replace("```", "").strip()

        if len(updated_code) < 100:
            print("❌ Gemini returned an invalid response.")

            shutil.copy(backup, filepath)

            self.log_modification(
                filepath,
                backup,
                "FAILED",
                False,
                "LLM returned too little code."
            )

            return

        # Save modified file
        filepath.write_text(updated_code, encoding="utf-8")

        # Validate JS
        valid, error = self.validate_js(filepath)

        if valid:

            console.print("[bold green]✓ File Updated Successfully[/bold green]")
            console.print("[bold green]✓ Validation Passed[/bold green]")

            self.log_modification(
                filepath,
                backup,
                "SUCCESS",
                True
            )

        else:

            console.print("[bold red]✗ Validation Failed[/bold red]")
            console.print(error)

            shutil.copy(backup, filepath)

            self.log_modification(
                filepath,
                backup,
                "FAILED",
                False,
                error
            )

            console.print("✓ Original restored")