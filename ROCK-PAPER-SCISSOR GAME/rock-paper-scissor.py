import random
import tkinter as tk
from tkinter import simpledialog, messagebox

choices = ["Rock", "Paper", "Scissors"]
player1_name = "Player 1"
player2_name = "Computer"
player1_score = 0
player2_score = 0
multiplayer_mode = False

def start_game():
    global player1_name, player2_name
    player1_name = simpledialog.askstring("Enter Name", "Enter your name:")
    if not player1_name:
        player1_name = "Player 1"
    
    if multiplayer_mode:
        player2_name = simpledialog.askstring("Enter Name", "Enter Player 2's name:")
        if not player2_name:
            player2_name = "Player 2"
    else:
        player2_name = "Computer"
    
    name_label.config(text=f"{player1_name} vs {player2_name}")
    reset_game()

def play(choice, player=1):
    if multiplayer_mode:
        if player == 1:
            player1_choice.set(choice)
            if player2_choice.get():
                determine_winner(player1_choice.get(), player2_choice.get())
        else:
            player2_choice.set(choice)
            if player1_choice.get():
                determine_winner(player1_choice.get(), player2_choice.get())
    else:
        computer_choice = random.choice(choices)
        determine_winner(choice, computer_choice)

def determine_winner(player1, player2):
    global player1_score, player2_score
    if player1 == player2:
        result = "It's a tie!"
    elif (player1 == "Rock" and player2 == "Scissors") or \
         (player1 == "Scissors" and player2 == "Paper") or \
         (player1 == "Paper" and player2 == "Rock"):
        result = f"{player1_name} wins!"
        player1_score += 1
    else:
        result = f"{player2_name} wins!"
        player2_score += 1

    update_display(player1, player2, result)

def update_display(player1, player2, result):
    result_label.config(text=f"{player1_name}: {player1} \n{player2_name}: {player2}\n\n{result}")
    score_label.config(text=f"Score - {player1_name}: {player1_score} | {player2_name}: {player2_score}")

def reset_game():
    global player1_score, player2_score
    player1_score, player2_score = 0, 0
    player1_choice.set("")
    player2_choice.set("")
    result_label.config(text="Make your move!")
    score_label.config(text=f"Score - {player1_name}: 0 | {player2_name}: 0")

def toggle_multiplayer():
    global multiplayer_mode
    multiplayer_mode = not multiplayer_mode
    mode_label.config(text="Multiplayer Mode: ON" if multiplayer_mode else "Multiplayer Mode: OFF")
    start_game()

root = tk.Tk()
root.title("Rock-Paper-Scissors")
root.geometry("450x550")
root.configure(bg="#2C2F33")

tk.Label(root, text="Rock-Paper-Scissors", font=("Arial", 18, "bold"), bg="#2C2F33", fg="white").pack(pady=10)
mode_label = tk.Label(root, text="Multiplayer Mode: OFF", font=("Arial", 12), bg="#2C2F33", fg="white")
mode_label.pack(pady=5)

name_label = tk.Label(root, text="Player vs Computer", font=("Arial", 14), bg="#2C2F33", fg="white")
name_label.pack(pady=5)

result_label = tk.Label(root, text="Make your move!", font=("Arial", 14), bg="#2C2F33", fg="white")
result_label.pack(pady=10)

score_label = tk.Label(root, text="Score - Player: 0 | Computer: 0", font=("Arial", 12), bg="#2C2F33", fg="white")
score_label.pack(pady=10)

player1_choice = tk.StringVar()
player2_choice = tk.StringVar()

btn_frame = tk.Frame(root, bg="#2C2F33")
btn_frame.pack(pady=10)

for text, choice in [("🪨 Rock", "Rock"), ("📄 Paper", "Paper"), ("✂️ Scissors", "Scissors")]:
    tk.Button(btn_frame, text=text, width=15, command=lambda ch=choice: play(ch, 1),
              font=("Arial", 12), bg="#7289DA", fg="white").pack(pady=5)

multiplayer_frame = tk.Frame(root, bg="#2C2F33")
multiplayer_frame.pack(pady=10)

for text, choice in [("🪨 Rock", "Rock"), ("📄 Paper", "Paper"), ("✂️ Scissors", "Scissors")]:
    tk.Button(multiplayer_frame, text=f"Player 2 {text}", width=15, command=lambda ch=choice: play(ch, 2),
              font=("Arial", 12), bg="#F04747", fg="white").pack(pady=5)

tk.Button(root, text="🎮 Start Game", width=15, command=start_game, font=("Arial", 12), bg="#FAA61A", fg="white").pack(pady=10)
tk.Button(root, text="👥 Toggle Multiplayer", width=20, command=toggle_multiplayer, font=("Arial", 12), bg="#FAA61A", fg="white").pack(pady=10)
tk.Button(root, text="🔄 Play Again", width=15, command=reset_game, font=("Arial", 12), bg="#43B581", fg="white").pack(pady=10)
tk.Button(root, text="❌ Exit", width=15, command=root.quit, font=("Arial", 12), bg="#F04747", fg="white").pack(pady=10)

root.mainloop()
