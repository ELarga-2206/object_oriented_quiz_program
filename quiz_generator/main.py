from questions import Question
from quiz_manager import QuizManager
from user_input import UserInterface

class QuizMaker:
    def __init__(self):
        self.ui = UserInterface()
        self.manager = QuizManager()

def run(self):
        while True:
            question_text = self.ui.get_question_text()
            
            if question_text.lower() == 'a':
                self.ui.show_message("\nQuiz creation complete. Questions saved to 'quiz_questions.txt'")
                break
            
            try:
                choices = self.ui.get_choices()   # for question details
                correct_answer = self.ui.get_correct_answer()
                
                # save question
                question = Question(question_text, choices, correct_answer)
                self.manager.save_question(question)
                self.ui.show_message("Question saved successfully!")
                
                if not self.ui.ask_to_continue():  # check if want to continue
                    self.ui.show_message("\nQuiz creation complete. Questions saved to 'quiz_questions.txt'")
                    break
            
            except Exception as e:
                self.ui.show_message(f"\nAn error occurred: {e}\nPlease try again.")

if __name__ == "__main__":
    app = QuizMaker()
    app.run()