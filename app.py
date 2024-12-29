import os
import cv2
from paddleocr import PaddleOCR
from PIL import Image
import numpy as np
import fasttext
import pyttsx3
import argostranslate.package
import argostranslate.translate
from vosk import Model, KaldiRecognizer
import wave
import json

def speak_text(text, language):
    try:
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)
        engine.setProperty('volume', 1.0)
        voices = engine.getProperty('voices')
        language_map = {
            'english_uk': 29,
            'english_us': 30,
            'french': 23,
            'italian': 25,
            'portuguese': 26,
            'dutch': 141,
            'swedish': 137,
        }
        if language.lower() in language_map:
            engine.setProperty('voice', voices[language_map[language.lower()]].id)
        else:
            print("Language not found! Defaulting to English (US).")
            engine.setProperty('voice', voices[30].id)
        engine.say(text)
        engine.runAndWait()
    finally:
        engine.stop()

def translate_text(text, from_code="en", to_code="en"):
    installed_languages = argostranslate.translate.get_installed_languages()

    from_lang = next((lang for lang in installed_languages if lang.code == from_code), None)
    to_lang = next((lang for lang in installed_languages if lang.code == to_code), None)

    if not from_lang or not to_lang:
        return "Language code not found or language not installed."

    translate = from_lang.get_translation(to_lang)
    return translate.translate(text)

def detect_language(text):
    model = fasttext.load_model('lid.176.bin')
    predicted_language, probability = model.predict(text)
    return predicted_language[0].split('__label__')[1]

def process_visual_translation():
    ocr = PaddleOCR(use_angle_cls=True, lang='en')
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not access the webcam.")
        return

    print("Press 'c' to capture a frame for OCR processing, 'q' to quit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to capture image.")
            break

        cv2.imshow("Webcam Feed", frame)
        key = cv2.waitKey(1) & 0xFF
        if key == ord('c'):
            print("Capturing frame for OCR processing...")
            pil_image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            results = ocr.ocr(np.array(pil_image), cls=True)
            if results and len(results[0]) > 0:
                recognized_texts = [res[1][0] for res in results[0]]
                full_text = " ".join(recognized_texts)
                detected_language = detect_language(full_text)
                print(f"Detected Language: {detected_language}")
                translated_text = translate_text(full_text, from_code=detected_language, to_code="en")
                print(f"Translated Text: {translated_text}")
            else:
                print("No text recognized in the captured frame.")

        elif key == ord('q'):
            print("Exiting...")
            break

    cap.release()
    cv2.destroyAllWindows()

def process_audio_translation():
    vosk_model_path = "./vosk_models/vosk-model-en-us-0.22"

    if not os.path.exists(vosk_model_path):
        print("Vosk model not found. Please download and place it in the correct path.")
        return

    model = Model(vosk_model_path)
    rec = KaldiRecognizer(model, 16000)
    
    print("Recording audio... Speak into the microphone.")

    import pyaudio
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
    stream.start_stream()

    print("Speak now, and stop speaking to end the recording.")
    audio_frames = []

    try:
        while True:
            data = stream.read(4000)
            if rec.AcceptWaveform(data):
                audio_frames.append(data)
                break
    except KeyboardInterrupt:
        pass

    stream.stop_stream()
    stream.close()
    p.terminate()

    audio_data = b''.join(audio_frames)
    recognized_text = json.loads(rec.FinalResult())['text']
    detected_language = detect_language(recognized_text)

    print(f"Recognized Text: {recognized_text}")
    print(f"Detected Language: {detected_language}")

    translated_text = translate_text(recognized_text, from_code=detected_language, to_code="en")
    print(f"Translated Text: {translated_text}")
    speak_text(translated_text, "english_us")

if __name__ == "__main__":
    print("Select mode:")
    print("1. Visual Translation")
    print("2. Audio Translation")

    mode = input("Enter 1 or 2: ")

    if mode == "1":
        process_visual_translation()
    elif mode == "2":
        process_audio_translation()
    else:
        print("Invalid selection. Exiting.")
