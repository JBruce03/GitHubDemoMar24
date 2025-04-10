import tkinter as tk
from admin import AdminInterface
from quiz import QuizApp

def main():
    root = tk.Tk()
    root.geometry("500x400")
    tk.Label(root, text="Quiz Bowl", font=("Arial", 18)).pack()

    tk.Button(root, text="Admin Login", width=20, command=lambda: open_admin(root)).pack(pady=20)
    tk.Button(root, text="Take a Quiz", width=20, command=lambda: open_quiz(root)).pack(pady=20)

    root.mainloop()

def open_admin(root):
    for widget in root.winfo_children():
        widget.destroy()
    AdminInterface(root)

def open_quiz(root):
    for widget in root.winfo_children():
        widget.destroy()
    QuizApp(root)

if __name__ == "__main__":
    main()
