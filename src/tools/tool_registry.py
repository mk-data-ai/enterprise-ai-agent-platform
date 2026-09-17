from typing import Any, Dict, List

from .base_tool import BaseTool


class ToolRegistry:
    """
    Central registry for tools available to AI agents.
    """

    def __init__(self):
        self._tools: Dict[str, BaseTool] = {}

    def register(self, tool: BaseTool) -> None:
        """
        Register a tool.
        """
        self._tools[tool.name] = tool

    def get(self, name: str) -> BaseTool:
        """
        Retrieve a registered tool by name.
        """
        if name not in self._tools:
            raise ValueError(
                f"Tool '{name}' is not registered."
            )

        return self._tools[name]

    def list_tools(self) -> List[str]:
        """
        Return names of all registered tools.
        """
        return list(self._tools.keys())

    def execute(
        self,
        name: str,
        parameters: Dict[str, Any],
    ) -> Any:
        """
        Execute a registered tool.
        """
        tool = self.get(name)

        return tool.execute(parameters)
