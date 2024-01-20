import tkinter as tk

def on_click(button_text):
    current_text = entry_var.get()
    if button_text == "=":
        try:
            result = eval(current_text)
            entry_var.set(result)
        except Exception as e:
            entry_var.set("Error")
    elif button_text == "C":
        entry_var.set(current_text[:-1])  # Remove the last character
    elif button_text == "AC":
        entry_var.set("")
    else:
        entry_var.set(current_text + button_text)

# Create main window
root = tk.Tk()
root.title("Calculator")

# Set custom theme colors to black and white
bg_color = "#000000"  # Black
entry_bg_color = "#F8F8F8"  # Light grey for entry background
btn_color = "#FFFFFF"  # White
fg_color = "#000000"  # Black
border_color = "#000000"  # Black for border color

# Entry widget to display input and results
entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, font=("Helvetica", 18), bd=10, relief=tk.GROOVE,
                 justify="right", bg=entry_bg_color, fg=fg_color, highlightthickness=2, highlightbackground=border_color)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

# Button layout
button_texts = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    'C', 'AC'
]

# Create and place buttons with custom colors for the remaining buttons
row_val = 1
col_val = 0
for button_text in button_texts:
    tk.Button(root, text=button_text, width=5, height=2, bd=5, relief=tk.GROOVE, bg=btn_color, fg=fg_color,
              command=lambda btn=button_text: on_click(btn)).grid(row=row_val, column=col_val, padx=5, pady=5, sticky="nsew")
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Configure row and column weights for resizing
for i in range(2):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

# Start the main loop
root.mainloop()
