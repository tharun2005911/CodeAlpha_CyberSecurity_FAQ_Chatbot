import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    print("GROQ_API_KEY was not found.")
    exit()

client = Groq(api_key=api_key)

response = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {
            "role": "system",
            "content": "You are a helpful cybersecurity assistant."
        },
        {
            "role": "user",
            "content": "What is phishing?"
        }
    ]
)

print("\nGroq API Response:\n")
print(response.choices[0].message.content)