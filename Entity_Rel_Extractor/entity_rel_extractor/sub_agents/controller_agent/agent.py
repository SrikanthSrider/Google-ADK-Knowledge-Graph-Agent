# agents/controller_agent/agent.py

import os
from datetime import date
from google.adk.agents import SequentialAgent
from threat_detector.sub_agents.ingestion_agent.agent import root_agent as ingestion_agent
from threat_detector.sub_agents.summary_agent.agent import root_agent as summary_agent
from threat_detector.sub_agents.extraction_agent.agent import root_agent as extraction_agent
#from graph_agent.agent import root_agent as graph_agent
from google.adk.tools.agent_tool import AgentTool

today = date.today()

root_agent = SequentialAgent(
    name="controller_agent",
    description=(
        f"Executes full threat intelligence pipeline on {today}. "
        "Steps: ingest → extract → graph push. "
        "Returns cleaned text, summaries, entities, relationships, and graph status."
    ),
    sub_agents=[
        ingestion_agent,
        summary_agent,
        extraction_agent
    ]
)
