# for class user_input

class UserInterface:
    @staticmethod
    def get_question_text():
        return input("Enter your question (type 'a' to stop): ")
    
    # for the choices 

    @staticmethod
    def get_choices():
        """Get and validate correct answer from user"""
        while True:
            answer = input("Enter the correct answer (A/B/C/D): ").upper().strip()
            if answer in ['A', 'B', 'C', 'D']:
                return answer
            print("Invalid! Please enter A, B, C, or D only.")
    
    @staticmethod
    def ask_to_continue():   # function for another question
        while True:
            cont = input("\nAdd another question? (Y/N): ").upper().strip()
            if cont in ['Y', 'N']:
                return cont == 'Y'
            print("Please enter Y or N.")

    @staticmethod
    def show_message(message):
        print(message)
    
