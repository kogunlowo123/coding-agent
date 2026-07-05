"""Test configuration for Coding Agent."""

import pytest


@pytest.fixture
def agent_config():
    return {"name": "coding-agent", "category": "Software Engineering"}
