import speech_recognition as sr
import time
import os
from gtts import gTTS
import pygame
import google.generativeai as genai
from dotenv import load_dotenv

# Load API Key
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Configure Gemini
genai.configure(api_key=api_key)

# Initialize pygame for audio playback
pygame.mixer.init()

def listen_for_speech(timeout=3):
    """Continuously listens for speech and returns transcription when silence is detected."""
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    with microphone as source:
        print("Adjusting for ambient noise...")
        recognizer.adjust_for_ambient_noise(source)
        print("Listening...")

        while True:
            try:
                # Listen to the audio
                audio = recognizer.listen(source, phrase_time_limit=None, timeout=None)
                print("Processing speech...")

                # Convert speech to text (Try English first)
                text = recognizer.recognize_google(audio, language="en-US")
                print(f"Recognized (English): {text}")
                return text, 'en'
            
            except sr.UnknownValueError:
                # If English recognition fails, try Hindi
                try:
                    text = recognizer.recognize_google(audio, language="hi-IN")
                    print(f"Recognized (Hindi): {text}")
                    return text, 'hi'
                except sr.UnknownValueError:
                    print("Could not understand speech.")
                    return None, None


def generate_response_with_gemini(text, max_tokens=200):
    """Generate a response using Google's Gemini API."""
    prompt = (
        "You are having a natural speech conversation with a user. Your responses should be clear, concise, and to the point. "
        "Adjust response length dynamically based on context—short for simple queries, longer for complex ones. "
        f"User: {text}\n"
        "AI:"
    )

    try:
        model = genai.GenerativeModel("gemini-2.0-flash")
        response = model.generate_content(prompt, generation_config={
            "max_output_tokens": max_tokens,
            "temperature": 0.7,
            "top_p": 0.9
        })

        # Ensure response is correctly extracted
        if hasattr(response, "text") and response.text.strip():
            return response.text.strip()
        else:
            return "Sorry, I couldn't generate a response."
    except Exception as e:
        print(f"Gemini API Error: {e}")
        return "Sorry, there was an issue generating a response."


def text_to_speech(text, lang):
    """Convert text to speech and play it."""
    temp_file = "response.mp3"
    tts = gTTS(text=text, lang=lang, slow=False)
    tts.save(temp_file)

    # Play the generated speech
    pygame.mixer.music.load(temp_file)
    pygame.mixer.music.play()

    # Wait for audio to finish playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    # Clean up
    pygame.mixer.music.unload()
    os.remove(temp_file)
