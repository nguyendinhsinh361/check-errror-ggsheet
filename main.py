
from src.etl import etl
from src.helpers import helper
from src.helpers import common
import re


def main():
    etl.etl_stream()
    # helper.check_L4_contains_enough_words("{{サラリーマンがマラソン大会によく参加しています。}}[[サラリーマンがマラソンたいかいによくさんかしています。]]((Sarariiman ga marason taikai ni yoku sankashite imasu.)) Nhân viên văn phòng thì thường xuyên tham gia các đại hội marathon.", "()()(に)()", "Sarariiman () ga <p>marason</p> () <p>taikai</p> () yoku sanka()shite imasu." ,"(ni)")


if __name__ == "__main__":
    main()
