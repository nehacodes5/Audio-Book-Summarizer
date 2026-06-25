from flask import Flask, render_template, request
import os

# Import custom functions
from transcribe import transcribe_audio
from summarize import summarize_text

app = Flask(__name__)

# Configure upload folder
UPLOAD_FOLDER = "static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Create uploads folder if it doesn't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


# Home Page
@app.route('/')
def home():
    return render_template('index.html')


# Handle Audio Upload and Processing
@app.route('/upload', methods=['POST'])
def upload_audio():

    # Check whether a file was uploaded
    if 'audio' not in request.files:
        return "No audio file uploaded."

    file = request.files['audio']

    # Check if user selected a file
    if file.filename == '':
        return "No file selected."

    # Save uploaded file
    file_path = os.path.join(
        app.config['UPLOAD_FOLDER'],
        file.filename
    )

    file.save(file_path)

    try:
        # Convert audio to text using Whisper
        transcript = transcribe_audio(file_path)

        # Generate summary using NVIDIA Nemotron
        summary = summarize_text(transcript)

        # Display transcript and summary
        return render_template(
            'result.html',
            transcript=transcript,
            summary=summary,
            filename=file.filename
        )

    except Exception as e:
        return f"An error occurred: {str(e)}"


if __name__ == "__main__":
    app.run(debug=True)