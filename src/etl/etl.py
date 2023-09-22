from src.enums.kind import Kind
from src.etl import extract
from src.modules.kind_d2 import Kind_D2_Service
from src.modules.kind_d3 import Kind_D3_Service
from src.modules.kind_d4 import Kind_D4_Service
from src.modules.kind_d5 import Kind_D5_Service
from src.modules.kind_d6 import Kind_D6_Service
from src.modules.kind_d7 import Kind_D7_Service
from src.modules.kind_d8 import Kind_D8_Service
from src.modules.kind_d9 import Kind_D9_Service
from src.modules.kind_d10 import Kind_D10_Service
from src.modules.kind_d11 import Kind_D11_Service
from src.modules.kind_d12 import Kind_D12_Service
from src.modules.kind_d13 import Kind_D13_Service
from src.modules.kind_d14 import Kind_D14_Service
from src.modules.kind_d15 import Kind_D15_Service
from src.modules.kind_d16 import Kind_D16_Service
from src.modules.kind_d17 import Kind_D17_Service
from src.modules.kind_d18 import Kind_D18_Service
from src.modules.kind_d19 import Kind_D19_Service
from src.modules.kind_d20 import Kind_D20_Service
from src.modules.kind_d21 import Kind_D21_Service
from src.modules.kind_d22 import Kind_D22_Service
from src.helpers import common

DATA_BASIC_1 = 'src/data/basic_1.json'
DATA_ERROR_BASIC_1 = 'src/error/basic_1.json'
DATA_ERROR_EXCEL_BASIC_1 = 'src/excel/basic_1.xlsx'
DATA_RULE = 'src/static/japan_rule.json'


