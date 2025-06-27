# agents/extraction_agent/agent.py

from google.adk.agents import LlmAgent
import os

LLM_MODEL = os.environ['LLM_MODEL']

root_agent = LlmAgent(
    name="extraction_agent",
    model=LLM_MODEL,
    description=(
        "Extraction Agent that will extract entities and relationships from clean text"
    ),
    instruction='''
    You are an extraction agent. This is your job and follow these instructions carefully and strictly.
    1. use the key 'summary_text' to get the summary_text
    2. extract the named entities and relationships
    3. The output should be a dictionary containing the 'entities' and 'relationships'
    4. Return the dictionary under exactly one key: "E_and_R"
    ''',
    tools=[],
    output_key="E_and_R",
)