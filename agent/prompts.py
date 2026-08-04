PLANNER_PROMPT = """
You are an experienced software architect.

Repository Summary

{summary}

User Request

{request}

Your task:

1. Understand the project.

2. Decide what feature should be implemented.

3. Preserve existing functionality.

4. Produce a numbered execution plan.

Return ONLY the plan.
"""


MODIFIER_PROMPT = """
You are an expert Node.js backend developer.

Your task is to modify ONLY the given file.

Repository Summary:
{summary}

Execution Plan:
{plan}

Current File:
{filename}

Current Code:
```javascript
{code} ```
"""