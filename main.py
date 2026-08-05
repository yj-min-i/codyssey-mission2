"""프로그램 시작점(entry point)."""

from quiz_game import QuizGame


def main():
    """게임 객체를 만들고 실행한다."""
    game = QuizGame()
    game.use_default_data()      # ← 임시로 기본 데이터 사용 (단계 7에서 load()로 교체)

    try:
        game.run()
    except (KeyboardInterrupt, EOFError):
        # Ctrl+C 또는 입력 스트림 종료 시에도 비정상 종료처럼 보이지 않게 처리
        print("\n\n⚠️  입력이 중단되었습니다. 안전하게 종료합니다.")

    print("👋 이용해 주셔서 감사합니다.")


if __name__ == "__main__":
    main()