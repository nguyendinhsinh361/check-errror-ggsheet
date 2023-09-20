from src.helpers import unicode
import re
# Column text_question


def check_structure_where(text):
    check = text.split("\"")
    return unicode.is_vietnamese(check[0]) and check[0].strip() == "Đâu là" and check[2].strip() == "?"


def check_written_by_japanese(text):
    return all(unicode.is_japanese(element) or not unicode.is_latin(element) for element in text)


def check_appear_only_have_one_han_char(text):
    return unicode.count_han_words(text) == 1


def check_appear_more_two_han_char(text):
    return unicode.count_han_words(text) >= 2


def check_written_by_vietnamese(text):
    return not check_written_by_japanese(text)


def check_structure_translate(text):
    check = text.split("\"")
    return unicode.is_vietnamese(check[1]) and check[0].strip() == "Dịch" and check[2].strip() == ""


def check_contain_a_pair_of_parentheses(text):
    return unicode.count_pair_of_parentheses(text) == 1


def check_contain_more_pair_of_parentheses(text):
    return unicode.count_pair_of_parentheses(text) >= 1


# Column kana_question

def check_match_column(col1, col2):
    # Pending
    return True

# Column hanviet_question


def check_written_by_capital_vietnamese(text):
    return unicode.is_vietnamese(text) and text == text.upper()

# Column audio


def check_have_tag_p_or_h(text):
    return bool(re.search(r'<[phPH][^>]*>.*?</[phPH]>', text))


def check_like_column(col1):
    # Pending
    clean_text = unicode.get_clean_text(col1)
    print(111, clean_text)
    return True

# Column image


def check_has_content(text):
    return bool(text)

# Column answer


def check_has_two_or_four_answers(text):
    answer_arr = text.split("\n")
    answer_arr = [element.strip()
                  for element in answer_arr if element.strip() != ""]
    return len(answer_arr) == 2 or len(answer_arr) == 4


def check_has_max_four_answers(text):
    answer_arr = text.split("\n")
    answer_arr = [element.strip()
                  for element in answer_arr if element.strip() != ""]
    return len(answer_arr) <= 4 and len(set(answer_arr)) == len(answer_arr)


def check_contains_enough_words(col1_answer, col2_correct_ans):
    words_col1 = [element.strip() for element in col1_answer.split(
        "\n") if element.strip() != ""]
    words_col2 = [element.strip() for element in col2_correct_ans.split(
        "\n") if element.strip() != ""]
    return all(element in words_col1 for element in words_col2)


def check_contains_noise_words(col1_answer, col2_correct_ans):
    words_col1 = [element.strip() for element in col1_answer.split(
        "\n") if element.strip() != ""]
    words_col2 = [element.strip() for element in col2_correct_ans.split(
        "\n") if element.strip() != ""]
    return len(words_col1) > len(words_col2) and not (len(set(words_col1)) == len(set(words_col2)))


def check_format_sentence(text):
    return bool(text[len(text) - 1] == ".") or text[0] == text[0].upper()


def check_order_words_diff(col1_answer, col2_correct_ans):
    words_col1 = [element.strip() for element in col1_answer.split(
        "\n") if element.strip() != ""]
    words_col2 = [element.strip() for element in col2_correct_ans.split(
        "\n") if element.strip() != ""]
    return all(words_col2[i] == words_col1[i] for i in range(len(words_col2)))


def check_audio_contains_answers_accept_dots(col1_answer, col2_audio):
    words_col1 = [element.strip() for element in col1_answer.split(
        "\n") if element.strip() != ""]
    return any(str(element.rstrip(".")) == str(col2_audio.rstrip("."))
               for element in words_col1)


def check_audio_contains_answers(col1_answer, col2_audio):
    words_col1 = [element.strip() for element in col1_answer.split(
        "\n") if element.strip() != ""]
    return any(str(element) == str(col2_audio) for element in words_col1)


def check_count_japanese_words(text):
    words = [element.strip()
             for element in text.split("\n") if element.strip() != ""]
    return all(len(element) <= 2 for element in words)


def check_has_punctuation(text):
    words = [element.strip()
             for element in text.split("\n") if element.strip() != ""]
    words_str = "".join(words)
    return all(unicode.is_japanese(element) for element in words_str)


def check_structure_pair_of_parentheses(text):
    return text.startswith('(') and text.endswith(')')


def check_muitii_line_breaks(text):
    line = [element.strip()
            for element in text.split("\n") if element.strip() != ""]
    return len(line) > 1


# Column Image_answer

# Column corect_answer

def check_type_number(text):
    return unicode.is_number(text)


def check_pairing_method(text):
    return True


def check_type_number_and_like_number_audio(text):
    # Pending
    another_con = True
    return unicode.is_number(text) and another_con


def check_correct_answer_like_audio(col1_corect_answer, col2_audio):
    line = [element.strip()
            for element in col1_corect_answer.split("\n") if element.strip() != ""]
    completed_text = "".join(line)
    return completed_text == col2_audio


def check_correct_answer_has_pair_of_parentheses_and_like_answer(col1_corect_answer, col2_answer):
    # Pending
    open_count = col1_corect_answer.count('(')
    close_count = col1_corect_answer.count(')')
    another_con = True
    return open_count > 1 and close_count > 1 and another_con
