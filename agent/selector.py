import re


class FileSelector:

    def select_files(self, project_info, plan):

        selected = []

        plan = plan.lower()

        mapping = {
            "model": project_info["models"],
            "controller": project_info["controllers"],
            "route": project_info["routes"],
            "config": project_info["configs"],
        }

        for keyword, files in mapping.items():
            if re.search(keyword, plan):
                selected.extend(files)

        return list(set(selected))