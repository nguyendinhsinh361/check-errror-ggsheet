from src.helpers import helper
from src.helpers import common


class Kind_D15_Service:
    # In this logic, each function will return array of number.
    # Example [1] or [1,2,3]
    # The goal is to eventually be able to match errors with file rule japan_rule.json
    def __init__(self, obj):
        self.obj = obj

    def J15(self, audio_question):
        arr_error = []
        if not helper.check_E3_written_by_japanese(audio_question):
            arr_error.append(69)
        if not helper.check_J3_have_tag_p_or_h(audio_question):
            arr_error.append(11)
        return arr_error

    def L15(self, answer):
        arr_error = []
        if not helper.check_E3_written_by_japanese(answer):
            arr_error.append(73)
        if not helper.check_L3_has_max_four_answers(answer):
            arr_error.append(14)
        return arr_error

    def S15(self, corect_answer):
        arr_error = []
        if not helper.check_S2_type_number(corect_answer):
            arr_error.append(30)

        return arr_error

    def T15(self, explain, audio_question, answer, correct_answer, kana_answer, romanji_answer):
        arr_error = []
        if not helper.check_T9_explain_like_audio_question(explain, audio_question):
            arr_error.append(46)
        if not helper.check_T15_form_kana_of_audio_question(explain, audio_question):
            arr_error.append(51)
        if not helper.check_T15_form_romanji_of_audio_question(explain, audio_question):
            arr_error.append(52)
        if not helper.check_T3_explain_mean_match_correct_answer_type_2(explain, answer, correct_answer):
            arr_error.append(40)
        return arr_error

    def run(self):
        kind_data = self.obj
        arr_error = [
            self.J15(kind_data["audio_question"]),
            self.L15(kind_data["answer"]),
            self.S15(kind_data["corect_answer"]),
            self.T15(kind_data["explain"], kind_data["audio_question"], kind_data["answer"],
                     kind_data["corect_answer"], kind_data["kana_answer"], kind_data["romanji_answer"]),
        ]
        return common.flatten_recursive(arr_error)
