import tkinter as tk
from deep_translator import GoogleTranslator

class TranslationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Language Translation App")
        self.translation_history = []

        # Create input fields
        self.text_label = tk.Label(root, text="Enter text to translate:")
        self.text_label.pack()
        self.text_entry = tk.Text(root, height=10, width=40)
        self.text_entry.pack()

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
            "Hindi": "hi",
            "Indonesian": "id",
            "Tagalog": "tl",
            "Thai": "th",
            "Vietnamese": "vi",
            "Turkish": "tr",
            "Polish": "pl",
            "Dutch": "nl",
            "Swedish": "sv",
            "Tamil": "ta",
        }

        self.source_language_label = tk.Label(root, text="Select source language:")
        self.source_language_label.pack()
        self.source_language_var = tk.StringVar(root)
        self.source_language_var.set("English")
        self.source_language_option = tk.OptionMenu(root, self.source_language_var, *self.languages.keys())
        self.source_language_option.pack()

        self.target_language_label = tk.Label(root, text="Select target language:")
        self.target_language_label.pack()
        self.target_language_var = tk.StringVar(root)
        self.target_language_var.set("Spanish")
        self.target_language_option = tk.OptionMenu(root, self.target_language_var, *self.languages.keys())
        self.target_language_option.pack()

        # Create buttons
        self.button_frame = tk.Frame(root)
        self.button_frame.pack()
        self.translate_button = tk.Button(self.button_frame, text="Translate", command=self.translate_text)
        self.translate_button.pack(side=tk.LEFT)
        self.clear_button = tk.Button(self.button_frame, text="Clear", command=self.clear_fields)
        self.clear_button.pack(side=tk.LEFT)
        self.swap_button = tk.Button(self.button_frame, text="Swap Languages", command=self.swap_languages)
        self.swap_button.pack(side=tk.LEFT)

        # Create output field
        self.output_label = tk.Label(root, text="Translated text:")
        self.output_label.pack()
        self.output_text = tk.Text(root, height=10, width=40)
        self.output_text.pack()

        # Create history field
        self.history_label = tk.Label(root, text="Translation History:")
        self.history_label.pack()
        self.history_text = tk.Text(root, height=10, width=40)
        self.history_text.pack()

    def translate_text(self):
        text = self.text_entry.get("1.0", tk.END)
        source_language = self.languages[self.source_language_var.get()]
        target_language = self.languages[self.target_language_var.get()]

        translator = GoogleTranslator(source=source_language, target=target_language)
        translation = translator.translate(text)

        self.output_text.delete("1.0", tk.END)
        self.output_text.insert("1.0", translation)
        self.translation_history.append(f"{self.source_language_var.get()} -> {self.target_language_var.get()}: {text} -> {translation}")
        self.update_history()

    def clear_fields(self):
        self.text_entry.delete("1.0", tk.END)
        self.output_text.delete("1.0", tk.END)

    def swap_languages(self):
        source_language = self.source_language_var.get()
        target_language = self.target_language_var.get()
        self.source_language_var.set(target_language)
        self.target_language_var.set(source_language)

    def update_history(self):
        self.history_text.delete("1.0", tk.END)
        for history in self.translation_history:
            self.history_text.insert(tk.END, history + "\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = TranslationApp(root)
    root.mainloop()
