import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("GROQ_API_KEY environment variable is not set.")

client = Groq(api_key=my_api_key)

model = "openai/gpt-oss-120b"
role = "user"
prompt = "Write a poem about the beauty of love."
#System
message_system = {"role": "system", "content": "You are a creative writer"}
message = {"role": role, "content": prompt}
messages = [message_system, message]

response = client.chat.completions.create(model=model, messages=messages, temperature=2)
print(response.choices[0].message.content)