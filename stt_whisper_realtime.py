import sounddevice as sd
import numpy as np
from transformers import WhisperProcessor, WhisperForConditionalGeneration

# Load Whisper model
MODEL_NAME = "openai/whisper-small"
processor = WhisperProcessor.from_pretrained(MODEL_NAME)
model = WhisperForConditionalGeneration.from_pretrained(MODEL_NAME)

SAMPLE_RATE = 16000  # Whisper requires 16kHz audio


def record_audio(duration=5):
    print(f"Recording for {duration} seconds...")
    audio = sd.rec(int(duration * SAMPLE_RATE), samplerate=SAMPLE_RATE, channels=1, dtype="float32")
    sd.wait()
    return audio.flatten()


def transcribe(audio_array):
    input_features = processor(audio_array, sampling_rate=SAMPLE_RATE, return_tensors="pt").input_features
    predicted_ids = model.generate(input_features)
    transcription = processor.batch_decode(predicted_ids, skip_special_tokens=True)[0]
    return transcription.strip()


if __name__ == "__main__":
    duration = int(input("Enter recording duration in seconds: "))
    audio = record_audio(duration)
    text = transcribe(audio)
    print("Transcribed Text:", text)
    with open("transcription_whisper_realtime.txt", "w", encoding="utf-8") as f:
        f.write(text)
