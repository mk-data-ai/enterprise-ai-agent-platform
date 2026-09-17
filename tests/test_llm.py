from src.llm.gateway import LLMResponse
from src.llm.mock_llm import MockLLMGateway


def test_mock_llm_creation():
    llm = MockLLMGateway()

    assert llm.model == "mock-llm"


def test_mock_llm_generates_response():
    llm = MockLLMGateway()

    response = llm.generate(
        prompt="Explain agentic AI."
    )

    assert isinstance(response, LLMResponse)
    assert response.model == "mock-llm"
    assert "agentic AI" in response.content


def test_mock_llm_includes_context_metadata():
    llm = MockLLMGateway()

    response = llm.generate(
        prompt="Analyze this task.",
        context={
            "project": "enterprise-ai-agent-platform"
        },
    )

    assert response.metadata["provider"] == "mock"
    assert response.metadata["context_provided"] is True
