import vertexai
from vertexai.generative_models import GenerativeModel
vertexai.init(project="ethereal-cache-463417-g3", location="us-central1")
import re

def extract_entities(text: str) -> dict:
    prompt = f"""
You are a security-focused AI. Extract the following from the given article:

- People
- Organizations
- Locations
- Crimes

Return the result as a Python dictionary with keys: people, orgs, locations, crimes.

ARTICLE:
{text[:3000]}
    """

    model = GenerativeModel("gemini-2.0-flash-001")
    chat = model.start_chat()
    response = chat.send_message(prompt)

    raw = response.text.strip()

    # remove surrounding code block if present (e.g., ```python ... ```)
    if raw.startswith("```"):
        raw = re.sub(r"^```(?:\w+)?", "", raw)  # remove opening ``` or ```python
        raw = re.sub(r"```$", "", raw)          # remove closing ```

    try:
        return eval(raw.strip())
    except Exception as e:
        print("⚠️ Could not parse response:", raw)
        return {}