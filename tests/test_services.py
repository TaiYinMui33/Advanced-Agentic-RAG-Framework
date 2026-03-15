import pytest
from services.rag_agent import AgenticRAGService

@pytest.mark.asyncio
async def test_agent_processing():
    service = AgenticRAGService()
    response, sources = await service.process_query("What is AI?", "session_123")
    assert isinstance(response, str)
    assert len(sources) > 0
