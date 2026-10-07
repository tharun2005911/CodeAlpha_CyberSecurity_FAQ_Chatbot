# 🔐 Cybersecurity FAQ Chatbot

An NLP-based cybersecurity chatbot that combines a local FAQ knowledge base with an AI-powered fallback system.

The chatbot first searches a cybersecurity FAQ dataset using **NLTK preprocessing, TF-IDF vectorization, and cosine similarity**. If no relevant FAQ is found, the question is passed to the **Groq API** for an AI-generated cybersecurity response.

The AI fallback is restricted to cybersecurity-related topics.

---

## 🚀 Features

- 🔐 Cybersecurity-focused FAQ chatbot
- 📚 80 cybersecurity FAQs
- 📊 11 cybersecurity categories
- 🧠 NLP preprocessing using NLTK
- ✨ Stopword removal and lemmatization
- 🔎 TF-IDF vectorization
- 📐 Cosine similarity for FAQ matching
- 🎯 Similarity threshold for FAQ selection
- 🤖 Groq AI fallback for questions outside the FAQ dataset
- 🛡️ AI restricted to cybersecurity-related topics
- 💬 Single Question Mode
- 📋 Batch Mode for up to 5 questions
- 🗨️ Conversation history during the session
- 📊 FAQ statistics dashboard
- 🗑️ Clear Chat option
- 📄 CSV-based knowledge base

---

## 🧠 How It Works

The chatbot uses a hybrid approach combining traditional NLP with an AI fallback.

```text
                  User Question
                       ↓
                Text Preprocessing
                       ↓
                TF-IDF Vectorization
                       ↓
                Cosine Similarity
                       ↓
             Relevant FAQ Found?
                ↙            ↘
              YES             NO
               ↓               ↓
        FAQ Database        Groq AI
               ↓               ↓
          FAQ Answer     Cybersecurity
                          AI Answer