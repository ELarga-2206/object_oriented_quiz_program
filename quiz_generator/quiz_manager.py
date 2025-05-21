# class quiz_manager

#with open("quiz_questions.txt", "a", encoding="utf-8") as file:
#                file.write(f"Question: {question}\n")
 #               file.write(f"A: {choices[0]}\n")
  #              file.write(f"B: {choices[1]}\n")
   #             file.write(f"C: {choices[2]}\n")
    #            file.write(f"D: {choices[3]}\n")
     #           file.write(f"Correct Answer: {correct_answer}\n")
      #          file.write("-" * 40 + "\n")
       #     print("Question saved successfully!")

class QuizManager:
    def __init__(self, filename="quiz_questions.txt"):
        self.filename = filename
    
    def save_question(self, question):
        # what now lol