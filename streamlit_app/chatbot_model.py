import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

def train_and_save_model():
    X = [
        "I want SEO services",
        "Help with Instagram Ads",
        "Grow my website traffic",
        "How much do you charge?",
        "I need blog writers"
    ]
    y = ["SEO", "Social Media", "SEO", "Pricing", "Content Marketing"]

    vectorizer = TfidfVectorizer()
    X_vec = vectorizer.fit_transform(X)

    model = LogisticRegression()
    model.fit(X_vec, y)

    # Save model inside the deployed app folder
    with open("streamlit_app/intent_model.pkl", "wb") as f:
        pickle.dump(model, f)
    with open("streamlit_app/vectorizer.pkl", "wb") as f:
        pickle.dump(vectorizer, f)

# Only do this if model files don't already exist (avoid overwriting every time)
import os
if not os.path.exists("intent_model.pkl"):
    train_and_save_model()

# Now load it as usual
model = pickle.load(open("streamlit_app/intent_model.pkl", "rb"))
vectorizer = pickle.load(open("streamlit_app/vectorizer.pkl", "rb"))
