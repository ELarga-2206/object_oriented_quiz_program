import random
from constants import *

class QuizModel:
    def __init__(self, filename="quiz_questions.txt"):
        self.filename = filename # initialize as none
        self.questions = []
        self.current_question = 0
        self.score = 0
        self.load_questions()
        self.shuffle_questions()
        
    def load_questions(self): # for question data conversion to text
        with open(self.filename, "r") as file:
            content = file.read().strip() 

        blocks = content.split("----------------------------------------")
        
        for block in blocks:
            lines = block.strip().split("\n") 
            if len(lines) < 6: 
                continue

            try:
                question_text = lines[0].replace("Question:", "").strip() 
                options = [
                    lines[1].replace("A:", "").strip(),
                    lines[2].replace("B:", "").strip(),
                    lines[3].replace("C:", "").strip(),
                    lines[4].replace("D:", "").strip()
                ]
                correct = lines[5].replace("Correct Answer:", "").strip().upper() 

                self.questions.append({
                    "question": question_text,
                    "options": options,
                    "answer": correct 
                })
            except Exception as e:
                print(f"Error processing block:\n{block}\nError: {e}")
                continue
    
    def shuffle_questions(self):  # for random questions
        random.shuffle(self.questions)
        
    def get_current_question(self):  # Retrieve a specific question
        if self.current_question < len(self.questions):
            return self.questions[self.current_question]
        return None
        
    def check_answer(self, selected_option): # get current question
        current = self.get_current_question()
        if not current:
            return False, None
            
        is_correct = (chr(65 + selected_option) == current["answer"]  # score logic
        if is_correct:
            self.score += 1
            
        return is_correct, current["answer"]
    
    def next_question(self):
        self.current_question += 1
        return self.current_question < len(self.questions)
    
    def get_score(self): # Display the user's current performance
        return self.score, len(self.questions)