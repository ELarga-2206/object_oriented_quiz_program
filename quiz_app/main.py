import tkinter as tk
from quiz_controller import QuizController

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizController(root)
    root.mainloop()