import pytest

from src.tools.github_tool import GitHubTool
from src.tools.tool_registry import ToolRegistry


def test_github_tool_creation():
    tool = GitHubTool()

    assert tool.name == "github"


def test_tool_registry_registers_tool():
    registry = ToolRegistry()
    tool = GitHubTool()

    registry.register(tool)

    assert "github" in registry.list_tools()


def test_github_tool_simulation():
    registry = ToolRegistry()
    registry.register(GitHubTool())

    result = registry.execute(
        name="github",
        parameters={
            "operation": "inspect_repository"
        },
    )

    assert result["tool"] == "github"
    assert result["status"] == "simulated"


def test_github_tool_rejects_invalid_operation():
    registry = ToolRegistry()
    registry.register(GitHubTool())

    with pytest.raises(ValueError):
        registry.execute(
            name="github",
            parameters={
                "operation": "delete_repository"
            },
        )
