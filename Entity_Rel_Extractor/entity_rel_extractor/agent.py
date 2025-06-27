import os
from google.adk.agents import LlmAgent
from google.adk.tools.agent_tool import AgentTool
from .prompts import return_instructions_root
from threat_detector.sub_agents.controller_agent.agent import root_agent as controller_agent

LLM_MODEL = os.environ['LLM_MODEL']

root_agent = LlmAgent(
    name="threat_detector",
    model=LLM_MODEL,
    description=(
        "LLM-facing assistant that interprets user requests "
        "and invokes the threat pipeline as needed."
    ),
    instruction=return_instructions_root(),
    tools=[AgentTool(agent= controller_agent) ],
    output_key='source',
)

