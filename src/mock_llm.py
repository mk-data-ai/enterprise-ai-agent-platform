from typing import Any, Dict, Optional

from .gateway import LLMGateway, LLMResponse


class MockLLMGateway(LLMGateway):
    """
    Mock LLM implementation used for development and testing.

    This implementation does not call an external LLM provider.
    """

    def __init__(self, model: str = "mock-llm"):
        self.model = model

    def generate(
        self,
        prompt: str,
        system_prompt: Optional[str] = None,
        context: Optional[Dict[str, Any]] = None,
    ) -> LLMResponse:
        """
        Generate a deterministic mock response.
        """

        response = (
            f"Mock LLM response for prompt: {prompt}"
        )

        return LLMResponse(
            content=response,
            model=self.model,
            metadata={
                "provider": "mock",
                "context_provided": context is not None,
            },
        )
