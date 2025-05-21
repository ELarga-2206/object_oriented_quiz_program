from question import Question
from quiz_manager import QuizManager
from user_input import UserInterface

class QuizMaker:
    def __init__(self):
        self.ui = UserInterface()
        self.manager = QuizManager()