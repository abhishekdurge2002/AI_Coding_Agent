from openai import files

from agent.explorer import RepositoryExplorer
from agent.analyzer import ProjectAnalyzer
from agent.planner import Planner
from agent.utils import build_summary
from agent.modifier import Modifier
from agent.selector import FileSelector
from agent.summarizer import Summarizer
from rich.console import Console

console = Console()

REQUEST = "Improve the application so users can organise and search their notes."

def main():
    explorer = RepositoryExplorer("target_repo")
    project = explorer.explore()

    analyzer = ProjectAnalyzer("target_repo")
    analysis = analyzer.analyze()

    summary = build_summary(project, analysis)
    console.print("\nRepository Summary:\n")
    console.print(summary)

    planner = Planner()
    console.print("[cyan]🤖 Generating Execution Plan...[/cyan]")
    plan = planner.create_plan(summary, REQUEST)
    console.print("\nExecute Plan:\n")
    console.print(plan)

    selector = FileSelector()
    files = selector.select_files(project, plan)
    console.print("\nFiles Selected:")
    for file in files:
        console.print(file)

    console.print("\n[yellow]🚀 Starting Code Modification...[/yellow]")
    modifier = Modifier()
    for file in files:
        modifier.modify_file(
            file,
            summary,
            plan
        )

    summarizer = Summarizer()
    summary_text = summarizer.generate(plan, files)
    with open("execution_summary.txt", "w", encoding="utf-8") as f:
        f.write(summary_text)
    
    console.print("\nSummary written to execution_summary.txt")
    console.print("\n[bold green]🎉 AI Coding Agent Completed Successfully![/bold green]")


if __name__ == "__main__":
    main()