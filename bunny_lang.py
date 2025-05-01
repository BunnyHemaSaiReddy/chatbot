from deep_translator import GoogleTranslator

def trans(text, to_lang, from_lang='en'):
    translated_text = GoogleTranslator(source=from_lang, target=to_lang).translate(text)
    return translated_text

text = '''Narendra Modi

Current Position: Prime Minister of India (since 2014)

Personal Information:

Born: September 17, 1950, Vadnagar, Gujarat, India
Religion: Hinduism
Marital Status: Unmarried
... (rest of your text) ...
'''

# Example usage:
# print(trans(text, 'hi'))  # Translate to Hindi

def lang():
    from deep_translator.constants import GOOGLE_LANGUAGES_TO_CODES
    return GOOGLE_LANGUAGES_TO_CODES
