from flask import Flask, jsonify, render_template
import time
import threading
from processing import *

app = Flask(__name__)

@app.route('/')
def index():
    """Serve the UI"""
    return render_template('index.html')

# Function to handle the conversation loop
def conversation_loop():
    while True:
        # Step 1: Listen for speech
        text, detected_language = listen_for_speech()
        if not text:
            print("Speech not recognized, retrying...")
            continue
        
        print(f"User said: {text} (Detected language: {detected_language})")

        # Step 2: Generate AI Response
        response_text = generate_response_with_gemini(text)
        print(f"AI response: {response_text}")

        # Step 3: Convert response to speech
        text_to_speech(response_text, lang=detected_language)

@app.route('/start', methods=['GET'])
def start_conversation():
    """Start the speech conversation loop."""
    threading.Thread(target=conversation_loop).start()
    return jsonify({"message": "Speech conversation started"}), 200

if __name__ == "__main__":
    app.run(debug=True)
