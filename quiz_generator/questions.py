class Question:
    def __init__(self, text, choices, correct_answer):
        self.text = text
        self.choices = choices  
        self.correct_answer = correct_answer  
    
    def to_file_format(self):  # need to convert questions into strings
        lines = [
            f"Question: {self.text}",
            f"A: {self.choices['A']}",
            f"B: {self.choices['B']}",
            f"C: {self.choices['C']}",
            f"D: {self.choices['D']}",
            f"Correct Answer: {self.correct_answer}",
            "-" * 40
        ]
        return "\n".join(lines) + "\n"