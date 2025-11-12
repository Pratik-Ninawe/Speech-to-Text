import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import threading
import sounddevice as sd
import numpy as np
import librosa
import torch
from transformers import WhisperProcessor, WhisperForConditionalGeneration
import speech_recognition as sr


# Whisper Model
MODEL_NAME = "openai/whisper-small"
processor = WhisperProcessor.from_pretrained(MODEL_NAME)
model = WhisperForConditionalGeneration.from_pretrained(MODEL_NAME)
SAMPLE_RATE = 16000


# Helper Functions

def record_audio(duration=5):
    """Record from microphone"""
    append_output(f"Recording for {duration} seconds...")
    audio = sd.rec(int(duration * SAMPLE_RATE), samplerate=SAMPLE_RATE, channels=1, dtype='float32')
    sd.wait()
    append_output("Recording finished.")
    return audio.flatten()

def transcribe_whisper_audio(audio_array):
    """Transcribe raw audio array"""
    input_features = processor(audio_array, sampling_rate=SAMPLE_RATE, return_tensors="pt").input_features
    predicted_ids = model.generate(input_features)
    transcription = processor.batch_decode(predicted_ids, skip_special_tokens=True)[0]
    return transcription

def transcribe_audio_file(file_path):
    """Transcribe audio file using Whisper (librosa instead of torchaudio)"""
    try:
        audio, sr = librosa.load(file_path, sr=SAMPLE_RATE, mono=True)
    except Exception as e:
        return f"Error loading audio: {e}"

    try:
        input_features = processor(audio, sampling_rate=SAMPLE_RATE, return_tensors="pt").input_features
        predicted_ids = model.generate(input_features)
        transcription = processor.batch_decode(predicted_ids, skip_special_tokens=True)[0]
        return transcription
    except Exception as e:
        return f"Error during transcription: {e}"

def google_stt_microphone():
    """Google SpeechRecognition from mic"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        append_output("🎙️ Recording from microphone using Google STT...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        append_output(f"Google STT Output: {text}")
    except sr.UnknownValueError:
        append_output("Could not understand audio.")
    except sr.RequestError:
        append_output("API request failed.")

def whisper_realtime_stt():
    """Record via mic and transcribe using Whisper"""
    try:
        duration = int(duration_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Duration must be an integer (seconds)")
        return

    append_output(f"Recording {duration}s via Whisper Realtime...")
    audio = record_audio(duration)
    text = transcribe_whisper_audio(audio)
    append_output(f"Whisper Realtime Output: {text}")

def whisper_file_stt():
    """Transcribe an existing audio file"""
    file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.wav *.mp3 *.flac *.m4a")])
    if not file_path:
        return

    append_output(f"Transcribing file: {file_path}")
    text = transcribe_audio_file(file_path)
    append_output(f"Whisper File Output: {text}")

def append_output(message):
    """Append message to GUI output box"""
    output_text.insert(tk.END, message + "\n")
    output_text.see(tk.END)

def run_in_thread(func):
    """Run function in background thread"""
    threading.Thread(target=func, daemon=True).start()


# GUI Layout
root = tk.Tk()
root.title("🎤 Speech-to-Text NLP Project")
root.geometry("800x600")
root.resizable(False, False)
root.config(bg="#1e1e2f")

# Title
title_label = tk.Label(root, text="Speech-to-Text NLP Project", font=("Helvetica", 18, "bold"), bg="#1e1e2f", fg="#f1f1f1")
title_label.pack(pady=10)

# Duration input
duration_frame = tk.Frame(root, bg="#1e1e2f")
duration_frame.pack(pady=5)
tk.Label(duration_frame, text="Duration (sec):", font=("Helvetica", 12), bg="#1e1e2f", fg="#f1f1f1").pack(side=tk.LEFT)
duration_entry = tk.Entry(duration_frame, width=5)
duration_entry.insert(0, "5")
duration_entry.pack(side=tk.LEFT, padx=5)

# Buttons Frame
button_frame = tk.Frame(root, bg="#1e1e2f")
button_frame.pack(pady=10)

tk.Button(button_frame, text="Google STT (Mic)", font=("Helvetica", 12), command=lambda: run_in_thread(google_stt_microphone), bg="#4caf50", fg="white", width=18).grid(row=0, column=0, padx=5, pady=5)
tk.Button(button_frame, text="Whisper Realtime (Mic)", font=("Helvetica", 12), command=lambda: run_in_thread(whisper_realtime_stt), bg="#2196f3", fg="white", width=18).grid(row=0, column=1, padx=5, pady=5)
tk.Button(button_frame, text="Whisper File", font=("Helvetica", 12), command=lambda: run_in_thread(whisper_file_stt), bg="#9c27b0", fg="white", width=18).grid(row=1, column=0, padx=5, pady=5)

# Output Text Box
output_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=20, font=("Helvetica", 12), bg="#2e2e3e", fg="white")
output_text.pack(pady=10, padx=10)

# Run GUI
root.mainloop()