def etl_stream():
    kind_data = common.get_raw_data(DATA_BASIC_1)
    result_error = {}
    for data in kind_data:
        if (data["kind"].strip() == (Kind.KIND_2.value).strip()):
            kind_d2 = Kind_D2_Service(data)
            result_error[f'kind: {data["kind"]}, count_question: {data["Count questions "]}, text_question: {data["text_question"]}'] = {
                "kind": data["kind"],
                "count_questions": data["Count questions "],
                "text_question": data["text_question"],
                "error": kind_d2.run()
            }

        elif (data["kind"].strip() == (Kind.KIND_3.value).strip()):
            kind_d3 = Kind_D3_Service(data)
            result_error[f'kind: {data["kind"]}, count_question: {data["Count questions "]}, text_question: {data["text_question"]}'] = {
                "kind": data["kind"],
                "count_questions": data["Count questions "],
                "text_question": data["text_question"],
                "error": kind_d3.run()
            }

        elif (data["kind"].strip() == (Kind.KIND_4.value).strip()):
            kind_d4 = Kind_D4_Service(data)
            result_error[f'kind: {data["kind"]}, count_question: {data["Count questions "]}, text_question: {data["text_question"]}'] = {
                "kind": data["kind"],
                "count_questions": data["Count questions "],
                "text_question": data["text_question"],
                "error": kind_d4.run()
            }

        elif (data["kind"].strip() == (Kind.KIND_5.value).strip()):
            kind_d5 = Kind_D5_Service(data)
            result_error[f'kind: {data["kind"]}, count_question: {data["Count questions "]}, text_question: {data["text_question"]}'] = {
                "kind": data["kind"],
                "count_questions": data["Count questions "],
                "text_question": data["text_question"],
                "error": kind_d5.run()
            }

        elif (data["kind"].strip() == (Kind.KIND_6.value).strip()):
            kind_d6 = Kind_D6_Service(data)
            result_error[f'kind: {data["kind"]}, count_question: {data["Count questions "]}, text_question: {data["text_question"]}'] = {
                "kind": data["kind"],
                "count_questions": data["Count questions "],
                "text_question": data["text_question"],
                "error": kind_d6.run()
            }

        elif (data["kind"].strip() == (Kind.KIND_7.value).strip()):
            kind_d7 = Kind_D7_Service(data)
            result_error[f'kind: {data["kind"]}, count_question: {data["Count questions "]}, text_question: {data["text_question"]}'] = {
                "kind": data["kind"],
                "count_questions": data["Count questions "],
                "text_question": data["text_question"],
                "error": kind_d7.run()
            }

        elif (data["kind"].strip() == (Kind.KIND_8.value).strip()):
            kind_d8 = Kind_D8_Service(data)
            result_error[f'kind: {data["kind"]}, count_question: {data["Count questions "]}, text_question: {data["text_question"]}'] = {
                "kind": data["kind"],
                "count_questions": data["Count questions "],
                "text_question": data["text_question"],
                "error": kind_d8.run()
            }

        elif (data["kind"].strip() == (Kind.KIND_9.value).strip()):
            kind_d9 = Kind_D9_Service(data)
            result_error[f'kind: {data["kind"]}, count_question: {data["Count questions "]}, text_question: {data["text_question"]}'] = {
                "kind": data["kind"],
                "count_questions": data["Count questions "],
                "text_question": data["text_question"],
                "error": kind_d9.run()
            }

        elif (data["kind"].strip() == (Kind.KIND_10.value).strip()):
            kind_d10 = Kind_D10_Service(data)
            result_error[f'kind: {data["kind"]}, count_question: {data["Count questions "]}, text_question: {data["text_question"]}'] = {
                "kind": data["kind"],
                "count_questions": data["Count questions "],
                "text_question": data["text_question"],
                "error": kind_d10.run()
            }

        elif (data["kind"].strip() == (Kind.KIND_11.value).strip()):
            kind_d11 = Kind_D11_Service(data)
            result_error[f'kind: {data["kind"]}, count_question: {data["Count questions "]}, text_question: {data["text_question"]}'] = {
                "kind": data["kind"],
                "count_questions": data["Count questions "],
                "text_question": data["text_question"],
                "error": kind_d11.run()
            }

        elif (data["kind"].strip() == (Kind.KIND_12.value).strip()):
            kind_d12 = Kind_D12_Service(data)
            result_error[f'kind: {data["kind"]}, count_question: {data["Count questions "]}, text_question: {data["text_question"]}'] = {
                "kind": data["kind"],
                "count_questions": data["Count questions "],
                "text_question": data["text_question"],
                "error": kind_d12.run()
            }

        elif (data["kind"].strip() == (Kind.KIND_13.value).strip()):
            kind_d13 = Kind_D13_Service(data)
            result_error[f'kind: {data["kind"]}, count_question: {data["Count questions "]}, text_question: {data["text_question"]}'] = {
                "kind": data["kind"],
                "count_questions": data["Count questions "],
                "text_question": data["text_question"],
                "error": kind_d13.run()
            }

        elif (data["kind"].strip() == (Kind.KIND_14.value).strip()):
            kind_d14 = Kind_D14_Service(data)
            result_error[f'kind: {data["kind"]}, count_question: {data["Count questions "]}, text_question: {data["text_question"]}'] = {
                "kind": data["kind"],
                "count_questions": data["Count questions "],
                "text_question": data["text_question"],
                "error": kind_d14.run()
            }

        elif (data["kind"].strip() == (Kind.KIND_15.value).strip()):
            kind_d15 = Kind_D15_Service(data)
            result_error[f'kind: {data["kind"]}, count_question: {data["Count questions "]}, text_question: {data["text_question"]}'] = {
                "kind": data["kind"],
                "count_questions": data["Count questions "],
                "text_question": data["text_question"],
                "error": kind_d15.run()
            }

        elif (data["kind"].strip() == (Kind.KIND_16.value).strip()):
            kind_d16 = Kind_D16_Service(data)
            result_error[f'kind: {data["kind"]}, count_question: {data["Count questions "]}, text_question: {data["text_question"]}'] = {
                "kind": data["kind"],
                "count_questions": data["Count questions "],
                "text_question": data["text_question"],
                "error": kind_d16.run()
            }

        elif (data["kind"].strip() == (Kind.KIND_17.value).strip()):
            kind_d17 = Kind_D17_Service(data)
            result_error[f'kind: {data["kind"]}, count_question: {data["Count questions "]}, text_question: {data["text_question"]}'] = {
                "kind": data["kind"],
                "count_questions": data["Count questions "],
                "text_question": data["text_question"],
                "error": kind_d17.run()
            }

        elif (data["kind"].strip() == (Kind.KIND_18.value).strip()):
            kind_d18 = Kind_D18_Service(data)
            result_error[f'kind: {data["kind"]}, count_question: {data["Count questions "]}, text_question: {data["text_question"]}'] = {
                "kind": data["kind"],
                "count_questions": data["Count questions "],
                "text_question": data["text_question"],
                "error": kind_d18.run()
            }

        elif (data["kind"].strip() == (Kind.KIND_19.value).strip()):
            kind_d19 = Kind_D19_Service(data)
            result_error[f'kind: {data["kind"]}, count_question: {data["Count questions "]}, text_question: {data["text_question"]}'] = {
                "kind": data["kind"],
                "count_questions": data["Count questions "],
                "text_question": data["text_question"],
                "error": kind_d19.run()
            }

        elif (data["kind"].strip() == (Kind.KIND_20.value).strip()):
            kind_d20 = Kind_D20_Service(data)
            result_error[f'kind: {data["kind"]}, count_question: {data["Count questions "]}, text_question: {data["text_question"]}'] = {
                "kind": data["kind"],
                "count_questions": data["Count questions "],
                "text_question": data["text_question"],
                "error": kind_d20.run()
            }

        elif (data["kind"].strip() == (Kind.KIND_21.value).strip()):
            kind_d21 = Kind_D21_Service(data)
            result_error[f'kind: {data["kind"]}, count_question: {data["Count questions "]}, text_question: {data["text_question"]}'] = {
                "kind": data["kind"],
                "count_questions": data["Count questions "],
                "text_question": data["text_question"],
                "error": kind_d21.run()
            }

        elif (data["kind"].strip() == (Kind.KIND_22.value).strip()):
            kind_d22 = Kind_D22_Service(data)
            result_error[f'kind: {data["kind"]}, count_question: {data["Count questions "]}, text_question: {data["text_question"]}'] = {
                "kind": data["kind"],
                "count_questions": data["Count questions "],
                "text_question": data["text_question"],
                "error": kind_d22.run()
            }

    result_completed_raw = []
    result_completed = []
    for value in result_error.values():
        result_completed_raw.append(value)
    rule_data = common.get_raw_data(DATA_RULE)

    for tmp in result_completed_raw:
        error_values = tmp.get("error", [])
        column = ""
        content = ""
        for data in error_values:
            column += rule_data[str(data)]["column"] + "\n"
            content += rule_data[str(data)]["content"] + "\n"
        result_completed.append({"kind": tmp["kind"], "count_questions": tmp["count_questions"],
                                 "text_question": tmp["text_question"], "column": column, "content": content})
    result_completed = common.flatten_recursive(result_completed)
    result_completed = [tmp for tmp in result_completed if tmp["column"]]
    common.save_data_to_json(result_completed, DATA_ERROR_BASIC_1)
    common.convert_json_to_excel(result_completed, DATA_ERROR_EXCEL_BASIC_1)
    # return result_error
    # extract.extract_data()
