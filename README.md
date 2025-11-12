

````markdown
# Speech-to-Text


This project demonstrates basic Automatic Speech Recognition (ASR) functionality and can be extended for advanced speech applications, such as real-time transcription or language analysis.

---

##  Setup and Run Instructions

Follow these steps to set up and run the project locally:

### 1. Clone the Repository
```bash
git clone https://github.com/Pratik-Ninawe/Speech-to-Text.git
cd Speech-to-Text
````

### 2. Create and Activate a Virtual Environment

```bash
python -m venv venv

# Activate on Windows
venv\Scripts\activate

# Activate on macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Project

Run the main script to perform speech recognition:

```bash
python speech_to_text.py
```

* **Audio file input:** Make sure you have a `.wav` file (e.g., `sample.wav`) in the project folder.
* **Microphone input:** Ensure your microphone is connected and accessible.

### 5. Deactivate Virtual Environment (Optional)

```bash
deactivate
```

**Note:** No additional models or datasets are required. The project uses online or system-provided speech recognition engines through the `SpeechRecognition` library.

---

##  Dataset Information

* This project **does not use any external dataset**.
* It works directly with user-provided or recorded audio inputs (e.g., `.wav` files).
* No preprocessing is required for the input files.

---

##  Repository Directory Structure

```
Speech-to-Text/
├── audio/                      # (folder)
├── .gitignore
├── README.md
├── gui_stt.py
├── requirements.txt
├── stt_google.py
├── stt_whisper.py
└── stt_whisper_realtime.py
```

---

##  Example Usage

### Example Input

Audio file: `sample.wav` containing:

> "Hello, my name is Pratik and I am testing this speech to text project."

### Example Output


```
hello my name is pratik and i am testing this speech to text project
```

---

##  Project Workflow

**Text-based workflow diagram:**

```
 Audio Input  →   Processing (SpeechRecognition + PyAudio)
                        ↓
                   Speech-to-Text Conversion
                        ↓
                   Output Transcript (Text File)
```


---

##  Programming Languages, Libraries, and Tools

| Category                 | Library / Tool      | Purpose                                      |
| ------------------------ | ------------------- | -------------------------------------------- |
| **Core ASR**             | `SpeechRecognition` | Handles speech-to-text transcription         |
| **Audio I/O**            | `PyAudio`           | Captures and processes audio from microphone |
| **File Handling**        | `wave`, `os`        | Manages and reads `.wav` files               |
| **Programming Language** | Python 3            | Implementation language                      |
| **Environment**          | `venv`              | Virtual environment management               |
| **Version Control**      | Git & GitHub        | Repository hosting and versioning            |

---


##  Author

**Pratik Ninawe**


