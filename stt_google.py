import speech_recognition as sr

def record_and_transcribe():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Recording... Speak something:")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    
    try:
        text = r.recognize_google(audio)
        print("You said: ", text)
        # Save to file
        with open("transcription_google.txt", "w") as f:
            f.write(text)
    except sr.UnknownValueError:
        print("Could not understand audio.")
    except sr.RequestError:
        print("API request failed. Check internet connection.")

if __name__ == "__main__":
    record_and_transcribe()
