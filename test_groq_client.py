from groq_client import ask_groq

question = input("Ask an advanced cybersecurity question: ")

answer = ask_groq(question)

print("\nAI Answer:\n")
print(answer)