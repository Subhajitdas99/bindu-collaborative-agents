import os
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.duckduckgo import DuckDuckGoTools

# Configure OpenRouter
model = OpenAIChat(
    id="openai/gpt-4o-mini",   # OpenRouter model
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)

research_agent = Agent(
    instructions="""
You are a research agent specialized in the Bindu AI Framework.

If the user asks about Bindu, assume they mean the Bindu AI framework
used for building interoperable AI agents.

Search and explain concepts like:
- Internet of Agents
- Bindu Framework
- Agent-to-Agent communication
- Bindu architecture
""",
    model=model,
    tools=[DuckDuckGoTools()]
)

def research(query):
    result = research_agent.run(input=query)
    return result.content