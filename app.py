# app.py

from flask import Flask, jsonify, render_template
import time
import threading
from processing import *

app = Flask(__name__)

# Global thread and stop event
conversation_thread = None
stop_event = threading.Event()

@app.route('/')
def index():
    return render_template('index.html')

def conversation_loop():
    while not stop_event.is_set():
        text, detected_language = listen_for_speech()
        if not text:
            print("Speech not recognized, retrying...")
            continue

        print(f"User said: {text} (Detected language: {detected_language})")
        response_text = generate_response_with_gemini(text)
        print(f"AI response: {response_text}")
        text_to_speech(response_text, lang=detected_language)

@app.route('/start', methods=['GET'])
def start_conversation():
    global conversation_thread, stop_event

    if conversation_thread and conversation_thread.is_alive():
        return jsonify({"message": "Conversation already running."}), 400

    stop_event.clear()
    conversation_thread = threading.Thread(target=conversation_loop)
    conversation_thread.start()
    return jsonify({"message": "Speech conversation started"}), 200

@app.route('/stop', methods=['GET'])
def stop_conversation():
    global stop_event

    if not conversation_thread or not conversation_thread.is_alive():
        return jsonify({"message": "No conversation is running."}), 400

    stop_event.set()
    return jsonify({"message": "Speech conversation stopped"}), 200

if __name__ == "__main__":
    app.run(debug=True, port=5001)
