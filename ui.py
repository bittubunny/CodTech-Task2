import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle
import random

# Load the saved tokenizer
with open('tokenizer.pkl', 'rb') as f:
    tokenizer = pickle.load(f)

# Load the saved model
model = load_model('sentiment_model.keras')

# Recompile the model (if needed)
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Set up Streamlit app
st.set_page_config(page_title="🎬 Sentiment Analyzer", page_icon="🌟", layout="wide")

# Add background color
st.markdown(
    """
    <style>
    body {
        background-color: #f5f5f5;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Add title and subtitle
st.title("🎥 Movie Review Sentiment Analyzer")
st.subheader("📝 Enter your review below and find out its sentiment!")

# Add a fun banner
st.markdown(
    """
    <div style="background-color: #4CAF50; padding: 10px; border-radius: 10px;">
        <h2 style="color: white; text-align: center;">Is your review 🎉 Positive or 😞 Negative?</h2>
    </div>
    """,
    unsafe_allow_html=True,
)

# Input field for user review
user_review = st.text_area("💬 Enter your review here:", placeholder="Type something like 'The movie was fantastic!'")

# Button to predict sentiment
if st.button("🔮 Predict Sentiment"):
    if user_review.strip():
        # Preprocess the input
        max_length = 500  # Should match the max_length used during training
        input_seq = tokenizer.texts_to_sequences([user_review])
        input_padded = pad_sequences(input_seq, maxlen=max_length)

        # Predict sentiment
        prediction = model.predict(input_padded)
        sentiment = 'Positive' if prediction[0][0] >= 0.5 else 'Negative'
        confidence = prediction[0][0] if sentiment == 'Positive' else 1 - prediction[0][0]

        # Display sentiment with emojis
        sentiment_emoji = "🎉" if sentiment == "Positive" else "😞"
        st.write(f"**Predicted Sentiment:** {sentiment} {sentiment_emoji}")
        st.write(f"**Confidence:** {confidence*100:.4f}")

        # Random motivational message
        messages = {
            "Positive": [
                "Great to see a positive vibe! 🌟",
                "Spread the positivity! 💖",
                "This one's a hit! 🎬",
            ],
            "Negative": [
                "Oh no, looks like a miss. 😢",
                "Better luck next time! 🍀",
                "Maybe a different genre would help? 🤔",
            ],
        }
        st.write(random.choice(messages[sentiment]))

        # Feedback section
        st.markdown("---")
        st.subheader("📢 Share Your Feedback!")
        feedback = st.text_area("What do you think about the app?", placeholder="Your feedback is valuable!")
        if st.button("Submit Feedback"):
            if feedback.strip():
                st.success("Thank you for your feedback! 😊")
            else:
                st.warning("Please write something before submitting.")
    else:
        st.warning("Please enter a valid review.")

# Footer with contact info
st.markdown("---")
st.write("Made with ❤️ by Bharath Chelimalla")
st.write("Connect with me on [LinkedIn](https://www.linkedin.com) or check out my [GitHub](https://github.com).")
