import streamlit as st
from faq_engine import answer_question
import pandas as pd

df = pd.read_csv("data/faqs.csv")

# -----------------------------
# Page setup
# -----------------------------

st.set_page_config(
    page_title="Cybersecurity FAQ Chatbot",
    page_icon="🔐",
    layout="wide"
)

st.title("🔐 Cybersecurity FAQ Chatbot")
st.write("Ask cybersecurity questions and get answers from the FAQ database.")


# -----------------------------
# Sidebar
# -----------------------------

st.sidebar.header("⚙️ Options")
st.sidebar.subheader("📊 FAQ Statistics")

st.sidebar.write(f"Total FAQs: {len(df)}")
st.sidebar.write(f"Categories: {df['category'].nunique()}")

category_counts = df["category"].value_counts()

with st.sidebar.expander("View Categories"):
    for category, count in category_counts.items():
        st.write(f"**{category}:** {count}")

mode = st.sidebar.radio(
    "Choose mode:",
    ["Single Question", "Batch Mode"]
)

if st.sidebar.button("🗑️ Clear Chat"):
    st.session_state.messages = []
    st.rerun()


# -----------------------------
# Session history
# -----------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []


# -----------------------------
# Single Question Mode
# -----------------------------

if mode == "Single Question":

    st.subheader("💬 Ask a Question")

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    user_question = st.chat_input(
        "Ask a cybersecurity question..."
    )

    if user_question:

        score, source, answer = answer_question(user_question)

        st.session_state.messages.append({
            "role": "user",
            "content": user_question
        })

        if source == "faq":

            bot_response = f"**Answer:** {answer}"

        else:

            bot_response = f"**Answer:** {answer}"
        st.session_state.messages.append({
            "role": "assistant",
            "content": bot_response
        })

        st.rerun()


# -----------------------------
# Batch Mode
# -----------------------------

else:

    st.subheader("📋 Batch Questions")

    st.write(
        "Enter up to 5 cybersecurity questions and "
        "get all answers together."
    )

    questions = []

    for i in range(5):

        question = st.text_input(
            f"Question {i + 1}",
            key=f"batch_question_{i}"
        )

        questions.append(question)


    if st.button("🚀 Get Answers"):

        valid_questions = [
            question for question in questions
            if question.strip()
        ]

        if not valid_questions:

            st.warning("Please enter at least one question.")

        else:

            st.subheader("📚 Results")

            for i, question in enumerate(valid_questions, start=1):

                score, source, answer = answer_question(question)

                st.markdown(f"### Question {i}")

                st.write(question)

                if source == "faq":

                    st.success(answer)

                else:

                    st.info(answer)


                st.divider()