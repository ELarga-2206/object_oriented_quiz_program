

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

    def setup_handlers(self):
        for i, button in enumerate(self.view.option_buttons):
            button.config(command=lambda i=i: self.check_answer(i))
        self.view.next_button.config(command=self.next_question)
    
    def update_timer(self):
        elapsed_time = time.time() - self.start_time
        minutes = int(elapsed_time // 60)
        seconds = int(elapsed_time % 60)
        self.view.update_timer(minutes, seconds)
        self.view.root.after(1000, self.update_timer)
    
    def display_current_question(self):
        question = self.model.get_current_question()
        if question:
            self.view.display_question(
                self.model.current_question + 1,
                question["question"],
                question["options"]
            )
        else:
            self.end_quiz()
    
    def check_answer(self, selected_index):
        is_correct, correct_answer = self.model.check_answer(selected_index)
        current_question = self.model.get_current_question()
        
        if is_correct:
            winsound.PlaySound(CORRECT_SOUND, winsound.SND_FILENAME)
        else:
            correct_index = ord(correct_answer) - 65
            correct_text = current_question["options"][correct_index]
            winsound.PlaySound(WRONG_SOUND, winsound.SND_FILENAME)
        
        self.view.set_feedback(is_correct, correct_answer, correct_text)
        self.view.disable_options()
    
    def next_question(self):
        if self.model.next_question():
            self.view.enable_options()
            self.display_current_question()
        else:
            self.end_quiz()
    
    def end_quiz(self):
        elapsed_time = time.time() - self.start_time
        minutes = int(elapsed_time // 60)
        seconds = int(elapsed_time % 60)
        time_taken = f"{minutes}:{seconds:02d}"
        
        score, total = self.model.get_score()
        self.view.show_results(score, total, time_taken)