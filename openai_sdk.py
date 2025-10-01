from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama",
)

PROMPT = """You are a helpful assistant who writes emails using the following structure:
          * Situation
          * Task
          * Action
          * Result
          This helps customers stay informed."""


response = client.chat.completions.create(
    model="gpt-oss:20b",
    messages=[
        {"role": "system", "content": PROMPT},
        {"role": "user", "content": "Write an apology email for a late shipment of an AI chip."},
    ]
)

print(response.choices[0].message.content)
