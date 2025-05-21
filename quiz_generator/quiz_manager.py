class QuizManager:
    def __init__(self, filename="quiz_questions.txt"):
        self.filename = filename
    
    def save_question(self, question):
        try:
            with open(self.filename, "a", encoding="utf-8") as file:
                file.write(question.to_file_format())
            return True
        except Exception as e:
            raise Exception(f"Failed to save question: {e}")