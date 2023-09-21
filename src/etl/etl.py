from src.etl import extract
from src.modules.kind_d2 import Kind_D2_Service
from src.helpers import common

DATA_BASIC_1 = 'src/data/basic_1.json'


def etl_stream():
    kind_data = common.get_raw_data(DATA_BASIC_1)
    kind_d2 = Kind_D2_Service(kind_data[0])
    print(1111, kind_d2.run())
    # extract.extract_data()
