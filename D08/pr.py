import tkinter as tk
from tkinter import messagebox

def check_prime():
    try:
        number = int(entry.get())
        if number < 0:
            result = "Negative numbers do not have a property of primality!"
        elif number in (0, 1):
            result = f"Number {number} is neither prime nor composite!"
        else:
            for i in range(2, int(number ** 0.5) + 1):
                if number % i == 0:
                    result = f"Number {number} is a composite number!"
                    break
            else:
                result = f"Number {number} is a prime number!"
        messagebox.showinfo("Result", result)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid integer.")

# GUI setup
window = tk.Tk()
window.title("Prime Number Checker")
window.geometry("300x150")

label = tk.Label(window, text="Enter a number:")
label.pack(pady=5)

entry = tk.Entry(window)
entry.pack(pady=5)

check_button = tk.Button(window, text="Check", command=check_prime)
check_button.pack(pady=10)

window.mainloop()
