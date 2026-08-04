import os
import re
import time
from dotenv import load_dotenv
from google import genai
from google.genai.errors import ClientError
from rich.console import Console

load_dotenv()
console = Console()

class LLMClient:
    def __init__(self):
        self.client = genai.Client(
            api_key=os.getenv("GEMINI_API_KEY")
        )

    def clean_response(self, text):
            """
            Extract code from Gemini response.
            """
    
            match = re.search(r"```(?:javascript|js)?\n(.*?)```", text, re.DOTALL)
    
            if match:
                return match.group(1).strip()
    
            return text.strip()

    def ask(self, prompt):

        retries = 3

        for attempt in range(retries):

            try:

                response = self.client.models.generate_content(
                    model="gemini-3.5-flash",
                    contents=prompt
                )

                return self.clean_response(response.text)

            except Exception as e:

                console.print(f"[bold red]Gemini Error: {e}[/bold red]")

                if attempt < retries - 1:
                    console.print("Retrying...")
                    time.sleep(5)
                else:
                    raise


    