from pathlib import Path
import json

class ProjectAnalyzer:

    def __init__(self, repo_path):
        self.repo_path = Path(repo_path)

    def analyze(self):

        package_json = self.repo_path / "package.json"

        if not package_json.exists():
            return None

        with open(package_json, "r", encoding="utf-8") as f:
            data = json.load(f)

        dependencies = data.get("dependencies", {})

        info = {
            "project_name": data.get("name"),
            "express": "express" in dependencies,
            "mongoose": "mongoose" in dependencies,
            "mongodb": "mongodb" in dependencies,
            "scripts": data.get("scripts", {})
        }

        return info