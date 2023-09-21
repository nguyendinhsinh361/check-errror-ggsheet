from src.helpers import common
import re
# Column text_question


def check_E2_structure_where(text):
    check = text.split("\"")
    return common.is_vietnamese(check[1]) and check[0].strip() == "Đâu là" and check[2].strip() == "?"


def check_E3_written_by_japanese(text):
    return all(common.is_japanese(element) or not common.is_latin(element) for element in text)


def check_E11_appear_only_have_one_han_char(text):
    return common.count_han_words(text) == 1


def check_E12_appear_more_two_han_char(text):
    return common.count_han_words(text) >= 2


def check_E13_written_by_vietnamese(text):
    return not check_E3_written_by_japanese(text)


def check_E17_structure_translate(text):
    check = text.split("\"")
    return common.is_vietnamese(check[1]) and check[0].strip() == "Dịch" and check[2].strip() == ""


def check_E18_contain_a_pair_of_parentheses(text):
    return common.count_pair_of_parentheses(text) == 1


def check_E19_contain_more_pair_of_parentheses(text):
    return common.count_pair_of_parentheses(text) >= 1


# Column kana_question

def check_F3_match_column(col1, col2):
    words_col1 = [element.strip() for element in col1.split(
        "\n") if element.strip() != ""]
    words_col2 = [element.strip() for element in col2.split(
        "\n") if element.strip() != ""]
    return len(words_col1) == len(words_col2)
# Column hanviet_question


def check_I11_written_by_capital_vietnamese(text):
    return common.is_vietnamese(text) and text == text.upper()

# Column audio


def check_J3_have_tag_p_or_h(text):
    return bool(re.search(r'<[phPH][^>]*>.*?</[phPH]>', text))


def check_J3_like_column(col1_audio, col2_text_question):
    clean_text = common.get_clean_text(col1_audio)
    return clean_text == col2_text_question

# Column image


def check_K17_has_content(text):
    return bool(text)

# Column answer


def check_L2_has_two_or_four_answers(text):
    answer_arr = text.split("\n")
    answer_arr = [element.strip()
                  for element in answer_arr if element.strip() != ""]
    return len(answer_arr) == 2 or len(answer_arr) == 4


def check_L3_has_max_four_answers(text):
    answer_arr = text.split("\n")
    answer_arr = [element.strip()
                  for element in answer_arr if element.strip() != ""]
    return len(answer_arr) <= 4 and len(set(answer_arr)) == len(answer_arr)


def check_L4_contains_enough_words(col1_answer, col2_correct_ans):
    words_col1 = [element.strip() for element in col1_answer.split(
        "\n") if element.strip() != ""]
    words_col2 = [element.strip() for element in col2_correct_ans.split(
        "\n") if element.strip() != ""]
    return all(element in words_col1 for element in words_col2)


def check_L4_contains_noise_words(col1_answer, col2_correct_ans):
    words_col1 = [element.strip() for element in col1_answer.split(
        "\n") if element.strip() != ""]
    words_col2 = [element.strip() for element in col2_correct_ans.split(
        "\n") if element.strip() != ""]
    return len(words_col1) > len(words_col2) and not (len(set(words_col1)) == len(set(words_col2)))


def check_L4_format_sentence(text):
    return bool(text[len(text) - 1] == ".") or text[0] == text[0].upper()


def check_L4_order_words_diff(col1_answer, col2_correct_ans):
    words_col1 = [element.strip() for element in col1_answer.split(
        "\n") if element.strip() != ""]
    words_col2 = [element.strip() for element in col2_correct_ans.split(
        "\n") if element.strip() != ""]
    return all(words_col2[i] == words_col1[i] for i in range(len(words_col2)))


def check_L9_audio_contains_answers_accept_dots(col1_answer, col2_audio):
    words_col1 = [element.strip() for element in col1_answer.split(
        "\n") if element.strip() != ""]
    return any(str(element.rstrip(".")) == str(col2_audio.rstrip("."))
               for element in words_col1)


