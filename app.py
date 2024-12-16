import nltk
import streamlit as st
import speech_recognition as sr
from nltk.chat.util import Chat, reflections

# Define chatbot logic
pairs = [
    (r"hi|hello", ["Hello! How can I assist you today?", "Hi there!"]),
    (r"what is your name?", ["I'm a speech-enabled chatbot!", "I am a virtual assistant."]),
    (r"how are you?", ["I'm just a program, but I'm doing great! How about you?"]),
    (r"quit", ["Bye! Take care."]),
    (r"(.*)", ["I'm not sure how to respond to that, but I'm learning every day!"])
]

# Initialize the Chat object
chatbot = Chat(pairs, reflections)

# Function to transcribe speech into text
def transcribe_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("Listening... Please speak into your microphone.")
        try:
            audio = recognizer.listen(source, timeout=5)
            text = recognizer.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            return "Sorry, I couldn't understand your speech."
        except sr.RequestError:
            return "There seems to be an issue with the speech recognition service."
        except Exception as e:
            return f"An error occurred: {e}"

# Streamlit app
def main():
    st.title("Speech-Enabled Chatbot")
    st.write("You can either type your input or use the microphone for speech input.")

    # Input mode selection
    input_mode = st.radio("Choose input method:", ["Text", "Speech"])
    
    if input_mode == "Text":
        user_input = st.text_input("Type your message here:")
        if user_input:
            response = chatbot.respond(user_input)
            st.write(f"Chatbot: {response}")
    
    elif input_mode == "Speech":
        if st.button("Start Listening"):
            user_input = transcribe_speech()
            st.write(f"You said: {user_input}")
            if user_input:
                response = chatbot.respond(user_input)
                st.write(f"Chatbot: {response}")

if __name__ == "__main__":
    main()
