import random
import string
import tkinter as tk
from tkinter import messagebox, ttk, scrolledtext

password_history = []

def generate_password():
    try:
        length = int(length_var.get())
        if length <= 0:
            messagebox.showerror("Invalid Input", "Password length must be greater than 0!")
            return
        
        if strength_var.get() == "Easy":
            characters = string.ascii_letters
        elif strength_var.get() == "Medium":
            characters = string.ascii_letters + string.digits
        else:
            characters = string.ascii_letters + string.digits + string.punctuation
        
        password = ''.join(random.choice(characters) for _ in range(length))
        password_var.set(password)
        password_history.append(password)
        update_history()
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number!")

def copy_to_clipboard():
    if password_var.get():
        root.clipboard_clear()
        root.clipboard_append(password_var.get())
        root.update()
        messagebox.showinfo("Copied", "Password copied to clipboard!")

def save_to_file():
    if password_history:
        with open("passwords.txt", "w") as file:
            for pwd in password_history:
                file.write(pwd + "\n")
        messagebox.showinfo("Saved", "Passwords saved to passwords.txt!")

def update_history():
    history_text.config(state="normal")
    history_text.delete(1.0, tk.END)
    for pwd in password_history[-5:]:  # Show last 5 passwords
        history_text.insert(tk.END, pwd + "\n")
    history_text.config(state="disabled")

root = tk.Tk()
root.title("Password Generator")
root.geometry("400x400")
root.configure(bg="#2C2F33")

tk.Label(root, text="Password Generator", font=("Arial", 16, "bold"), bg="#2C2F33", fg="white").pack(pady=10)

tk.Label(root, text="Password Length:", font=("Arial", 12), bg="#2C2F33", fg="white").pack()
length_var = tk.StringVar()
tk.Entry(root, textvariable=length_var, width=10, font=("Arial", 12)).pack(pady=5)

tk.Label(root, text="Password Strength:", font=("Arial", 12), bg="#2C2F33", fg="white").pack()
strength_var = ttk.Combobox(root, values=["Easy", "Medium", "Strong"], font=("Arial", 12), state="readonly")
strength_var.pack(pady=5)
strength_var.current(2)

tk.Button(root, text="🔒 Generate Password", command=generate_password, font=("Arial", 12), bg="#7289DA", fg="white").pack(pady=10)

password_var = tk.StringVar()
tk.Entry(root, textvariable=password_var, width=25, font=("Arial", 12), state="readonly").pack()

tk.Button(root, text="📋 Copy to Clipboard", command=copy_to_clipboard, font=("Arial", 12), bg="#43B581", fg="white").pack(pady=5)
tk.Button(root, text="💾 Save Passwords", command=save_to_file, font=("Arial", 12), bg="#FAA61A", fg="white").pack(pady=5)

tk.Label(root, text="Recent Passwords:", font=("Arial", 12, "bold"), bg="#2C2F33", fg="white").pack(pady=5)
history_text = scrolledtext.ScrolledText(root, width=30, height=5, font=("Arial", 10), state="disabled")
history_text.pack(pady=5)

tk.Button(root, text="❌ Exit", command=root.quit, font=("Arial", 12), bg="#F04747", fg="white").pack(pady=10)

root.mainloop()
