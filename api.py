from openai import OpenAI
import openai
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)
CORS(app)


client = OpenAI()

@app.route('/api/stt', methods=['POST'])
def stt():
    print('요청 들어옴')
    if 'audio' not in request.files:
        return jsonify({"error": "No audio file part"}), 400
    audio_file = request.files['audio']
    audio_file.save('./file/' + audio_file.filename)
    print(audio_file)
    files = open("file/recording.mp3", "rb")
    try:
        transcription = client.audio.transcriptions.create(
            model = "whisper-1",
            file = files
        )
        print(transcription.text)
        response = jsonify({"text": transcription.text})
        response.headers.add('Access-Control-Allow-Origin', '*')

        return response
    except Exception as e:
        return jsonify({'error': str(e)}, 500)


if __name__ == "__main__":
    app.run(debug=True)
