import re
from nltk.corpus import stopwords


# Preprocesses text and returns clean text
def clean_text(text):
    regex_legal_letters = re.compile('[^ \\t\\n\\v\\f\\ra-zA-Z]')
    text = regex_legal_letters.sub('', text)
    text = text.lower()
    words_arr = text.split()
    stop_words = set(stopwords.words('english'))
    clean_word_arr = [w for w in words_arr if not w in stop_words]
    cleanText = " ".join(word for word in clean_word_arr)
    return cleanText


# Separates text to blocks with max_text_len tokens
def separate_text_to_blocks(text, max_text_len):
    words = text.split()
    blocks = []
    current = ""
    tokens = 0
    for word in words:
        if tokens > max_text_len - 3:
            blocks.append(current)
            current = word
            tokens = 0
        else:
            current += word + " "
            tokens += 1
    blocks.append(current)
    return blocks
