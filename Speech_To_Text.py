import os
import wave
import json
import vosk
import pyaudio

def load_model(language_code):
    models = {
        "en": "C:\\Users\\Manu\\OneDrive\\Desktop\\PEC HACKATHON\\vosk-model-small-en-us-0.15",
        "ko": "C:\\Users\\Manu\\OneDrive\\Desktop\\PEC HACKATHON\\vosk-model-small-ko-0.22",
        "sw": "C:\\Users\\Manu\\OneDrive\\Desktop\\PEC HACKATHON\\vosk-model-small-sv-rhasspy-0.15\\vosk-model-small-sv-rhasspy-0.15",
        "hi":  "C:\\Users\\Manu\\OneDrive\\Desktop\\PEC HACKATHON\\vosk-model-small-hi-0.22" 
    }
    if language_code in models:
        model_path = models[language_code]
        if os.path.exists(model_path):
            return vosk.Model(model_path)
        else:
            raise FileNotFoundError(f"Model path not found: {model_path}")
    else:
        raise ValueError(f"Language model for '{language_code}' is not configured.")

def speech_to_text(language_code="en"):
    model = load_model(language_code)
    audio_interface = pyaudio.PyAudio()
    stream = audio_interface.open(
        format=pyaudio.paInt16,
        channels=1,
        rate=16000,
        input=True,
        frames_per_buffer=8000
    )
    stream.start_stream()

    print(f"Listening... Speak in {language_code.upper()}.")

    recognizer = vosk.KaldiRecognizer(model, 16000)

    try:
        while True:
            data = stream.read(4000, exception_on_overflow=False)

            if recognizer.AcceptWaveform(data):
                result = json.loads(recognizer.Result())
                print(f"[{language_code.upper()}] Recognized text:", result.get("text", ""))

    except KeyboardInterrupt:
        print("Stopping...")

    finally:
        stream.stop_stream()
        stream.close()
        audio_interface.terminate()

if __name__ == "__main__":
    language_code = input("Enter language code (en, ko, sw, hi): ").strip().lower()
    speech_to_text(language_code)
