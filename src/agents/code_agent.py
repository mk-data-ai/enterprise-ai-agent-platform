from typing import Any, Dict, Optional

from .base_agent import BaseAgent
from src.llm.gateway import LLMGateway


class CodeAgent(BaseAgent):
    """
    Agent responsible for software engineering tasks.
    """

    def __init__(self, llm: Optional[LLMGateway] = None):
        super().__init__(
            name="code-agent",
            description=(
                "Handles code generation, analysis, debugging "
                "and refactoring tasks."
            ),
        )

        self.llm = llm

    def execute(
        self,
        task: str,
        context: Optional[Dict[str, Any]] = None,
    ) -> Any:
        """
        Execute a software engineering task.
        """

        if self.llm is None:
            return {
                "agent": self.name,
                "task": task,
                "status": "planned",
                "message": "Code task received for execution.",
            }

        response = self.llm.generate(
            prompt=task,
            system_prompt=(
                "You are a software engineering AI agent. "
                "Help analyze, generate, debug and refactor code."
            ),
            context=context,
        )

        return {
            "agent": self.name,
            "task": task,
            "status": "completed",
            "response": response.content,
            "model": response.model,
        }
