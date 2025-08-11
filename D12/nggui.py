import random
import tkinter as tk
from tkinter import messagebox


# Game Functions
def start_game():
    global alice, turns
    alice = random.randint(1, 100)
    difficulty = difficulty_var.get()
    turns = 5 if difficulty == "hard" else 10
    turns_label.config(text=f"Turns left: {turns}")
    guess_entry.delete(0, tk.END)
    message_label.config(text="Game started! Make your guess.")


def check_guess():
    global turns, alice
    try:
        guess = int(guess_entry.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a number between 1 and 100")
        return

    if guess > alice:
        message_label.config(text="Too high!")
    elif guess < alice:
        message_label.config(text="Too low!")
    else:
        messagebox.showinfo("Winner!", f"🎉 Congrats! The number was {alice}.")
        ask_play_again()
        return

    turns -= 1
    turns_label.config(text=f"Turns left: {turns}")

    if turns == 0:
        messagebox.showerror("Game Over", f"You've run out of turns! The number was {alice}.")
        ask_play_again()


def ask_play_again():
    play_again = messagebox.askyesno("Play Again", "Do you want to play again?")
    if play_again:
        start_game()
    else:
        root.destroy()


# GUI Setup
root = tk.Tk()
root.title("Number Guessing Game")
root.geometry("400x300")
root.resizable(False, False)

# Title
title_label = tk.Label(root, text="Number Guessing Game", font=("Arial", 18, "bold"))
title_label.pack(pady=10)

# Difficulty selection
difficulty_var = tk.StringVar(value="easy")
tk.Label(root, text="Select Difficulty:", font=("Arial", 12)).pack()
tk.Radiobutton(root, text="Easy (10 turns)", variable=difficulty_var, value="easy").pack()
tk.Radiobutton(root, text="Hard (5 turns)", variable=difficulty_var, value="hard").pack()

# Turns left
turns_label = tk.Label(root, text="Turns left: 0", font=("Arial", 12))
turns_label.pack(pady=5)

# Guess input
guess_entry = tk.Entry(root, font=("Arial", 14), justify="center")
guess_entry.pack(pady=5)

# Buttons
start_button = tk.Button(root, text="Start Game", font=("Arial", 12), command=start_game)
start_button.pack(pady=5)

guess_button = tk.Button(root, text="Submit Guess", font=("Arial", 12), command=check_guess)
guess_button.pack(pady=5)

# Message label
message_label = tk.Label(root, text="", font=("Arial", 12), fg="blue")
message_label.pack(pady=5)

root.mainloop()
