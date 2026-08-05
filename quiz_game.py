"""퀴즈 게임 전체를 관리하는 모듈."""


class QuizGame:
    """메뉴 출력, 사용자 입력 처리, 게임 진행을 담당하는 클래스."""

    def __init__(self):
        self.quizzes = []      # Quiz 객체를 담을 리스트
        self.best_score = 0    # 최고 점수

    # ---------- 입력 처리 ----------
    def ask_number(self, prompt, min_value, max_value):
        """min_value~max_value 사이의 정수를 받을 때까지 반복해서 물어본다."""
        while True:
            raw = input(prompt).strip()   # 앞뒤 공백 제거

            if raw == "":                 # 빈 입력(그냥 Enter)
                print("⚠️  아무것도 입력하지 않았습니다. 다시 입력해 주세요.")
                continue

            try:
                value = int(raw)          # 숫자 변환 시도
            except ValueError:            # abc 처럼 숫자가 아닐 때
                print("⚠️  숫자만 입력할 수 있습니다. 다시 입력해 주세요.")
                continue

            if value < min_value or value > max_value:   # 허용 범위 밖
                print(f"⚠️  {min_value}~{max_value} 사이의 숫자를 입력하세요.")
                continue

            return value                  # 모두 통과하면 값을 돌려준다

    def ask_text(self, prompt):
        """빈 문자열이 아닌 글자를 받을 때까지 반복해서 물어본다."""
        while True:
            text = input(prompt).strip()
            if text == "":
                print("⚠️  빈 내용은 입력할 수 없습니다. 다시 입력해 주세요.")
                continue
            return text

    # ---------- 화면 출력 ----------
    def show_menu(self):
        """메인 메뉴를 출력한다."""
        print()
        print("=" * 40)
        print("        🎯  나만의 퀴즈 게임  🎯")
        print("=" * 40)
        print("  1. 퀴즈 풀기")
        print("  2. 퀴즈 추가")
        print("  3. 퀴즈 목록")
        print("  4. 점수 확인")
        print("  5. 종료")
        print("=" * 40)

    # ---------- 메인 루프 ----------
    def run(self):
        """메뉴를 반복 출력하며 사용자가 고른 기능을 실행한다."""
        while True:
            self.show_menu()
            choice = self.ask_number("선택: ", 1, 5)

            if choice == 1:
                print("\n[퀴즈 풀기] 아직 구현 중입니다.")
            elif choice == 2:
                print("\n[퀴즈 추가] 아직 구현 중입니다.")
            elif choice == 3:
                print("\n[퀴즈 목록] 아직 구현 중입니다.")
            elif choice == 4:
                print("\n[점수 확인] 아직 구현 중입니다.")
            elif choice == 5:
                print("\n프로그램을 종료합니다.")
                break