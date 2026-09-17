from src.agents.code_agent import CodeAgent
from src.agents.orchestrator import AgentOrchestrator
from src.tools.github_tool import GitHubTool
from src.tools.tool_registry import ToolRegistry


def main():
    # Create the agent
    code_agent = CodeAgent()

    # Create the orchestrator
    orchestrator = AgentOrchestrator(
        agents=[code_agent]
    )

    # Create and register tools
    tool_registry = ToolRegistry()
    github_tool = GitHubTool()

    tool_registry.register(github_tool)

    print("Registered agents:")
    print(orchestrator.list_agents())

    print("\nRegistered tools:")
    print(tool_registry.list_tools())

    # Execute an agent task
    result = orchestrator.execute(
        agent_name="code-agent",
        task="Analyze the repository structure.",
    )

    print("\nAgent result:")
    print(result)

    # Execute a tool operation
    tool_result = tool_registry.execute(
        name="github",
        parameters={
            "operation": "inspect_repository"
        },
    )

    print("\nTool result:")
    print(tool_result)


if __name__ == "__main__":
    main()
