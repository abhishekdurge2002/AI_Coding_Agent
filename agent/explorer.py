from pathlib import Path

IGNORE_DIRS = {
    "node_modules",
    ".git",
    "__pycache__",
    ".idea",
    ".vscode",
    "dist",
    "build"
}

class RepositoryExplorer:

    def __init__(self, repo_path):
        self.repo_path = Path(repo_path)

    def explore(self):
        project_info = {
            "models": [],
            "controllers": [],
            "routes": [],
            "configs": [],
            "others": []
        }

        for file in self.repo_path.rglob("*"):

            if file.is_dir():
                continue

            if any(part in IGNORE_DIRS for part in file.parts):
                continue

            filename = file.name.lower()

            if file.suffix == ".bak":
                continue

            if "model" in filename:
                project_info["models"].append(str(file))

            elif "controller" in filename:
                project_info["controllers"].append(str(file))

            elif "route" in filename:
                project_info["routes"].append(str(file))

            elif "config" in filename:
                project_info["configs"].append(str(file))

            else:
                project_info["others"].append(str(file))

        return project_info