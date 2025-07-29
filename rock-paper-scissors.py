#task 2
#rock-paper-scissors game
import tkinter as tk
import random

# Main App Window
app = tk.Tk()
app.title("Rock, Paper, Scissors Game")
app.geometry("400x450")
app.config(bg="#f0f0f0")

# Global Score
user_score = 0
computer_score = 0

# Choices and Emojis
choices = ["rock", "paper", "scissors"]
emoji = {
    "rock": "🪨",
    "paper": "📄",
    "scissors": "✂️"
}

# Functions
def play(choice):
    global user_score, computer_score

    computer_choice = random.choice(choices)
    result = ""

    if choice == computer_choice:
        result = "😐 It's a Tie!"
    elif (choice == "rock" and computer_choice == "scissors") or \
         (choice == "paper" and computer_choice == "rock") or \
         (choice == "scissors" and computer_choice == "paper"):
        result = "🎉 You Win!"
        user_score += 1
    else:
        result = "💻 Computer Wins!"
        computer_score += 1

    user_choice_label.config(text=f"You chose: {emoji[choice]} {choice.capitalize()}")
    computer_choice_label.config(text=f"Computer chose: {emoji[computer_choice]} {computer_choice.capitalize()}")
    result_label.config(text=result)
    score_label.config(text=f"🧑 You: {user_score}  |  🤖 Computer: {computer_score}")

def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    user_choice_label.config(text="You chose:")
    computer_choice_label.config(text="Computer chose:")
    result_label.config(text="Result will appear here.")
    score_label.config(text="🧑 You: 0  |  🤖 Computer: 0")

# Labels
title = tk.Label(app, text="Rock, Paper, Scissors", font=("Arial", 20, "bold"), bg="#f0f0f0")
title.pack(pady=10)

user_choice_label = tk.Label(app, text="You chose:", font=("Arial", 12), bg="#f0f0f0")
user_choice_label.pack(pady=5)

computer_choice_label = tk.Label(app, text="Computer chose:", font=("Arial", 12), bg="#f0f0f0")
computer_choice_label.pack(pady=5)

result_label = tk.Label(app, text="Result will appear here.", font=("Arial", 14, "bold"), fg="blue", bg="#f0f0f0")
result_label.pack(pady=10)

score_label = tk.Label(app, text="🧑 You: 0  |  🤖 Computer: 0", font=("Arial", 12, "bold"), bg="#f0f0f0")
score_label.pack(pady=10)

# Buttons
button_frame = tk.Frame(app, bg="#f0f0f0")
button_frame.pack(pady=10)

rock_btn = tk.Button(button_frame, text="🪨 Rock", width=12, height=2, command=lambda: play("rock"))
rock_btn.grid(row=0, column=0, padx=5)

paper_btn = tk.Button(button_frame, text="📄 Paper", width=12, height=2, command=lambda: play("paper"))
paper_btn.grid(row=0, column=1, padx=5)

scissors_btn = tk.Button(button_frame, text="✂️ Scissors", width=12, height=2, command=lambda: play("scissors"))
scissors_btn.grid(row=0, column=2, padx=5)

reset_btn = tk.Button(app, text="🔁 Reset Game", command=reset_game, bg="#ddd", font=("Arial", 10))
reset_btn.pack(pady=20)

# Start the GUI
app.mainloop()
