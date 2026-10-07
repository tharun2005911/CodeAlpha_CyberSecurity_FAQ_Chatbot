from faq_engine import answer_question

user_question = input(
    "Ask a cybersecurity question: "
)

score, source, answer = answer_question(
    user_question
)

print("Similarity score:", score)
print("Answer source:", source)
print("Answer:", answer)