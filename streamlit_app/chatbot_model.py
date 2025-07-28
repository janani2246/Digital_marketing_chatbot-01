# streamlit_app/chatbot_model.py

import os
import pickle
import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Sample training data (customize if needed)
X_train = [
    "I want help with SEO",
    "Need social media marketing",
    "How much do you charge?",
    "I want to increase traffic",
    "Can you manage Instagram?",
    "Write blog posts for me",
    "Help with ad campaigns",
    "Tell me your pricing",
]
y_train = [
    "SEO",
    "Social Media",
    "Pricing",
    "SEO",
    "Social Media",
    "Content Marketing",
    "Advertising",
    "Pricing"
]

MODEL_PATH = "streamlit_app/intent_model.pkl"
VECTORIZER_PATH = "streamlit_app/vectorizer.pkl"

# Train and save model if not exists
def train_and_save():
    vectorizer = TfidfVectorizer()
    X_vectorized = vectorizer.fit_transform(X_train)

    model = LogisticRegression()
    model.fit(X_vectorized, y_train)

    with open(MODEL_PATH, "wb") as f:
        pickle.dump(model, f)
    with open(VECTORIZER_PATH, "wb") as f:
        pickle.dump(vectorizer, f)

# Train if model not found
if not os.path.exists(MODEL_PATH) or not os.path.exists(VECTORIZER_PATH):
    train_and_save()

# Load model
with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)
with open(VECTORIZER_PATH, "rb") as f:
    vectorizer = pickle.load(f)

# Streamlit UI
st.title("🧠 Digital Marketing Chatbot")

user_input = st.text_input("Ask me anything about our marketing services:")

if user_input:
    user_vec = vectorizer.transform([user_input])
    prediction = model.predict(user_vec)[0]

    responses = {
        "SEO": "We offer full SEO services to rank your site on Google.",
        "Social Media": "We can manage your Instagram, Facebook, and more.",
        "Pricing": "Our pricing depends on services. Contact us for a quote.",
        "Content Marketing": "We write blogs, articles, and email content.",
        "Advertising": "We run ads on Google, Facebook, Instagram, and more.",
    }

    st.write("🤖 Chatbot:")
    st.success(responses.get(prediction, "Sorry, I didn't understand. Please rephrase."))
