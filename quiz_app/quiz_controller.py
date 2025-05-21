# for quiz_controller

import time
import winsound
from quiz_model import QuizModel
from quiz_view import QuizView
from constants import *

class QuizController:
    def __init__(self, root):
        self.model = QuizModel()
        self.view = QuizView(root)
        self.start_time = time.time()
        
        self.setup_handlers()
        self.update_timer()
        self.display_current_question()