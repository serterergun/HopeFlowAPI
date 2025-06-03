import os
from openai import OpenAI, APIError

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ask_openai(messages: list[dict], model: str = "gpt-4") -> str:
    """
    Sends a list of messages to OpenAI ChatCompletion API and returns the response.
    """
    try:
        response = client.chat.completions.create(
            model=model,
            messages=messages
        )
        return response.choices[0].message.content
    except APIError as e:
        raise RuntimeError(f"OpenAI error: {str(e)}")