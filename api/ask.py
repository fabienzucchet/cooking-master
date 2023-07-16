import openai
import os

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY

# Send a prompt to the GPT-4 API and return the response
async def ask():
    messages = [
        {
            "role": "system",
            "content": "You are a helpful assistant."
        },
        {
            "role": "user",
            "content": "Hello!"
        }
    ]

    response = openai.ChatCompletion.create(
    model="gpt-4",
    max_tokens=100,
    temperature=1.2,
    messages = messages)

    print(response)

    return response
