from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Rectangle
from deep_translator import GoogleTranslator

class TranslationApp(App):
    def build(self):
        layout = FloatLayout()

        # Background
        with layout.canvas.before:
            Color(0.9, 0.9, 0.9, 1)
            Rectangle(size=(800, 600))

        # Create input fields
        self.text_input = TextInput(
            hint_text='Enter text to translate',
            size_hint=(0.8, 0.3),
            pos_hint={'x': 0.1, 'y': 0.6}
        )
        layout.add_widget(self.text_input)

        # Create language options
        self.languages = {
            "English": "en",
            "Spanish": "es",
            "French": "fr",
            "German": "de",
            "Italian": "it",
            "Portuguese": "pt",
            "Chinese": "zh",
            "Japanese": "ja",
            "Korean": "ko",
            "Arabic": "ar",
            "Russian": "ru",
            "Indonesian": "id",
            "Tagalog": "tl",
            "Thai": "th",
            "Vietnamese": "vi",
            "Turkish": "tr",
            "Polish": "pl",
            "Dutch": "nl",
            "Swedish": "sv",
        }
        self.source_language = Spinner(
            text='English',
            values=list(self.languages.keys()),
            size_hint=(0.3, 0.05),
            pos_hint={'x': 0.1, 'y': 0.5}
        )
        layout.add_widget(self.source_language)
        self.target_language = Spinner(
            text='Spanish',
            values=list(self.languages.keys()),
            size_hint=(0.3, 0.05),
            pos_hint={'x': 0.6, 'y': 0.5}
        )
        layout.add_widget(self.target_language)

        # Create buttons
        self.translate_button = Button(
            text='Translate',
            size_hint=(0.2, 0.05),
            pos_hint={'x': 0.4, 'y': 0.4}
        )
        self.translate_button.bind(on_press=self.translate_text)
        layout.add_widget(self.translate_button)

        # Create output field
        self.output_text = TextInput(
            hint_text='Translated text',
            readonly=True,
            size_hint=(0.8, 0.3),
            pos_hint={'x': 0.1, 'y': 0.1}
        )
        layout.add_widget(self.output_text)

        return layout

    def translate_text(self, instance):
        text = self.text_input.text
        source_language = self.languages[self.source_language.text]
        target_language = self.languages[self.target_language.text]
        translator = GoogleTranslator(source=source_language, target=target_language)
        translation = translator.translate(text)
        self.output_text.text = translation

if __name__ == '__main__':
    TranslationApp().run()
