from src.agents.code_agent import CodeAgent
from src.agents.orchestrator import AgentOrchestrator


def test_code_agent_creation():
    agent = CodeAgent()

    assert agent.name == "code-agent"
    assert "code generation" in agent.description.lower()


def test_orchestrator_registers_agent():
    agent = CodeAgent()
    orchestrator = AgentOrchestrator([agent])

    assert "code-agent" in orchestrator.list_agents()


def test_orchestrator_executes_agent():
    agent = CodeAgent()
    orchestrator = AgentOrchestrator([agent])

    result = orchestrator.execute(
        agent_name="code-agent",
        task="Analyze repository structure.",
    )

    assert result["agent"] == "code-agent"
    assert result["status"] == "planned"
