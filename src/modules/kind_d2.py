from src.helpers import helper
from src.helpers import common


class Kind_D2_Service:
    # In this logic, each function will return array of number.
    # Example [1] or [1,2,3]
    # The goal is to eventually be able to match errors with file rule japan_rule.json
    def __init__(self, obj):
        self.obj = obj

    def E2(self, text_question):
        arr_error = []
        if not helper.check_E2_structure_where(text_question):
            arr_error.append(1)
        if not helper.check_E2_has_tag_p_same(text_question):
            arr_error.append(90)
        if not helper.check_format_tag_p(text_question):
            arr_error.append(109)
        return arr_error

    def L2(self, answer):
        arr_error = []
        if not helper.check_L2_has_two_or_four_answers(answer):
            arr_error.append(13)
        if not helper.check_E3_written_by_japanese(answer):
            arr_error.append(
                71)
        return arr_error

    def M2(self, kana_answer, answer):
        arr_error = []
        if not helper.check_F3_match_column(kana_answer, answer):
            arr_error.append(26)
        return arr_error

    def N2(self, romanji_answer, kana_answer):
        arr_error = []
        if not helper.check_F3_match_column(romanji_answer, kana_answer):
            arr_error.append(28)
        return arr_error

    def S2(self, correct_answer):
        arr_error = []
        if not helper.check_S2_type_number(correct_answer):
            arr_error.append(30)
        return arr_error

    def T2(self, explain, answer, correct_answer, kana_answer, romanji_answer, text_question):
        arr_error = []
        if not helper.check_T2_explain_match_answer_and_correct_answer_type_1(explain, answer, correct_answer):
            arr_error.append(
                34)
        if not helper.check_T2_explain_match_answer_and_kana_answer_type_1(explain, kana_answer, correct_answer):
            arr_error.append(
                35)
        if not helper.check_T2_explain_match_answer_and_romanji_answer_type_1(explain, romanji_answer, correct_answer):
            arr_error.append(36)
        if not helper.check_T2_explain_mean_like_text_question_type_1(explain, text_question):
            arr_error.append(
                37)
        arr_error.append(helper.check_T2_brackets(explain))
        return arr_error

    def run(self):
        kind_data = self.obj
        arr_error = [
            self.E2(kind_data["text_question"]),
            self.L2(kind_data["answer"]),
            self.M2(kind_data["kana_answer"], kind_data["answer"]),
            self.N2(kind_data["romanji_answer"], kind_data["kana_answer"]),
            self.S2(kind_data["correct_answer"]),
            self.T2(kind_data["explain"], kind_data["answer"], kind_data["correct_answer"],
                    kind_data["kana_answer"], kind_data["romanji_answer"], kind_data["text_question"])
        ]
        return common.flatten_recursive(arr_error)
