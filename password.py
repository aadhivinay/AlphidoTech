import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random
import string

def generate_password(length, include_uppercase=True, include_numbers=True, include_special_chars=True):
    lowercase_chars = string.ascii_lowercase
    uppercase_chars = string.ascii_uppercase if include_uppercase else ''
    digit_chars = string.digits if include_numbers else ''
    special_chars = string.punctuation if include_special_chars else ''

    all_chars = lowercase_chars + uppercase_chars + digit_chars + special_chars

    # Ensure the password length is at least 1 and not greater than the total characters
    length = max(1, min(length, len(all_chars)))

    password = ''.join(random.choice(all_chars) for _ in range(length))

    return password

def generate_password_and_update_entry():
    try:
        password_length = int(length_entry.get())
        if selected_category:
            password = generate_password(
                length=password_length,
                include_uppercase=upper_var.get(),
                include_numbers=number_var.get(),
                include_special_chars=special_var.get()
            )
            password_entry.config(state="normal")  # Set the state to normal to allow modifications
            password_entry.delete(0, tk.END)
            password_entry.insert(0, password)
            password_entry.config(state="readonly")  # Set the state back to readonly
        else:
            messagebox.showinfo("Category Not Selected", "Please select a category first.")
    except ValueError:
        messagebox.showinfo("Invalid Length", "Please enter a valid password length.")

def copy_to_clipboard():
    password = password_entry.get()
    root.clipboard_clear()
    root.clipboard_append(password)
    root.update()
    messagebox.showinfo("Password Copied", "Password copied to clipboard!")

def set_category(category):
    global selected_category
    selected_category = category
    highlight_category_button(category)

def highlight_category_button(selected_category=None):
    for btn_category, btn_object in category_buttons.items():
        if btn_category == selected_category:
            btn_object.config(style="Highlighted.TButton")
        else:
            btn_object.config(style="TButton")

def update_length_tooltip():
    length_tooltip.config(text="Adjust password length as needed.")

# GUI Setup
root = tk.Tk()
root.title("Password Generator")

# Set custom style for the highlighted category button with Roboto font
style = ttk.Style()
style.configure("TButton", font=("Roboto", 10))
style.configure("Highlighted.TButton", font=("Roboto", 10), background="lightgreen")

# Password Length
length_label = ttk.Label(root, text="Password Length:")
length_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

length_entry_var = tk.StringVar()
length_entry = ttk.Entry(root, textvariable=length_entry_var)
length_entry.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)
length_entry.insert(0, "Enter Length")
length_entry.bind("<FocusIn>", lambda event: length_entry.delete(0, tk.END))

# Tooltip for Password Length entry
length_tooltip = ttk.Label(root, text="")
length_tooltip.grid(row=0, column=2, padx=5, pady=10)
length_tooltip.bind("<Enter>", lambda event: None)  # Do nothing on enter
length_tooltip.bind("<Leave>", lambda event: length_tooltip.place(relx=0.5, rely=0.5, anchor="center"))

# Checkboxes
upper_var = tk.BooleanVar(value=True)
upper_check = ttk.Checkbutton(root, text="Include Uppercase", variable=upper_var)
upper_check.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)

number_var = tk.BooleanVar(value=True)
number_check = ttk.Checkbutton(root, text="Include Numbers", variable=number_var)
number_check.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)

special_var = tk.BooleanVar(value=True)
special_check = ttk.Checkbutton(root, text="Include Special Characters", variable=special_var)
special_check.grid(row=3, column=0, padx=10, pady=10, sticky=tk.W)

# Category Buttons
categories_frame = ttk.LabelFrame(root, text="Select Category:")
categories_frame.grid(row=4, column=0, columnspan=2, pady=10, padx=10, sticky=tk.W + tk.E)
categories = ["Website Account", "Banking", "Social Media", "Others"]

category_buttons = {}
selected_category = None

for i, category in enumerate(categories):
    category_button = ttk.Button(categories_frame, text=category, command=lambda cat=category: set_category(cat))
    category_button.grid(row=0, column=i, padx=5, pady=5)
    category_buttons[category] = category_button

# Generate Password Button
generate_button = ttk.Button(root, text="Generate Password", command=generate_password_and_update_entry)
generate_button.grid(row=5, column=0, columnspan=2, pady=20)

# Display Generated Password
password_label = ttk.Label(root, text="Generated Password:")
password_label.grid(row=6, column=0, padx=10, pady=10, sticky=tk.W)
password_entry = ttk.Entry(root, state="readonly")
password_entry.grid(row=6, column=1, padx=10, pady=10, sticky=tk.W + tk.E)

# Copy to Clipboard Button
copy_button = ttk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.grid(row=7, column=0, columnspan=2, pady=20)

# Run the GUI
root.mainloop()
