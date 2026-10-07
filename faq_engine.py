import pandas as pd
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from groq_client import ask_groq


# NLP tools
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words("english"))


# Text preprocessing
def preprocess_text(text):
    words = text.lower().split()

    filtered_words = [
        word for word in words
        if word not in stop_words
    ]

    lemmatized_words = [
        lemmatizer.lemmatize(word)
        for word in filtered_words
    ]

    return " ".join(lemmatized_words)


# Load FAQ dataset
df = pd.read_csv("data/faqs.csv")

questions = df["question"]
answers = df["answer"]


# Create TF-IDF model
vectorizer = TfidfVectorizer(
    ngram_range=(1, 2)
)

processed_questions = questions.apply(preprocess_text)

question_vectors = vectorizer.fit_transform(
    processed_questions
)


# Match user question with FAQ
def answer_question(user_question):
    processed_user_question = preprocess_text(user_question)

    user_vector = vectorizer.transform(
        [processed_user_question]
    )

    similarities = cosine_similarity(
        user_vector,
        question_vectors
    )

    best_match_index = similarities.argmax()
    best_score = similarities[0, best_match_index]

    threshold = 0.2

    if best_score >= threshold:
        matched_question = questions.iloc[best_match_index]
        answer = answers.iloc[best_match_index]

        return best_score, "faq", answer

    # No relevant FAQ found → use Groq
    ai_answer = ask_groq(user_question)

    return best_score, "ai", ai_answer