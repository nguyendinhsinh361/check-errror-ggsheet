from src.helpers import helper
from src.helpers import common


class Kind_D19_Service:
    # In this logic, each function will return array of number.
    # Example [1] or [1,2,3]
    # The goal is to eventually be able to match errors with file rule japan_rule.json
    def __init__(self, obj):
        self.obj = obj

    def E19(self, text_question):
        arr_error = []
        if not helper.check_E3_written_by_japanese(text_question):
            arr_error.append(2)
        if not helper.check_E19_contain_more_pair_of_parentheses(text_question):
            arr_error.append(8)
        return arr_error

    def F19(self, kana_question, text_question):
        arr_error = []
        if not helper.check_F3_match_column(kana_question, text_question):
            arr_error.append(9)
        return arr_error

    def G19(self, romaji_question, kana_question):
        arr_error = []
        if not helper.check_F3_match_column(romaji_question, kana_question):
            arr_error.append(10)
        return arr_error

    def L19(self, answer):
        arr_error = []
        if not helper.check_L19_structure_pair_of_parentheses(answer):
            arr_error.append(22)
        return arr_error

    def M19(self, kana_answer, answer):
        arr_error = []
        if not helper.check_F3_match_column(kana_answer, answer):
            arr_error.append(26)
        return arr_error

    def N19(self, romanji_answer, kana_answer):
        arr_error = []
        if not helper.check_F3_match_column(romanji_answer, kana_answer):
            arr_error.append(28)
        return arr_error

    def S19(self, corect_answer, answer):
        arr_error = []
        if not helper.check_S19_correct_answer_has_pair_of_parentheses_and_like_answer(corect_answer, answer):
            arr_error.append(85)

        return arr_error

    def T19(self, explain, text_question, answer, correct_answer, kana_answer, romanji_answer):
        arr_error = []
        if not helper.check_T19_complete_sentences_text_combining_correct_answer(explain, correct_answer):
            arr_error.append(60)
        if not helper.check_T19_complete_sentences_text_combining_kana_answer(explain, correct_answer):
            arr_error.append(61)
        if not helper.check_T19_complete_sentences_text_combining_romanji_answer(explain, correct_answer):
            arr_error.append(62)
        if not helper.check_T5_check_mean_vietnamese(explain):
            arr_error.append(76)
        return arr_error

    def V19(self, explain_grammar, text_question):
        arr_error = []
        if not helper.check_V3_explain_grammar(explain_grammar, text_question):
            arr_error.append(66)
        if not helper.check_V3_number_explain_grammar(explain_grammar, text_question):
            arr_error.append(67)

        return arr_error

    def run(self):
        kind_data = self.obj
        arr_error = [
            self.E19(kind_data["text_question"]),
            self.F19(kind_data["kana_question"], kind_data["text_question"]),
            self.G19(kind_data["romaji_question"], kind_data["kana_question"]),
            self.L19(kind_data["answer"]),
            self.M19(kind_data["kana_answer"], kind_data["answer"]),
            self.N19(kind_data["romanji_answer"], kind_data["kana_answer"]),
            self.S19(kind_data["corect_answer"]),
            self.T19(kind_data["explain"], kind_data["text_question"], kind_data["answer"],
                     kind_data["corect_answer"], kind_data["kana_answer"], kind_data["romanji_answer"]),
            self.V19(kind_data["explain_grammar"], kind_data["text_question"]),

        ]
        return common.flatten_recursive(arr_error)
