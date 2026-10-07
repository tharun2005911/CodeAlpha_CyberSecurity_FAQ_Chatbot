import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

client = Groq(api_key=api_key)


def ask_groq(question):
    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a cybersecurity assistant for a cybersecurity FAQ chatbot. "
                    "You must answer ONLY questions related to cybersecurity, "
                    "information security, network security, privacy, data protection, "
                    "cryptography, malware, phishing, authentication, cloud security, "
                    "web security, incident response, vulnerabilities, and defensive security. "
                    "If the user's question is unrelated to cybersecurity, "
                    "do not answer it. Instead respond exactly with: "
                    "'Sorry, I can only answer cybersecurity-related questions.' "
                    "For cybersecurity questions, provide clear, concise, educational, "
                    "and defensive guidance. "
                    "Do not provide instructions for unauthorized attacks, "
                    "credential theft, malware deployment, or other illegal activity."
                )
            },
            {
                "role": "user",
                "content": question
            }
        ]
    )

    return response.choices[0].message.content