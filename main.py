
from src.etl import etl
from src.helpers import helper
from src.helpers import common
import re


def main():
    etl.etl_stream()
    # helper.check_T18_complete_sentences_answer_combining_romanji_answer("{{まさか! 彼女は満点で試験に合格しました。}}[[まさか! かのじょはまんてんでしけんにごうかくしました。]]((Masaka! Kanojo wa manten de shiken ni goukaku shimashita.)) Không thể tin được! Cô ấy đã đỗ kỳ thi với điểm tuyệt đối.", "1", "")


if __name__ == "__main__":
    main()
