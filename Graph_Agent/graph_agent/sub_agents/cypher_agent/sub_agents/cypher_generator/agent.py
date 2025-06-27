import os
from google.adk.agents import LoopAgent
from cypher_generator.sub_agents.approval_agent.agent import root_agent as approval_agent
from cypher_generator.sub_agents.nl2cypher_agent.agent import root_agent as nl2cypher_agent

root_agent = LoopAgent(
    name="cypher_generator",
    description="Generates the Cypher query for the user and seek his approval of the query",
    sub_agents=[nl2cypher_agent, approval_agent]
)