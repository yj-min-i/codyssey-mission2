"""프로그램 시작점(entry point)."""

from quiz_game import QuizGame


def main():
    """게임 객체를 만들고, 저장된 데이터를 불러온 뒤 실행한다."""
    game = QuizGame()
    game.load()

    try:
        game.run()
    except (KeyboardInterrupt, EOFError):
        # Ctrl+C(KeyboardInterrupt) 또는 입력 종료(EOFError)에도 비정상 종료하지 않는다
        print("\n\n⚠️  입력이 중단되었습니다. 저장 후 안전하게 종료합니다.")
        game.save()

    print("👋 이용해 주셔서 감사합니다.")


if __name__ == "__main__":
    main()