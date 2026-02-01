from openai import OpenAI
import os

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise RuntimeError("OPENAI_API_KEY is not set in the environment.")

client = OpenAI()  # reads OPENAI_API_KEY from your environment

resp = client.responses.create(
    model="gpt-4o-mini",
    input="Hello World!"
)

print(resp.output_text)


