import os
from google.adk.agents import LlmAgent
from google.adk.tools.agent_tool import AgentTool

LLM_MODEL = os.environ['LLM_MODEL']

root_agent = LlmAgent(
    model = LLM_MODEL,
    name = 'cypher_executor',
    description='Executor Agent for the cypher generated by the cypher_agent',
    instruction=
    '''
    ''',
    tools=[]
)