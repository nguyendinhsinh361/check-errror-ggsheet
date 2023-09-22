from src.helpers import helper
from src.helpers import common


class Kind_D18_Service:
    # In this logic, each function will return array of number.
    # Example [1] or [1,2,3]
    # The goal is to eventually be able to match errors with file rule japan_rule.json
    def __init__(self, obj):
        self.obj = obj

    def E18(self, text_question):
        arr_error = []
        if not helper.check_E3_written_by_japanese(text_question):
            arr_error.append(2)
        if not helper.check_E18_contain_a_pair_of_parentheses(text_question):
            arr_error.append(7)
        return arr_error

    def F18(self, kana_question, text_question):
        arr_error = []
        if not helper.check_F3_match_column(kana_question, text_question):
            arr_error.append(9)
        return arr_error

    def G18(self, romaji_question, kana_question):
        arr_error = []
        if not helper.check_F3_match_column(romaji_question, kana_question):
            arr_error.append(10)
        return arr_error

    def L18(self, answer):
        arr_error = []
        if not helper.check_E3_written_by_japanese(answer):
            arr_error.append(73)
        if not helper.check_L3_has_max_four_answers(answer):
            arr_error.append(14)
        return arr_error

    def M18(self, kana_answer, answer):
        arr_error = []
        if not helper.check_F3_match_column(kana_answer, answer):
            arr_error.append(26)
        return arr_error

    def N18(self, romanji_answer, kana_answer):
        arr_error = []
        if not helper.check_F3_match_column(romanji_answer, kana_answer):
            arr_error.append(28)
        return arr_error

    def S18(self, corect_answer):
        arr_error = []
        if not helper.check_S2_type_number(corect_answer):
            arr_error.append(30)

        return arr_error

    def T18(self, explain, text_question, answer, correct_answer, kana_answer, romanji_answer):
        arr_error = []
        if not helper.check_T18_complete_sentences_answer_combining_correct_answer(explain, correct_answer):
            arr_error.append(57)
        if not helper.check_T18_complete_sentences_answer_combining_kana_answer(explain, correct_answer):
            arr_error.append(58)
        if not helper.check_T18_complete_sentences_answer_combining_romanji_answer(explain, correct_answer):
            arr_error.append(59)
        if not helper.check_T5_check_mean_vietnamese(explain):
            arr_error.append(76)
        return arr_error

    def V18(self, explain_grammar, text_question):
        arr_error = []
        if not helper.check_V3_explain_grammar(explain_grammar, text_question):
            arr_error.append(66)
        if not helper.check_V3_number_explain_grammar(explain_grammar, text_question):
            arr_error.append(67)

        return arr_error

    def run(self):
        kind_data = self.obj
        arr_error = [
            self.E18(kind_data["text_question"]),
            self.F18(kind_data["kana_question"], kind_data["text_question"]),
            self.G18(kind_data["romaji_question"], kind_data["kana_question"]),
            self.L18(kind_data["answer"]),
            self.M18(kind_data["kana_answer"], kind_data["answer"]),
            self.N18(kind_data["romanji_answer"], kind_data["kana_answer"]),
            self.S18(kind_data["corect_answer"]),
            self.T18(kind_data["explain"], kind_data["text_question"], kind_data["answer"],
                     kind_data["corect_answer"], kind_data["kana_answer"], kind_data["romanji_answer"]),
            self.V18(kind_data["explain_grammar"], kind_data["text_question"]),

        ]
        return common.flatten_recursive(arr_error)
