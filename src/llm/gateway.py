from abc import ABC, abstractmethod
from typing import Any, Dict, Optional


class LLMResponse:
    """
    Standard response returned by an LLM provider.
    """

    def __init__(
        self,
        content: str,
        model: str,
        metadata: Optional[Dict[str, Any]] = None,
    ):
        self.content = content
        self.model = model
        self.metadata = metadata or {}


class LLMGateway(ABC):
    """
    Provider-independent interface for LLM interaction.

    Agents depend on this abstraction rather than
    directly depending on a specific LLM provider.
    """

    @abstractmethod
    def generate(
        self,
        prompt: str,
        system_prompt: Optional[str] = None,
        context: Optional[Dict[str, Any]] = None,
    ) -> LLMResponse:
        """
        Generate a response from an LLM.
        """
        raise NotImplementedError
