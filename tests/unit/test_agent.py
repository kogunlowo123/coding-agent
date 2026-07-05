"""Coding Agent - Unit Tests."""

import pytest
from src.agent.tools import AgentTools


@pytest.mark.asyncio
async def test_generate_code():
    """Test Generate production code from a specification."""
    tools = AgentTools()
    result = await tools.generate_code(spec="test", language="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_explain_code():
    """Test Explain what a code block does in plain language."""
    tools = AgentTools()
    result = await tools.explain_code(code="test", language="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_complete_code():
    """Test Complete partial code with context-aware suggestions."""
    tools = AgentTools()
    result = await tools.complete_code(partial_code="test", cursor_position=1)
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_convert_code():
    """Test Convert code between languages or frameworks."""
    tools = AgentTools()
    result = await tools.convert_code(source_code="test", source_lang="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_agent_initialization():
    """Test that the agent initializes correctly."""
    from src.agent.coding_agent_agent import CodingAgentAgent
    agent = CodingAgentAgent()
    assert agent.agent_id is not None
    assert agent._system_prompt is not None
    assert len(agent._tool_dispatch) > 0
