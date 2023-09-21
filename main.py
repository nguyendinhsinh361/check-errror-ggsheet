from src.helpers import helper


def main():
    helper.check_explain_like_audio(
        """{{私}}[[わたし]]((watashi)) tôi""", """私""")


if __name__ == "__main__":
    main()
