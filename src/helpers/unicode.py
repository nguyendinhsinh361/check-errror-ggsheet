from bs4 import BeautifulSoup
import re


def is_japanese(word):
    return '\u4e00' <= word <= '\u9fff' or '\u3040' <= word <= '\u30ff'


def is_vietnamese(text):
    return not is_japanese(text)


def is_han(word):
    return all('\u4e00' <= char <= '\u9fff' for char in word)


def is_latin(text):
    latin_character = re.compile(r'^[a-zA-Z]+$')
    return bool(latin_character.match(text))


def count_han_words(text):
    han_word_count = 0

    for char in text:
        if is_han(char):
            print(char)
            han_word_count += 1
    return han_word_count


def count_pair_of_parentheses(text):
    text_sparate = text.split("()")
    return len(text_sparate) - 1


def get_clean_text(text):

    # Parse the HTML
    soup = BeautifulSoup(text, 'html.parser')

    result = ' '.join(soup.find_all(text=True))
    return result


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False