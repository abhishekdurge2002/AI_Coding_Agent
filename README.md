# 🤖 AI Coding Agent

An AI-powered coding agent built in **Python 3.11+** that can automatically analyze an existing codebase, understand a natural language product requirement, generate an implementation plan using an LLM, modify the relevant source files, and summarize the changes made.

This project was developed as part of an AI Coding Agent interview assignment.

---

# 🎯 Objective

The objective of this project is to build an autonomous AI coding agent capable of:

- Exploring an existing software repository.
- Understanding the project structure automatically.
- Generating an execution plan from a product requirement.
- Identifying the relevant files that require modification.
- Updating the codebase using an LLM.
- Preserving the existing functionality.
- Producing a summary of all modifications.

The target application for this assignment is the **node-easy-notes-app** repository.

---

# 🏗 Architecture

```
                User Request
                     │
                     ▼
           Repository Explorer
                     │
                     ▼
            Project Analyzer
                     │
                     ▼
               LLM Planner
                     │
                     ▼
              File Selector
                     │
                     ▼
             Code Modifier
             ↙            ↘
     Backup Files    Validate Output
             ↘            ↙
            Summary Generator
                     │
                     ▼
              Execution Report
```

---

# ⚙ Workflow

The agent performs the following workflow:

1. Receive the user requirement.
2. Explore the repository recursively.
3. Identify models, controllers, routes and configuration files.
4. Analyze the project structure and dependencies.
5. Generate an execution plan using Gemini.
6. Select only the files that require modification.
7. Create backups of the original files.
8. Modify the selected files.
9. Save the updated files.
10. Generate an execution summary.

---

# 💻 Technologies

- Python 3.11+
- Google Gemini API
- python-dotenv
- GitPython
- Rich
- Pathlib
- JSON
- Regular Expressions

---

# 📁 Folder Structure

```
AI-Coding-Agent/

│
├── agent/
│   ├── analyzer.py
│   ├── explorer.py
│   ├── llm.py
│   ├── modifier.py
│   ├── planner.py
│   ├── prompts.py
│   ├── selector.py
│   ├── summarizer.py
│   └── utils.py
│
├── target_repo/
│
├── execution_summary.txt
├── main.py
├── requirements.txt
├── README.md
└── .env
```

---

# 🔍 Repository Exploration

The Repository Explorer scans the target repository recursively while ignoring unnecessary directories such as:

- node_modules
- .git
- __pycache__
- dist
- build

The explorer automatically identifies:

- Models
- Controllers
- Routes
- Configuration files

This allows the agent to understand the overall project structure without manual intervention.

Example:

```
Models:
app/models/note.model.js

Controllers:
app/controllers/note.controller.js

Routes:
app/routes/note.routes.js
```

---

# 📝 Planning

The execution plan is generated using the Gemini Large Language Model.

Input:

```
Improve the application so users can better organise and search their notes.
```

Gemini analyzes:

- Repository summary
- Project structure
- User requirement

It then generates a step-by-step implementation plan such as:

- Add tags to the Note model.
- Update create and update APIs.
- Enhance search functionality.
- Preserve existing behaviour.

---

# 📂 File Selection

Instead of modifying every file in the repository, the File Selector determines which files are relevant based on the generated execution plan.

For this assignment, the selected files were:

- note.model.js
- note.controller.js
- note.routes.js

This minimizes unnecessary modifications and reduces LLM token usage.

---

# ✏ Code Modification

For every selected file, the agent performs the following steps:

1. Read the source file.
2. Create a backup (.bak).
3. Build a structured prompt.
4. Send the prompt to Gemini.
5. Receive updated code.
6. Remove markdown formatting if present.
7. Replace the original file.
8. Log the modification.

This approach ensures that only the intended file is modified while preserving unrelated code.

---

# ✅ Validation

To improve reliability, the agent includes several safety mechanisms:

- Original files are backed up before modification.
- LLM responses are cleaned before writing.
- Invalid or empty responses are rejected.
- Execution details are recorded in an execution summary.

These measures reduce the risk of corrupting the target repository.

---

# 🚀 How to Run

## Clone this repository

```bash
git clone <your-github-repository>
```

---

## Create a virtual environment

```bash
python -m venv venv
```

---

## Activate the environment

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

---

## Install dependencies

```bash
pip install -r requirements.txt
```

---

## Configure the Gemini API Key

Create a `.env` file.

```
GEMINI_API_KEY=YOUR_API_KEY
```

---

## Run the agent

```bash
python main.py
```

---

# 📊 Example Output

```
Repository Summary

Project:
node-easy-notes-app

Models:
note.model.js

Controllers:
note.controller.js

Routes:
note.routes.js

Execution Plan Generated

Files Selected

✓ note.model.js

✓ note.controller.js

✓ note.routes.js

Files Modified Successfully

Execution Summary Saved
```

---

# 📌 Assumptions

- The repository follows a conventional Node.js project structure.
- Models, controllers and routes follow common naming conventions.
- The provided repository is syntactically correct before modification.
- Gemini returns valid source code.
- The application can be modified file-by-file.

---

# ⚖ Trade-offs

Current implementation:

- File-level modifications instead of AST-based editing.
- Uses LLM-generated code directly.
- File selection is keyword-based.
- Validation is lightweight.

These trade-offs were chosen to keep the solution simple, readable and suitable for the assignment timeframe.

---

# 🔮 Future Improvements

Possible enhancements include:

- AST-based code modification instead of full-file replacement.
- Automatic syntax validation before saving.
- Git integration for automatic commits and rollback.
- Multi-LLM support (Gemini, OpenAI, Claude).
- Repository embeddings for semantic code search.
- Parallel file processing.
- Interactive CLI.
- Unit and integration test generation.
- Support for additional programming languages.

---

# 👨‍💻 Author

**Abhishek Durge**

AI Coding Agent Assignment

![alt text](<Screenshot 2026-08-03 183834.png>) ![alt text](<Screenshot 2026-08-03 183813.png>)