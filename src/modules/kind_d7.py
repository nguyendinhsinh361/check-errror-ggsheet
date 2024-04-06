from src.helpers import helper
from src.helpers import common


class Kind_D7_Service:
    # In this logic, each function will return array of number.
    # Example [1] or [1,2,3]
    # The goal is to eventually be able to match errors with file rule japan_rule.json
    def __init__(self, obj):
        self.obj = obj

    def E7(self, text_question):
        arr_error = []
        if not helper.check_E3_written_by_japanese(text_question):
            arr_error.append(2)
        if not helper.check_E2_has_tag_p_same(text_question):
            arr_error.append(90)
        if not helper.check_format_tag_p(text_question):
            arr_error.append(109)
        return arr_error

    def F7(self, kana_question, text_question):
        arr_error = []
        if not helper.check_F3_match_column(kana_question, text_question):
            arr_error.append(9)
        if not helper.check_format_tag_p(kana_question):
            arr_error.append(110)
        return arr_error

    def G7(self, romaji_question, kana_question):
        arr_error = []
        if not helper.check_F3_match_column(romaji_question, kana_question):
            arr_error.append(10)
        if not helper.check_format_tag_p(romaji_question):
            arr_error.append(111)
        return arr_error

    def H7(self, mean_question):
        arr_error = []
        if not helper.check_E13_written_by_vietnamese(mean_question):
            arr_error.append(70)
        return arr_error

    def J7(self, audio, text_question):
        arr_error = []
        if not helper.check_E3_written_by_japanese(audio):
            arr_error.append(69)
        if helper.check_J3_have_tag_p_or_h(audio):
            arr_error.append(11)
        if not helper.check_J3_like_column(audio, text_question):
            arr_error.append(12)

        return arr_error

    def L7(self, answer):
        arr_error = []
        if not helper.check_E3_written_by_japanese(answer):
            arr_error.append(71)
        if not helper.check_L3_has_max_four_answers(answer):
            arr_error.append(14)
        return arr_error

    def M7(self, kana_answer, answer):
        arr_error = []
        if not helper.check_F3_match_column(kana_answer, answer):
            arr_error.append(26)
        return arr_error

    def N7(self, romanji_answer, kana_answer):
        arr_error = []
        if not helper.check_F3_match_column(romanji_answer, kana_answer):
            arr_error.append(28)
        return arr_error

    def S7(self, correct_answer):
        arr_error = []
        if not helper.check_S2_type_number(correct_answer):
            arr_error.append(30)

        return arr_error

    def T7(self, explain, answer, correct_answer, kana_answer, romanji_answer):
        arr_error = []
        if not helper.check_T2_explain_match_answer_and_correct_answer_type_1(explain, answer, correct_answer):
            arr_error.append(34)
        if not helper.check_T2_explain_match_answer_and_kana_answer_type_1(explain, kana_answer, correct_answer):
            arr_error.append(35)
        if not helper.check_T2_explain_match_answer_and_romanji_answer_type_1(explain, romanji_answer, correct_answer):
            arr_error.append(36)
        if not helper.check_T5_check_mean_vietnamese(explain):
            arr_error.append(76)
        arr_error.append(helper.check_T2_brackets(explain))
        return arr_error

    def V7(self, explain_grammar, text_question):
        arr_error = []
        if not helper.check_V3_explain_grammar(explain_grammar, text_question):
            arr_error.append(66)
        if not helper.check_V3_number_explain_grammar(explain_grammar, text_question):
            arr_error.append(67)

        return arr_error

    def run(self):
        kind_data = self.obj
        arr_error = [
            self.E7(kind_data["text_question"]),
            self.F7(kind_data["kana_question"], kind_data["text_question"]),
            self.G7(kind_data["romaji_question"], kind_data["kana_question"]),
            self.H7(kind_data["mean_question"]),
            self.J7(kind_data["audio"], kind_data["text_question"]),
            self.L7(kind_data["answer"]),
            self.M7(kind_data["kana_answer"], kind_data["answer"]),
            self.N7(kind_data["romanji_answer"], kind_data["kana_answer"]),
            self.S7(kind_data["correct_answer"]),
            self.T7(kind_data["explain"], kind_data["answer"], kind_data["correct_answer"],
                    kind_data["kana_answer"], kind_data["romanji_answer"]),
            self.V7(kind_data["explain_grammar"], kind_data["text_question"]),
        ]
        return common.flatten_recursive(arr_error)
