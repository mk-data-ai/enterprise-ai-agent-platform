from abc import ABC, abstractmethod
from typing import Any, Dict


class BaseTool(ABC):
    """
    Base abstraction for tools that can be invoked by AI agents.
    """

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    @abstractmethod
    def execute(
        self,
        parameters: Dict[str, Any],
    ) -> Any:
        """
        Execute the tool with the supplied parameters.
        """
        raise NotImplementedError
