# for quiz_view

import tkinter as tk
from tkinter import messagebox
from constants import *

class QuizView:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz App")
        self.root.geometry("500x450")
        self.root.configure(bg=BACKGROUND_COLOR)
        
        self.setup_ui()
        
    def setup_ui(self):
        self.timer_label = tk.Label(
            self.root, text="Time: 0:00", font=("Segoe UI", 12),
            bg=BACKGROUND_COLOR, fg=BUTTON_FG
        )
        self.timer_label.pack(pady=5)
        
        self.question_label = tk.Label(
            self.root, text="", font=QUESTION_FONT, wraplength=450,
            bg=BACKGROUND_COLOR, fg=BUTTON_FG
        )
        self.question_label.pack(pady=20)
        
        self.option_buttons = []
        for i in range(4):
            btn = tk.Button(
                self.root, text="", width=40, font=OPTION_FONT,
                bg=BUTTON_BG, fg=BUTTON_FG, activebackground=BUTTON_ACTIVE_BG
            )
            btn.pack(pady=5)
            self.option_buttons.append(btn)
        
        self.feedback_label = tk.Label(
            self.root, text="", font=FEEDBACK_FONT, 
            bg=BACKGROUND_COLOR, fg=BUTTON_FG
        )
        self.feedback_label.pack(pady=10)
        
        # Next button
        self.next_button = tk.Button(
            self.root, text="Next", font=OPTION_FONT,
            bg="#d1e7dd", fg=BUTTON_FG, activebackground="#bce5cb"
        )
        self.next_button.pack(pady=10)
    
    def display_question(self, question_num, question_text, options):
        self.question_label.config(text=f"Q{question_num}: {question_text}")
        for i, option in enumerate(options):
            self.option_buttons[i].config(text=f"{chr(65+i)}. {option}")
        self.feedback_label.config(text="")
        
    def set_feedback(self, is_correct, correct_answer=None, correct_text=None):
        if is_correct:
            self.feedback_label.config(text="✅ Correct!", fg="green")
        else:
            self.feedback_label.config(
                text=f"❌ Incorrect! Correct: {correct_answer}. {correct_text}", 
                fg="red"
            )
    
    def disable_options(self):
        for btn in self.option_buttons:
            btn.config(state="disabled")
    
    def enable_options(self):
        for btn in self.option_buttons:
            btn.config(state="normal")
    
    def show_results(self, score, total, time_taken):
        for widget in self.root.winfo_children():
            widget.destroy()
            
        self.root.configure(bg=BACKGROUND_COLOR)
        tk.Label(
            self.root, text="🎉 Quiz Complete!", 
            font=("Segoe UI", 20), bg=BACKGROUND_COLOR, fg=BUTTON_FG
        ).pack(pady=20)
        
        tk.Label(
            self.root, text=f"You scored {score} out of {total}", 
            font=QUESTION_FONT, bg=BACKGROUND_COLOR, fg=BUTTON_FG
        ).pack(pady=10)
        
        tk.Label(
            self.root, text=f"Time taken: {time_taken}", 
            font=QUESTION_FONT, bg=BACKGROUND_COLOR, fg=BUTTON_FG
        ).pack(pady=10)
    
    def update_timer(self, minutes, seconds):
        self.timer_label.config(text=f"Time: {minutes}:{seconds:02d}")