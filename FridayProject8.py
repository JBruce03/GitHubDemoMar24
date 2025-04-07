import sqlite3
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# === Database Setup ===
def setup_database():
    conn = sqlite3.connect('customers.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS customers (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    birthday TEXT NOT NULL,
                    email TEXT NOT NULL,
                    phone TEXT NOT NULL,
                    address TEXT NOT NULL,
                    contact_method TEXT NOT NULL
                )''')
    conn.commit()
    conn.close()

# === Submit Function ===
def submit_info():
    name = entry_name.get()
    birthday = entry_birthday.get()
    email = entry_email.get()
    phone = entry_phone.get()
    address = entry_address.get()
    contact_method = contact_method_var.get()

    # Basic validation
    if not (name and birthday and email and phone and address and contact_method != "Select Method"):
        messagebox.showwarning("Missing Info", "Please fill in all fields.")
        return

    conn = sqlite3.connect('customers.db')
    c = conn.cursor()
    c.execute("INSERT INTO customers (name, birthday, email, phone, address, contact_method) VALUES (?, ?, ?, ?, ?, ?)",
              (name, birthday, email, phone, address, contact_method))
    conn.commit()
    conn.close()

    messagebox.showinfo("Success", "Customer information saved successfully!")

    # Clear form
    entry_name.delete(0, tk.END)
    entry_birthday.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_address.delete(0, tk.END)
    contact_method_var.set("Select Method")

# === View Entries Function ===
def view_entries():
    view_win = tk.Toplevel(root)
    view_win.title("Submitted Customer Entries")
    view_win.geometry("800x400")

    tree = ttk.Treeview(view_win, columns=("ID", "Name", "Birthday", "Email", "Phone", "Address", "Contact"), show='headings')
    tree.heading("ID", text="ID")
    tree.heading("Name", text="Name")
    tree.heading("Birthday", text="Birthday")
    tree.heading("Email", text="Email")
    tree.heading("Phone", text="Phone")
    tree.heading("Address", text="Address")
    tree.heading("Contact", text="Contact Method")

    tree.column("ID", width=40)
    tree.column("Name", width=120)
    tree.column("Birthday", width=90)
    tree.column("Email", width=150)
    tree.column("Phone", width=100)
    tree.column("Address", width=180)
    tree.column("Contact", width=100)

    tree.pack(fill=tk.BOTH, expand=True)

    # Fetch data from database
    conn = sqlite3.connect('customers.db')
    c = conn.cursor()
    c.execute("SELECT * FROM customers")
    rows = c.fetchall()
    conn.close()

    for row in rows:
        tree.insert("", tk.END, values=row)

# === GUI Setup ===
setup_database()

root = tk.Tk()
root.title("Customer Information Management System")

# Labels and Entry Fields
tk.Label(root, text="Name:").grid(row=0, column=0, padx=10, pady=5, sticky='e')
entry_name = tk.Entry(root, width=30)
entry_name.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Birthday (MM-DD-YYYY):").grid(row=1, column=0, padx=10, pady=5, sticky='e')
entry_birthday = tk.Entry(root, width=30)
entry_birthday.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Email:").grid(row=2, column=0, padx=10, pady=5, sticky='e')
entry_email = tk.Entry(root, width=30)
entry_email.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Phone Number (###-###-####):").grid(row=3, column=0, padx=10, pady=5, sticky='e')
entry_phone = tk.Entry(root, width=30)
entry_phone.grid(row=3, column=1, padx=10, pady=5)

tk.Label(root, text="Address:").grid(row=4, column=0, padx=10, pady=5, sticky='e')
entry_address = tk.Entry(root, width=30)
entry_address.grid(row=4, column=1, padx=10, pady=5)

tk.Label(root, text="Preferred Contact Method:").grid(row=5, column=0, padx=10, pady=5, sticky='e')
contact_method_var = tk.StringVar()
contact_method_var.set("Select Method")
contact_method_menu = ttk.Combobox(root, textvariable=contact_method_var, values=["Email", "Phone", "Mail",], state="readonly", width=28)
contact_method_menu.grid(row=5, column=1, padx=10, pady=5)

# Submit Button
submit_button = tk.Button(root, text="Submit", command=submit_info, width=20, bg="green", fg="white")
submit_button.grid(row=6, column=0, columnspan=2, pady=(10, 5))
# View Entries Button
view_button = tk.Button(root, text="View Entries", command=view_entries, width=20, bg="blue", fg="white")
view_button.grid(row=7, column=0, columnspan=2, pady=(0, 20))

root.mainloop()

