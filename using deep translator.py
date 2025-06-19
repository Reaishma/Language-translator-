from deep_translator import GoogleTranslator

def translate_text():
    text = input("Enter text to translate: ")
    source_language = input("Enter source language (e.g. en for English): ")
    target_language = input("Enter target language (e.g. es for Spanish): ")
    translator = GoogleTranslator(source=source_language, target=target_language)
    print(translator.translate(text))

def add_translation():
    print("This feature is not supported by the deep_translator library.")
    print("However, you can use the library to translate text and store the translations in a dictionary.")

def main():
    while True:
        print("1. Translate text")
        print("2. Add translation (not supported)")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            translate_text()
        elif choice == "2":
            add_translation()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
