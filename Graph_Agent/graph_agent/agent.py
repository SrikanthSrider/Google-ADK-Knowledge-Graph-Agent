import os
from google.adk.agents import LlmAgent
from google.adk.tools.agent_tool import AgentTool
from graph_agent.sub_agents.cypher_agent.agent import root_agent as cypher_agent
from graph_agent.sub_agents.explainer_agent.agent import root_agent as explainer_agent

LLM_MODEL = os.environ['LLM_MODEL']

root_agent = LlmAgent(
    name="graph_agent",
    model=LLM_MODEL,
    description=(
        '''
        An agent that will manage all the interactions involving the neo4j graph database
        '''
    ),
    instruction=
    '''
    ''',
    tools=[AgentTool(agent=cypher_agent), AgentTool(agent=explainer_agent)]
)