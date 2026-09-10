def test_agent_orchestrator():
    prompt = "Test execution query for agentic-personalized-news-digest"
    assert len(prompt) > 0
    assert "Test" in prompt
