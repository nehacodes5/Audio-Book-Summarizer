 🎧 Audio Book Summarizer

An AI-powered web application that converts audio files into text and generates concise summaries using advanced Speech Recognition and Natural Language Processing (NLP) techniques.

The application uses **OpenAI Whisper** for audio transcription and **NVIDIA Nemotron 3 Nano Omni** (via OpenRouter API) for intelligent text summarization.

---

🚀 Features

* Upload audio files (`.mp3`, `.wav`, `.m4a`)
* Convert audio to text using **OpenAI Whisper**
* Generate AI-powered summaries using **NVIDIA Nemotron 3 Nano Omni**
* Display complete transcript and summarized content
* Modern and responsive user interface
* Listen to uploaded audio directly on the results page

---

🛠️ Tech Stack

### Frontend

* HTML
* CSS

### Backend

* Python
* Flask

### AI Models

* OpenAI Whisper (Speech-to-Text)
* NVIDIA Nemotron 3 Nano Omni (Text Summarization)

### APIs

* OpenRouter API

---

📂 Project Structure

```bash
Audio_Book_Summarizer/
│
├── app.py
├── transcribe.py
├── summarize.py
│
├── static/
│   └── uploads/
│
├── templates/
│   ├── index.html
│   └── result.html
│
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone <your-github-repository-link>
```

### 2. Navigate to the Project Directory

```bash
cd Audio_Book_Summarizer
```

### 3. Install Required Dependencies

```bash
pip install flask
pip install openai-whisper
pip install requests
```

---

🔑 OpenRouter API Key Setup

This project uses the **OpenRouter API** to access the NVIDIA Nemotron 3 Nano Omni model for text summarization.

### 1. Create an OpenRouter Account

Visit:

https://openrouter.ai/

Create an account and generate your API key.

### 2. Add Your API Key

Open the `summarize.py` file and replace:

```python
API_KEY = "your_openrouter_api_key"
```

with:

```python
API_KEY = "sk-or-v1-your-api-key-here"
```

Example:

```python
API_KEY = "sk-or-v1-xxxxxxxxxxxxxxxxxxxxxxxx"
```

### 3. Model Used

The application uses the following NVIDIA model:

```python
"model": "nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free"
```

⚠️ Important

* Never share your API key publicly.
* Do not upload your API key to GitHub.
* Replace the API key with a placeholder before pushing the project to a public repository.

---

🎵 FFmpeg Installation

OpenAI Whisper requires FFmpeg.

Download and install FFmpeg from:

https://ffmpeg.org/download.html

After installation, add FFmpeg to your system PATH.

Verify installation:

```bash
ffmpeg -version
```

---

▶️ Running the Application

Run the Flask application:

```bash
python app.py
```

Open your browser and visit:

```bash
http://127.0.0.1:5000
```

---

📖 How It Works

1. User uploads an audio file.
2. Flask saves the uploaded file.
3. OpenAI Whisper converts the audio into text.
4. The transcript is sent to NVIDIA Nemotron 3 Nano Omni.
5. The AI model generates a concise summary.
6. The application displays both the transcript and summary.

---

🔄 Application Workflow

```text
Audio File
     ↓
OpenAI Whisper
     ↓
Transcript Generation
     ↓
NVIDIA Nemotron 3 Nano Omni
     ↓
AI Summary
```

---

🔮 Future Enhancements

* Download summary as PDF
* Multiple summary length options
* Dark mode support
* User authentication
* Summary history storage
* Summary download feature

---

👩‍💻 Author

Neha Saini

LinkedIn: www.linkedin.com/in/neha-saini-b7767329
GitHub: https://github.com/nehacodes5
