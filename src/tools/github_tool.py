from typing import Any, Dict

from .base_tool import BaseTool


class GitHubTool(BaseTool):
    """
    Safe GitHub tool abstraction for AI agents.

    This initial implementation operates in simulation mode.
    No GitHub credentials or repository modifications are performed.
    """

    def __init__(self):
        super().__init__(
            name="github",
            description=(
                "Performs GitHub-related operations such as "
                "repository inspection, branch creation and "
                "pull request preparation."
            ),
        )

    def execute(
        self,
        parameters: Dict[str, Any],
    ) -> Dict[str, Any]:
        """
        Execute a GitHub operation in simulation mode.
        """

        operation = parameters.get("operation")

        if not operation:
            raise ValueError(
                "GitHub operation must be specified."
            )

        supported_operations = {
            "inspect_repository",
            "create_branch",
            "prepare_pull_request",
        }

        if operation not in supported_operations:
            raise ValueError(
                f"Unsupported GitHub operation: {operation}"
            )

        return {
            "tool": self.name,
            "operation": operation,
            "status": "simulated",
            "message": (
                f"GitHub operation '{operation}' "
                "was simulated successfully."
            ),
        }
