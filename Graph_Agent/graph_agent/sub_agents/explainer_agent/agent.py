import os
from google.adk.agents import LlmAgent
from google.adk.tools.agent_tool import AgentTool

LLM_MODEL = os.environ['LLM_MODEL']

root_agent = LlmAgent(
    model = LLM_MODEL,
    name = 'explainer_agent',
    description='Explainer of the cypher result returned by the cypher_executor',
    instruction=
    '''
    ''',
    tools=[]
)