def check_L13_audio_contains_answers(col1_answer, col2_audio):
    words_col1 = [element.strip() for element in col1_answer.split(
        "\n") if element.strip() != ""]
    return any(str(element) == str(col2_audio) for element in words_col1)


def check_L17_count_japanese_words(text):
    words = [element.strip()
             for element in text.split("\n") if element.strip() != ""]
    return all(len(element) <= 2 for element in words)


def check_L17_has_punctuation(text):
    words = [element.strip()
             for element in text.split("\n") if element.strip() != ""]
    words_str = "".join(words)
    return all(common.is_japanese(element) for element in words_str)


def check_L19_structure_pair_of_parentheses(text):
    return text.startswith('(') and text.endswith(')')


def check_L21_muitii_line_breaks(text):
    line = [element.strip()
            for element in text.split("\n") if element.strip() != ""]
    return len(line) > 1


# Column Image_answer

# Column corect_answer

def check_S2_type_number(text):
    return common.is_number(text)


def check_S4_pairing_method(text):
    # Pending
    return True


def check_S13_type_number_and_like_number_audio(text):
    # Pending
    another_con = True
    return common.is_number(text) and another_con


def check_S14_correct_answer_like_audio(col1_corect_answer, col2_audio):
    line = [element.strip()
            for element in col1_corect_answer.split("\n") if element.strip() != ""]
    completed_text = "".join(line)
    return completed_text == col2_audio


def check_S19_correct_answer_has_pair_of_parentheses_and_like_answer(col1_corect_answer, col2_answer):
    # Pending
    open_count = col1_corect_answer.count('(')
    close_count = col1_corect_answer.count(')')
    another_con = True
    return open_count > 1 and close_count > 1 and another_con


# Column explain


def check_T2_explain_match_answer_and_correct_answer_type_1(col1_explain, col2_answer, col3_correct_answer):
    condition = r'\{\{(.*?)\}\}'
    return common.check_explain_match_type_1(col1_explain, col2_answer, col3_correct_answer, condition)


def check_T2_explain_match_answer_and_kana_answer_type_1(col1_explain, col2_kana_answer, col3_correct_answer):
    condition = r'\[\[(.*?)\]\]'
    return common.check_explain_match_type_1(
        col1_explain, col2_kana_answer, col3_correct_answer, condition)


def check_T2_explain_match_answer_and_romanji_answer_type_1(col1_explain, col2_romanji_answer, col3_correct_answer):
    condition = r'\(\((.*?)\)\)'
    return common.check_explain_match_type_1(
        col1_explain, col2_romanji_answer, col3_correct_answer, condition)


def check_T2_explain_mean_like_text_question_type_1(col1_explain, col2_text_question):
    check = col2_text_question.split("\"")[1].strip()
    explain_text_question = col1_explain.split("))")
    if (len(explain_text_question) < 2):
        explain_text_question = col1_explain.split("]]")
    if (len(explain_text_question) < 2):
        explain_text_question = col1_explain.split("}}")
    return check == explain_text_question[-1].strip()


def check_T3_explain_mean_like_text_question_type_2(col1_explain, col2_text_question):
    check_tag_p = bool(re.search(r'<[pP][^>]*>.*?</[pP]>', col2_text_question))
    condition = r'\{\{(.*?)\}\}'
    return not check_tag_p and common.check_explain_match_type_2(
        col1_explain, col2_text_question, condition)


def check_T3_explain_mean_like_kana_question_type_2(col1_explain, col2_kana_question):
    check_tag_p = bool(re.search(r'<[pP][^>]*>.*?</[pP]>', col2_kana_question))
    condition = r'\[\[(.*?)\]\]'
    return not check_tag_p and common.check_explain_match_type_2(
        col1_explain, col2_kana_question, condition)


