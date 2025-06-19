

Language Translation App 🌎💬

Overview
A Python-based app that translates text between multiple languages using Tkinter, Kivy, and deep_translator libraries. Features include text translation, language selection, and a user-friendly GUI.

Features
- *Text Translation*: Translate text from one language to another 🌐
- *Language Selection*: Select source and target languages 📚
- *GUI*: User-friendly graphical interface built using Tkinter and Kivy 📱

Libraries Used
- *Tkinter*: For building the initial GUI version of the app 🐍
- *Kivy*: For building the mobile-friendly version of the app 📱
- *deep_translator*: For translating text between languages 🤖

Installation
To run this app, you'll need to install the following libraries:

Prerequisites
- Python 3.x installed on your system
- pip (Python package manager) installed on your system

Installation Steps
1. Clone the repository: `git clone https://github.com/Reaishma/Language-translator-.git`
2. Navigate to the project directory: `cd Language-translator-`
3. Install the required libraries: `pip install -r requirements.txt`
4. Run the app: `python main.py`

Code Snippets
Here's a sample code snippet for translating text using the `deep_translator` library:

from deep_translator import GoogleTranslator

def translate_text(text, source_language, target_language):
    translator = GoogleTranslator(source=source_language, target=target_language)
    translation = translator.translate(text)
    return translation

text = "Hello, how are you?"
source_language = "en"
target_language = "es"

translation = translate_text(text, source_language, target_language)
print(translation)

Contribution Guidelines
contributions are welcomed to this project! Here's how you can contribute:

1. Fork the repository
2. Create a new branch for your feature or bug fix
3. Make your changes and commit them
4. Open a pull request with a clear description of your changes

Coding Standards
- Follow PEP 8 guidelines for Python code
- Use consistent naming conventions and formatting

Pull Request Guidelines
- Provide a clear description of your changes
- Include relevant screenshots or examples
- Ensure that your changes do not break existing functionality

Challenges Overcome
- *Language Code Issues*: Ensured correct and consistent language codes 🔍
- *Library Compatibility*: Ensured compatibility between libraries and app requirements 📊

Final Result
A functional language translation app that can translate text between multiple languages 🌈

Screenshots
For output screenshots, please refer to the attached document:
https://docs.google.com/document/d/1Rj2CC7RZBfNUssNO6GYRBFewmq7Q4yIk/edit?usp=drivesdk&ouid=106517890474604036558&rtpof=true&sd=true 📸

Author
- *Reaishma N* 🙋‍♀️

License
MIT License 📄

