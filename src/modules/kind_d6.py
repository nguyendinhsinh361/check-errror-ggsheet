from src.helpers import helper
from src.helpers import common


class Kind_D6_Service:
    # In this logic, each function will return array of number.
    # Example [1] or [1,2,3]
    # The goal is to eventually be able to match errors with file rule japan_rule.json
    def __init__(self, obj):
        self.obj = obj

    def E6(self, text_question):
        arr_error = []
        if not helper.check_E3_written_by_japanese(text_question):
            arr_error.append(2)
        return arr_error

    def F6(self, kana_question, text_question):
        arr_error = []
        if not helper.check_F3_match_column(kana_question, text_question):
            arr_error.append(9)
        return arr_error

    def G6(self, romaji_question, kana_question):
        arr_error = []
        if not helper.check_F3_match_column(romaji_question, kana_question):
            arr_error.append(10)
        return arr_error

    def H6(self, mean_question):
        arr_error = []
        if not helper.check_E13_written_by_vietnamese(mean_question):
            arr_error.append(70)
        return arr_error

    def J6(self, audio_question, text_question):
        arr_error = []
        if not helper.check_E3_written_by_japanese(audio_question):
            arr_error.append(69)
        if not helper.check_J3_have_tag_p_or_h(audio_question):
            arr_error.append(11)
        if not helper.check_J3_like_column(audio_question, text_question):
            arr_error.append(12)

        return arr_error

    def L6(self, answer, correct_answer):
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

    def M6(self, kana_answer, answer):
        arr_error = []
        if not helper.check_F3_match_column(kana_answer, answer):
            arr_error.append(26)
        return arr_error

    def N6(self, romanji_answer, kana_answer):
        arr_error = []
        if not helper.check_F3_match_column(romanji_answer, kana_answer):
            arr_error.append(28)
        return arr_error

    def S6(self, corect_answer):
        arr_error = []
        if not helper.check_E13_written_by_vietnamese(corect_answer):
            arr_error.append(74)
        if not helper.check_L21_muitii_line_breaks(corect_answer):
            arr_error.append(75)
        if not helper.check_S4_pairing_method(corect_answer):
            arr_error.append(31)

        return arr_error

    def T6(self, explain, answer, correct_answer, kana_answer, romanji_answer):
        arr_error = []
        if not helper.check_T4_explain_mean_match_correct_answer_type_3(explain, correct_answer):
            arr_error.append(43)
        if not helper.check_T6_form_kana(explain, kana_answer, correct_answer):
            arr_error.append(44)
        if not helper.check_T6_form_romanji(explain, romanji_answer, correct_answer):
            arr_error.append(45)
        if not helper.check_T5_check_mean_vietnamese(explain):
            arr_error.append(76)
        if not helper.check_T4_count_explain(explain, answer):
            arr_error.append(42)

        return arr_error

    def V6(self, explain_grammar, text_question):
        arr_error = []
        if not helper.check_V3_explain_grammar(explain_grammar, text_question):
            arr_error.append(66)
        if not helper.check_V3_number_explain_grammar(explain_grammar, text_question):
            arr_error.append(67)

        return arr_error

    def run(self):
        kind_data = self.obj
        arr_error = [
            self.E6(kind_data["text_question"]),
            self.F6(kind_data["kana_question"], kind_data["text_question"]),
            self.G6(kind_data["romaji_question"], kind_data["kana_question"]),
            self.H6(kind_data["mean_question"]),
            self.J6(kind_data["audio_question"], kind_data["text_question"]),
            self.L6(kind_data["answer"]),
            self.M6(kind_data["kana_answer"], kind_data["answer"]),
            self.N6(kind_data["romanji_answer"], kind_data["kana_answer"]),
            self.S6(kind_data["corect_answer"]),
            self.T6(kind_data["explain"], kind_data["answer"], kind_data["corect_answer"],
                    kind_data["kana_answer"], kind_data["romanji_answer"]),
            self.V6(kind_data["explain_grammar"], kind_data["text_question"]),
        ]
        return common.flatten_recursive(arr_error)
