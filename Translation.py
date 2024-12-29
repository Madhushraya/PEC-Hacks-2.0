import argostranslate.package
import argostranslate.translate

def translate_text(text: str, from_code: str = "en", to_code: str = "pt") -> str:
    installed_languages = argostranslate.translate.get_installed_languages()

    from_lang = next((lang for lang in installed_languages if lang.code == from_code), None)
    to_lang = next((lang for lang in installed_languages if lang.code == to_code), None)

    if not from_lang or not to_lang:
        return "Language code not found or language not installed."

    translate = from_lang.get_translation(to_lang)
    translated_text = translate.translate(text)
    return translated_text

print(translate_text("Hello, how are you?", from_code="en", to_code="hi"))