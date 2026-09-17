from typing import Any, Dict, List

from .base_agent import BaseAgent


class AgentOrchestrator:
    """
    Coordinates execution across specialized AI agents.
    """

    def __init__(self, agents: List[BaseAgent]):
        self.agents = {
            agent.name: agent
            for agent in agents
        }

    def register_agent(self, agent: BaseAgent) -> None:
        """Register an agent with the orchestrator."""
        self.agents[agent.name] = agent

    def list_agents(self) -> List[str]:
        """Return the names of registered agents."""
        return list(self.agents.keys())

    def execute(
        self,
        agent_name: str,
        task: str,
        context: Dict[str, Any] | None = None,
    ) -> Any:
        """
        Route a task to the requested agent.
        """

        if agent_name not in self.agents:
            raise ValueError(
                f"Agent '{agent_name}' is not registered."
            )

        agent = self.agents[agent_name]

        return agent.execute(
            task=task,
            context=context,
        )
