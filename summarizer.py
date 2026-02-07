from dotenv import load_dotenv
import os
from openai import OpenAI
import json

# Load environment variables from .env file
load_dotenv()

# Initialize OpenAI client with API key from environment
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_summary(transcript):
    prompt = f"""
You are an AI assistant. Read this meeting transcript and return JSON:
- summary
- key_points
- action_items

Transcript:
{transcript}

Output only JSON with keys:
summary, key_points, action_items
"""

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=500
    )

    # Parse JSON from response
    try:
        return json.loads(response.choices[0].message.content)
    except json.JSONDecodeError:
        # Fallback if JSON parsing fails
        return {"summary": response.choices[0].message.content, "key_points": [], "action_items": []}