import os
from google.adk.agents import SequentialAgent
from google.adk.tools.agent_tool import AgentTool
from cypher_agent.sub_agents.cypher_generator.agent import root_agent as cypher_generator
from cypher_agent.sub_agents.cypher_executor.agent import root_agent as cypher_executor

LLM_MODEL = os.environ['LLM_MODEL']

root_agent = SequentialAgent(
    name="cypher_agent",
    model=LLM_MODEL,
    description=
        '''
        A pipeline that consists of 2 components: 
            1. cypher_generator_agent, for cypher generation
            2. cypher_executor_agent, for cypher execution
        ''',
    sub_agents=[cypher_generator, cypher_executor]
)