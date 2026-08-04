from datetime import datetime


class Summarizer:

    def generate(self, plan, modified_files):

        summary = []

        summary.append("=" * 50)
        summary.append("AI Coding Agent Summary")
        summary.append("=" * 50)

        summary.append(f"Time : {datetime.now()}")

        summary.append("\nExecution Plan:")
        summary.append(plan)

        summary.append("\nModified Files:")

        for file in modified_files:
            summary.append(f"✓ {file}")

        summary.append("\nStatus: SUCCESS")

        return "\n".join(summary)