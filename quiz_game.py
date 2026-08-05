"""퀴즈 게임 전체를 관리하는 모듈."""

import json
import os
import random

from quiz import Quiz

# 데이터 파일은 이 소스 파일이 있는 프로젝트 루트에 둔다.
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATE_FILE = os.path.join(BASE_DIR, "state.json")

# 파일이 없을 때(첫 실행) 사용할 기본 퀴즈 8문항 — 주제: 간식·디저트·카페 메뉴 상식
DEFAULT_QUIZZES = [
    {
        "question": "초콜릿의 원료가 되는 열매는 무엇일까?",
        "choices": ["카카오", "커피", "바닐라", "아몬드"],
        "answer": 1,
    },
    {
        "question": "화이트초콜릿에 들어가지 않는 성분은?",
        "choices": ["설탕", "우유", "카카오버터", "코코아 고형분(카카오매스)"],
        "answer": 4,
    },
    {
        "question": "에스프레소에 뜨거운 물을 섞어 만드는 카페 메뉴는?",
        "choices": ["아메리카노", "카페라떼", "카푸치노", "콜드브루"],
        "answer": 1,
    },
    {
        "question": "카페라떼와 카푸치노의 가장 큰 차이는?",
        "choices": ["원두의 종류", "우유 거품(폼)의 양", "컵의 재질", "물의 온도"],
        "answer": 2,
    },
    {
        "question": "마카롱 반죽에 들어가는 대표적인 가루는?",
        "choices": ["아몬드 가루", "감자 전분", "옥수수 가루", "쌀가루"],
        "answer": 1,
    },
    {
        "question": "티라미수에 들어가는 이탈리아 치즈는?",
        "choices": ["체다", "모차렐라", "마스카르포네", "고르곤졸라"],
        "answer": 3,
    },
    {
        "question": "버블티의 '버블(펄)'을 만드는 주재료는?",
        "choices": ["젤라틴", "타피오카 전분", "찹쌀", "한천"],
        "answer": 2,
    },
    {
        "question": "겨울 간식 붕어빵에 전통적으로 들어가는 속은?",
        "choices": ["팥", "고구마", "크림", "치즈"],
        "answer": 1,
    },
]


class QuizGame:
    """메뉴 출력, 사용자 입력 처리, 게임 진행을 담당하는 클래스."""

    def __init__(self):
        self.quizzes = []      # Quiz 객체를 담을 리스트
        self.best_score = 0    # 최고 점수

    def use_default_data(self):
        """기본 퀴즈 데이터로 초기화한다."""
        self.quizzes = [Quiz.from_dict(item) for item in DEFAULT_QUIZZES]
        self.best_score = 0

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
                self.play_quiz()
            elif choice == 2:
                print("\n[퀴즈 추가] 아직 구현 중입니다.")
            elif choice == 3:
                print("\n[퀴즈 목록] 아직 구현 중입니다.")
            elif choice == 4:
                print("\n[점수 확인] 아직 구현 중입니다.")
            elif choice == 5:
                print("\n프로그램을 종료합니다.")
                break
    # ---------- 기능: 퀴즈 풀기 ----------
    def play_quiz(self):
        """저장된 퀴즈를 출제하고 채점한 뒤 최고 점수를 갱신한다."""
        if not self.quizzes:                      # 퀴즈가 없는 경우 처리
            print("\n⚠️  등록된 퀴즈가 없습니다. 먼저 '2. 퀴즈 추가'로 문제를 등록해 주세요.")
            return

        total = len(self.quizzes)
        count = self.ask_number(f"\n몇 문제를 풀까요? (1~{total}): ", 1, total)
        selected = random.sample(self.quizzes, count)   # 순서를 랜덤하게 섞어서 뽑기

        print(f"\n📝 퀴즈를 시작합니다! (총 {count}문제)")
        correct_count = 0

        for number, quiz in enumerate(selected, start=1):
            quiz.show(number)
            user_answer = self.ask_number("정답 입력 (1-4): ", 1, 4)

            if quiz.is_correct(user_answer):
                print("✅ 정답입니다!")
                correct_count += 1
            else:
                right = quiz.choices[quiz.answer - 1]
                print(f"❌ 오답입니다. 정답은 {quiz.answer}번({right})입니다.")

        score = round(correct_count / count * 100)      # 100점 만점 환산

        print()
        print("=" * 40)
        print(f"🏆 결과: {count}문제 중 {correct_count}문제 정답! ({score}점)")

        if score > self.best_score:
            self.best_score = score
            print("🎉 새로운 최고 점수입니다!")
        else:
            print(f"현재 최고 점수는 {self.best_score}점입니다.")
        print("=" * 40)