def check_T3_explain_mean_like_romanji_question_type_2(col1_explain, col2_romanji_question):
    check_tag_p = bool(
        re.search(r'<[pP][^>]*>.*?</[pP]>', col2_romanji_question))
    condition = r'\(\((.*?)\)\)'
    return not check_tag_p and common.check_explain_match_type_2(
        col1_explain, col2_romanji_question, condition)


def check_T3_explain_mean_match_correct_answer_type_2(col1_explain, col2_answer, col3_correct_answer):
    explain_answer = col1_explain.split("))")
    if (len(explain_answer) < 2):
        explain_answer = col1_explain.split("]]")
    if (len(explain_answer) < 2):
        explain_answer = col1_explain.split("}}")
    answers = [element.strip()
               for element in col2_answer.split("\n") if element.strip() != ""]
    return explain_answer[-1].strip() == answers[int(col3_correct_answer) - 1].strip()


def check_T4_explain_mean_match_correct_answer_type_3(col1_explain, col2_correct_answer):
    explain_answer = col1_explain.split("))")
    if (len(explain_answer) < 2):
        explain_answer = col1_explain.split("]]")
    if (len(explain_answer) < 2):
        explain_answer = col1_explain.split("}}")
    answers = [element.strip()
               for element in col2_correct_answer.split("\n") if element.strip() != ""]
    return explain_answer[-1].strip().rstrip(".").upper() == " ".join(answers).strip().rstrip(".").upper()


def check_T4_count_explain(col1_explain, col2_answer):
    # Pending ???
    return True


def check_T8_form_kana(col1_explain, col2_correct_answer):
    # Pending ???
    return True


def check_T8_form_romanji(col1_explain, col2_correct_answer):
    # Pending ???
    return True


def check_T9_explain_like_audio(col1_explain, audio):
    explain_jp = re.findall(r'\{\{(.*?)\}\}', col1_explain)
    if not audio and not explain_jp:
        return True
    if not explain_jp or not audio:
        return False
    return explain_jp[0].strip() == audio.strip()


def check_T15_form_kana_of_audio(col1_explain, audio):
    # Pending ???
    return True


def check_T15_form_romanji_of_audio(col1_explain, audio):
    # Pending ???
    return True


def check_T17_expression_kanji_of_correct_answer(col1_explain, col2_correct_answer):
    # Pending ???
    return True


def check_T17_complete_sentences_answer_combining_correct_answer(col1_explain, col2_correct_answer):
    # Pending ???
    return True


def check_T17_complete_sentences_answer_combining_kana_answer(col1_explain, col2_correct_answer):
    # Pending ???
    return True


def check_T17_complete_sentences_answer_combining_romanji_answer(col1_explain, col2_correct_answer):
    # Pending ???
    return True


def check_T18_complete_sentences_text_combining_correct_answer(col1_explain, col2_correct_answer):
    # Pending ???
    return True


def check_T18_complete_sentences_text_combining_kana_answer(col1_explain, col2_correct_answer):
    # Pending ???
    return True


def check_T18_complete_sentences_text_combining_romanji_answer(col1_explain, col2_correct_answer):
    # Pending ???
    return True


def check_T19_complete_sentences_drop_text_combining_correct_answer(col1_explain, col2_correct_answer):
    # Pending ???
    return True


def check_T19_complete_sentences_drop_text_combining_kana_answer(col1_explain, col2_correct_answer):
    # Pending ???
    return True


def check_T19_complete_sentences_drop_text_combining_romanji_answer(col1_explain, col2_correct_answer):
    # Pending ???
    return True

# Column explain_grammar


def check_V3_explain_grammar(col1_explain_grammar, col2_text_question):
    check_tag_p = bool(re.search(r'<[pP][^>]*>.*?</[pP]>', col2_text_question))
    if check_tag_p and not col1_explain_grammar:
        return False
    condition_explain_number = True
    return condition_explain_number
