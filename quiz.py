"""개별 퀴즈 한 문제를 표현하는 모듈."""


class Quiz:
    """문제 1개(문제 내용, 선택지 4개, 정답 번호)를 담는 클래스."""

    def __init__(self, question, choices, answer):
        self.question = question    # str: 문제 내용
        self.choices = choices      # list: 선택지 4개
        self.answer = answer        # int: 정답 번호(1~4)

    def show(self, number):
        """문제 번호와 함께 문제와 선택지를 출력한다."""
        print(f"\n[문제 {number}] {self.question}")
        for index, choice in enumerate(self.choices, start=1):
            print(f"   {index}. {choice}")

    def is_correct(self, user_answer):
        """사용자가 입력한 번호가 정답이면 True를 돌려준다."""
        return user_answer == self.answer

    def to_dict(self):
        """JSON 파일에 저장하기 위해 dict 형태로 바꾼다."""
        return {
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer,
        }

    @classmethod
    def from_dict(cls, data):
        """JSON에서 읽어온 dict를 Quiz 객체로 되돌린다."""
        return cls(data["question"], data["choices"], data["answer"])