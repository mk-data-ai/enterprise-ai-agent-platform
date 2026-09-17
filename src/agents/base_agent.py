from abc import ABC, abstractmethod
from typing import Any, Dict


class BaseAgent(ABC):
    """
    Base abstraction for all AI agents in the platform.
    """

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    @abstractmethod
    def execute(self, task: str, context: Dict[str, Any] | None = None) -> Any:
        """
        Execute an agent task.

        Args:
            task: Task description.
            context: Optional execution context.

        Returns:
            Agent execution result.
        """
        raise NotImplementedError
