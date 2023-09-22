from src.helpers import helper
from src.helpers import common


class Kind_D10_Service:
    # In this logic, each function will return array of number.
    # Example [1] or [1,2,3]
    # The goal is to eventually be able to match errors with file rule japan_rule.json
    def __init__(self, obj):
        self.obj = obj

    def J10(self, audio_question):
        arr_error = []
        if not helper.check_E3_written_by_japanese(audio_question):
            arr_error.append(69)
        if not helper.check_J3_have_tag_p_or_h(audio_question):
            arr_error.append(11)
        return arr_error

    def L10(self, answer, correct_answer):
        arr_error = []
        if not helper.check_E3_written_by_japanese(answer):
            arr_error.append(73)
        if not helper.check_L4_contains_enough_words(answer, correct_answer):
            arr_error.append(15)
        if not helper.check_L4_contains_noise_words(answer, correct_answer):
            arr_error.append(16)
        if not helper.check_L4_format_sentence(answer):
            arr_error.append(20)
        if not helper.check_L4_order_words_diff(answer, correct_answer):
            arr_error.append(20)
        return arr_error

    def M10(self, kana_answer, answer):
        arr_error = []
        if not helper.check_F3_match_column(kana_answer, answer):
            arr_error.append(26)
        return arr_error

    def N10(self, romanji_answer, kana_answer):
        arr_error = []
        if not helper.check_F3_match_column(romanji_answer, kana_answer):
            arr_error.append(28)
        return arr_error

    def S10(self, correct_answer, audio_question):
        arr_error = []
        if not helper.check_E3_written_by_japanese(correct_answer):
            arr_error.append(72)
        if not helper.check_L21_muitii_line_breaks(correct_answer):
            arr_error.append(75)
        if not helper.check_S10_like_audo_question(correct_answer, audio_question):
            arr_error.append(33)
        return arr_error

    def T10(self, explain, audio_question, correct_answer, kana_answer, romanji_answer):
        arr_error = []
        if not helper.check_T9_explain_like_audio_question(explain, audio_question):
            arr_error.append(46)
        if not helper.check_T10_form_kana_match_correct_answer(explain, correct_answer):
            arr_error.append(44)
        if not helper.check_T10_form_romanji_match_kana_answer(explain, kana_answer):
            arr_error.append(45)
        if not helper.check_T5_check_mean_vietnamese(explain):
            arr_error.append(76)

        return arr_error

    def run(self):
        kind_data = self.obj
        arr_error = [
            self.J10(kind_data["audio_question"]),
            self.L10(kind_data["answer"], kind_data["corect_answer"]),
            self.M10(kind_data["kana_answer"], kind_data["answer"]),
            self.N10(kind_data["romanji_answer"], kind_data["kana_answer"]),
            self.S10(kind_data["corect_answer"], kind_data["audio_question"]),
            self.T10(kind_data["explain"], kind_data["audio_question"],
                     kind_data["corect_answer"], kind_data["kana_answer"], kind_data["romanji_answer"]),
        ]
        return common.flatten_recursive(arr_error)
