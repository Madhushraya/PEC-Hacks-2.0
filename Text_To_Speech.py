import pyttsx3

def speak_text(text, language):
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

if __name__ == "__main__":
    text = input("Enter the text you want to speak: ")
    print("Select language:")
    print("1. English (UK)\n2. English (US)\n3. French. \n4. Italian\n5. Portuguese\n6. Dutch.\n7. Swedish")
    language_choice = input("Enter the number corresponding to the language: ")
    language_map = {
        '1': 'english_uk',
        '2': 'english_us',
        '3': 'french',
        '4': 'italian',
        '5': 'portuguese',
        '6': 'dutch',
        '7': 'swedish'
    }
    language = language_map.get(language_choice, 'english_us')
    speak_text(text, language)
