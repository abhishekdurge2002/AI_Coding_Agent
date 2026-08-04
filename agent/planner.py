from agent.prompts import PLANNER_PROMPT
from agent.llm import LLMClient

class Planner:
    def __init__(self):
        self.llm = LLMClient()

    def create_plan(self, summary, user_request):
        prompt = PLANNER_PROMPT.format(
            summary=summary, 
            request=user_request
        )

        return self.llm.ask(prompt)