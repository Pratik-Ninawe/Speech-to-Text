from transformers import WhisperProcessor, WhisperForConditionalGeneration
import whisper
import torch

def transcribe_audio(file_path):
    model_name = "openai/whisper-small"
    processor = WhisperProcessor.from_pretrained(model_name)
    model = WhisperForConditionalGeneration.from_pretrained(model_name)

    # Load and resample audio (whisper's own function)
    audio = whisper.load_audio(file_path)
    audio = whisper.pad_or_trim(audio)

    input_features = processor(audio, sampling_rate=16000, return_tensors="pt").input_features
    predicted_ids = model.generate(input_features)
    transcription = processor.batch_decode(predicted_ids, skip_special_tokens=True)[0]

    print("Transcribed Text:", transcription)
    with open("transcription_whisper.txt", "w", encoding="utf-8") as f:
        f.write(transcription)


if __name__ == "__main__":
    audio_file = "audio/sample.wav"  # Replace with your audio path
    transcribe_audio(audio_file)
