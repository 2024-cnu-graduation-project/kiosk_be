from openai import OpenAI
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

client = OpenAI()

@app.route('/api/stt', methods=['GET'])
def stt():
    audio_file = open("data/TEST9.mp3", "rb")
    # audio_file = request.args.get('audio_file')
    transcription = client.audio.transcriptions.create(
        model = "whisper-1",
        file=audio_file
    )
    print(transcription.text)
    return jsonify({"text": transcription.text})


if __name__ == "__main__":
    app.run(debug=True)
