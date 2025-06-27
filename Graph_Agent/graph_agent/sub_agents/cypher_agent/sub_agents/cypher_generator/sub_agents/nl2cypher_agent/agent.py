import os
from google.adk.agents import LlmAgent
from google.adk.tools.agent_tool import AgentTool

LLM_MODEL = os.environ['LLM_MODEL']

root_agent = LlmAgent(
    model=LLM_MODEL,
    name='nl2cypher_agent',
    description='Generates a valid Cypher query from the natural language request stored in state["nlquery"].',
    instruction="""
You are a Cypher generation assistant.

This is the user's natural language request:
{nlquery}

Given a user's natural language request, output the correct Cypher query to accomplish the task.

Only output the Cypher query. Do not include any explanation, commentary, or markdown formatting.

Examples:
- If the user says "Show me all people who work at Neo4j", generate:
  MATCH (p:Person)-[:WORKS_AT]->(c:Company {name: "Neo4j"}) RETURN p;

- If the user says "Create a person named Alice", generate:
  CREATE (p:Person {name: "Alice"});

Use proper Cypher syntax. Ensure queries are valid and executable.
""",
    output_key="cypher_query",  # saves the generated Cypher into state["cypher_query"]
    tools=[]  # no tools needed here; it's a pure generation step
)
