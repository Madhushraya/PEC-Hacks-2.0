# Translation Glasses: Empowering Vision with AI

This project provides a comprehensive solution for multimodal input processing, allowing both speech and text inputs to be recognized, translated, and converted into speech in the desired language. It integrates powerful tools such as Vosk for speech recognition, FastText for language detection, Argos Translate for translation, and pyttsx3 for text-to-speech synthesis.

## Features

- **Speech Recognition**: Recognize spoken input using Vosk's ASR models.
- **Text Recognition**: Perform OCR on visual input using PaddleOCR.
- **Language Detection**: Automatically detect the input language using FastText.
- **Translation**: Translate recognized text to a target language using Argos Translate.
- **Text-to-Speech**: Convert translated text into speech using pyttsx3.
- **Model Management**: Automatically download Vosk models as needed.

## Installation

### Prerequisites

1. Python 3.8 or later
2. pip (Python package manager)

### Required Libraries

Install the required Python packages:

```bash
pip install vosk pyttsx3 paddleocr fasttext opencv-python-headless argostranslate tqdm requests
```

### Vosk Models

Ensure you have the necessary Vosk models. The program can download them automatically if they are not already available locally.

### FastText Model

Download the FastText language identification model `lid.176.bin`:

```bash
wget https://dl.fbaipublicfiles.com/fasttext/supervised-models/lid.176.bin
```

### Argos Translate Models

Argos Translate will dynamically download and install the required language translation models.

## Usage

Run the program and choose between audio or visual input for translation:

```bash
python main.py
```

### Audio Mode

- Speak into the microphone.
- The program detects the spoken language, translates the text to the target language, and plays the translated text as speech.

### Visual Mode

- Use the webcam to capture an image containing text.
- The program extracts text using OCR, detects the language, translates it, and optionally speaks the translated text.

## Configuration

### Supported Languages

Update the `language_map` in the `speak_text` function to customize supported languages and voices.

### Default Models

The default Vosk models and their URLs are configured in the `model_urls` variable. Modify as needed for additional languages.

## File Structure

```
project/
├── main.py               # Main program integrating all functionalities
├── vosk_models/          # Directory for storing Vosk models
├── lid.176.bin           # FastText language identification model
├── requirements.txt      # List of required Python libraries
├── README.md             # Project documentation
```

## Examples

### Audio Input

1. Speak in any supported language.
2. The program detects the language, translates it to the target language, and speaks the translation.

### Visual Input

1. Press `c` to capture a frame.
2. The text in the frame is extracted, translated, and optionally spoken.

## Troubleshooting

- **Model Not Found**: Ensure Vosk models are downloaded and placed in the `vosk_models` directory.
- **No Audio Output**: Verify that `pyttsx3` is properly configured for your system.
- **Dependencies Missing**: Run `pip install -r requirements.txt` to install all required dependencies.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License. See `LICENSE` for details.

## Acknowledgments

- [Vosk](https://alphacephei.com/vosk/)
- [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR)
- [FastText](https://fasttext.cc/)
- [Argos Translate](https://github.com/argosopentech/argos-translate)
