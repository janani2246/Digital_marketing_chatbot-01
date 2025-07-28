import pickle

# Load
model = pickle.load(open("streamlit_app/intent_model.pkl", "rb"))
vectorizer = pickle.load(open("streamlit_app/vectorizer.pkl", "rb"))

# Responses
intent_to_response = {
    "SEO": "We provide SEO services to improve your Google rankings.",
    "Social Media": "We can help you grow on Instagram, Facebook, and more.",
    "Pricing": "Our plans start at ₹10,000/month. Want a custom quote?",
    "Content Marketing": "We offer blog writing, newsletters, and more!"
}

def get_bot_response(user_input):
    vec = vectorizer.transform([user_input])
    intent = model.predict(vec)[0]
    return intent_to_response.get(intent, "Sorry, I didn't understand. Can you try again?")

