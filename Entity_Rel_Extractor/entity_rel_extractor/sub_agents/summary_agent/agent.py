import os
from google.adk.agents import LlmAgent

from tools.ingest_tool import ingest_text_from_source

LLM_MODEL = os.environ['LLM_MODEL']

root_agent = LlmAgent(
    model=LLM_MODEL,
    name='summary_agent',
    description="Takes the cleaned text and summarises it neatly into full sentences",
    instruction=
    '''
    You are the summary agent. cleaned text is provided from the ingestion agent.

    This is your job:
    1. Retrieve the cleaned text using the key 'cleaned_text'
    2. Summarize it:
    - Into short, factual full sentences
    - Resolve pronouns and coreferences
    - Capture all main points
    - Maximum of 10 sentences.
    - REALLY FOCUS ON MAIN POINTS
    - Do not need to go into so many details
    - must be factual
    3. Return exactly one key
    -'summary_text': the summarised text as str
    ''',
    output_key='summary_text'
)


