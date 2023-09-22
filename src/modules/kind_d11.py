from src.helpers import helper
from src.helpers import common


class Kind_D11_Service:
    # In this logic, each function will return array of number.
    # Example [1] or [1,2,3]
    # The goal is to eventually be able to match errors with file rule japan_rule.json
    def __init__(self, obj):
        self.obj = obj

    def E11(self, text_question):
        arr_error = []
        if not helper.check_E3_written_by_japanese(text_question):
            arr_error.append(2)
        return arr_error

    def F11(self, kana_question, text_question):
        arr_error = []
        if not helper.check_F3_match_column(kana_question, text_question):
            arr_error.append(9)
        return arr_error

    def G11(self, romaji_question, kana_question):
        arr_error = []
        if not helper.check_F3_match_column(romaji_question, kana_question):
            arr_error.append(10)
        return arr_error

    def H11(self, mean_question):
        arr_error = []
        if not helper.check_E13_written_by_vietnamese(mean_question):
            arr_error.append(70)
        return arr_error

    def I11(self, hanviet_question):
        arr_error = []
        if not helper.check_I11_written_by_capital_vietnamese(hanviet_question):
            arr_error.append(77)
        return arr_error

    def J11(self, audio_question, text_question):
        arr_error = []
        if not helper.check_E3_written_by_japanese(audio_question):
            arr_error.append(69)
        if not helper.check_J3_have_tag_p_or_h(audio_question):
            arr_error.append(11)
        if not helper.check_J3_like_column(audio_question, text_question):
            arr_error.append(12)

        return arr_error

    def run(self):
        kind_data = self.obj
        arr_error = [
            self.E11(kind_data["text_question"]),
            self.F11(kind_data["kana_question"], kind_data["text_question"]),
            self.G11(kind_data["romaji_question"], kind_data["kana_question"]),
            self.H11(kind_data["mean_question"]),
            self.H11(kind_data["mean_question"]),
            self.I11(kind_data["hanviet_question"]),
            self.J11(kind_data["audio_question"], kind_data["text_question"]),
        ]
        return common.flatten_recursive(arr_error)
