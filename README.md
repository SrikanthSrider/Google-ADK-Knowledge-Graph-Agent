# Google-ADK-Knowledge-Graph-Agent
A knowledge Graph Agent capable of extracting entities and relationships and commiting them to neo4j

## Components of Agent
- The agent has so far 2 components: 
    - an agent for entity and relationhip extraction
    - a graph agent for writing, executing cypher queries and explaining the results

## The folders
- Entity_Extraction_POC:
    - In here there is a simple proof of concept/testing for extracting entities and relationships and then making a gpickle ggraph out of them
    - No LLM agents involved
- Entity_Rel_Extractor:
    - This is the entity and relationship extraction agent
    - Progress:
        - Able to extract entities and relationships and present them back to the author
        - Flow:
            - Extract text using langchain tools
            - summarise and do co-reference resolution
            - Extract 
            - present them back
- Graph_Agent:
    - This is the graph database agent.
    - Progress:
        - nl2_cypher_agent works, able to generate cypher queries
        - Flow:
            - get user request
            - generate query accordingly
            - approve query
            - execute query
            - explain results

## Next Steps:
- Entity_Rel_Extractor:
    - Feed in the standardised schema and to help stnadardise the extractions
- Graph_Agent:
    - cypher_execution agent needs to be set up
    - explainer agent needs to be set up
    - Might rethink flow
- Overall:
    - stitch everything together :)



