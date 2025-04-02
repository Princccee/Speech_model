# Speech-Agent: AI-Powered Speech-Based Conversation System

## Overview
Speech-Agent is a real-time speech-based conversation system that allows users to interact with an AI using voice. The system listens to the user, detects the language, transcribes the speech, generates an AI response, and converts the response back into speech. The conversation happens seamlessly with natural pauses.

## Features
- **Automatic Speech Recognition (ASR)**: Detects and transcribes user speech.
- **Language Detection**: Supports multiple languages (English & Hindi currently).
- **AI Response Generation**: Uses Google's Gemini API to generate responses dynamically.
- **Text-to-Speech (TTS)**: Converts AI responses back to speech.
- **Continuous Listening**: Detects when the user stops speaking and resumes after response.
- **Web UI (Streamlit)**: Provides a simple interface for interaction.

## Project Structure
```
Speech-agent/
├── __pycache__
│   └── processing.cpython-311.pyc
├── app.py            # Flask backend to handle speech processing
├── processing.py     # Speech recognition, language detection, AI response, TTS
├── requirements.txt  # Required dependencies
├── templates/
│   ├── home.html     # HTML template for UI
│   └── index.html    # HTML template for UI
└── ui.py             # Streamlit UI for user interaction
```

## Installation
### 1. Clone the Repository
```sh
git clone https://github.com/Princccee/Speech_model.git
cd Speech_model
```

### 2. Create a Virtual Environment & Install Dependencies
```sh
python -m venv .venv
source .venv/bin/activate   # On Windows use: .venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Set Up API Keys
Create a `.env` file in the project root and add your Google Gemini API key:
```sh
GEMINI_API_KEY=your_api_key_here
```

## Running the Application
### 1. Start the Flask Backend
```sh
python app.py
```

### 2. Start the Streamlit UI
```sh
streamlit run ui.py
```

## Usage
1. Open the Streamlit UI in your browser.
2. Click on the "Start Conversation" button.
3. Speak into the microphone and wait for the AI response.
4. The system will process the input and respond via speech.
5. Continue the conversation naturally.

## Technologies Used
- **Python** (Flask, Streamlit, SpeechRecognition, gTTS, pygame)
- **Google Gemini API** for AI-generated responses
- **gTTS (Google Text-to-Speech)** for voice synthesis
- **Pygame** for audio playback

## Future Enhancements
- Expand language support
- Improve speech detection accuracy
- Enhance UI with real-time transcript display
- Integrate with additional AI models

## Contributors
- **Your Name** ([GitHub](https://github.com/Princccee/Speech_model.git))



