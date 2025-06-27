import os
from google.adk.agents import LlmAgent

from tools.ingest_tool import ingest_text_from_source

LLM_MODEL = os.environ['LLM_MODEL']

root_agent = LlmAgent(
    model=LLM_MODEL,
    name='ingestion_agent',
    description="Loads the document and gets the cleaned using the ingest_text_from_source tool",
    instruction=
    '''
    You are the ingestion agent. Users will supply a document 'source', which could be:
    - a public HTTP/HTTPS URL (web page or PDF link), OR
    - a file path to a local PDF on disk.

    Your job:
    1. Call the function ingest_text_from_source with the provided source.
    2. Retrieve the cleaned text.
    4. Return exactly one key:
    - 'cleaned_text': the full cleaned string
    ''',
    tools=[ingest_text_from_source],
    output_key='cleaned_text'
)

