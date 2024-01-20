import tkinter as tk
from tkinter import ttk, messagebox


class ToDoListApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List App")

        self.tasks = []
        self.completed_tasks = []

        # Style
        self.style = ttk.Style()
        self.style.configure("TButton", padding=5, font=('Bell MT', 12), background='#008080', foreground='black')
        self.style.configure("TEntry", padding=5, font=('Bell MT', 12))
        self.style.configure("TLabel", font=('Bell MT', 14, 'bold'), background='#008080',
                             foreground='white')  # Updated background and foreground for heading
        self.style.configure("TListbox", font=('Bell MT', 12), selectbackground="#d3d3d3", selectforeground="black")
        self.style.configure("TCheckbutton", indicatorsize=20,
                             font=('Bell MT', 12))  # Set the checkbox size to 20 pixels
        self.style.configure("TFrame", background='#008080')  # Set the background color here
        self.style.map("TButton", foreground=[('active', 'black')])

        # Widgets
        frame = ttk.Frame(master, style="TFrame")
        frame.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')

        self.task_entry = ttk.Entry(frame, width=30, style="TEntry")
        self.task_entry.grid(row=0, column=0, padx=10, pady=10, columnspan=2, sticky='w')
        self.task_entry.insert(0, "Task")
        self.task_entry.bind("<FocusIn>", self.clear_task_entry)

        self.add_button = ttk.Button(frame, text="Add Task", command=self.add_task, style="TButton")
        self.add_button.grid(row=0, column=3, padx=10, pady=10, sticky='w')

        self.task_listbox = tk.Listbox(frame, width=50, height=10, selectmode=tk.SINGLE, font=('Bell MT', 12),
                                       activestyle="none")
        self.task_listbox.grid(row=1, column=0, columnspan=4, padx=10, pady=10, sticky='nsew')
        self.task_listbox.bind("<Enter>", self.on_hover_enter)
        self.task_listbox.bind("<Leave>", self.on_hover_leave)
        self.task_listbox.bind("<Button-1>", self.on_task_click)

        self.mark_completed_button = ttk.Button(frame, text="Mark as Completed", command=self.mark_completed,
                                                style="TButton")
        self.mark_completed_button.grid(row=2, column=0, padx=10, pady=10, sticky='w')

        self.remove_button = ttk.Button(frame, text="Remove Task", command=self.remove_task, style="TButton")
        self.remove_button.grid(row=2, column=1, padx=10, pady=10, sticky='w')

        self.clear_button = ttk.Button(frame, text="Clear All Tasks", command=self.clear_tasks, style="TButton")
        self.clear_button.grid(row=2, column=2, padx=10, pady=10, sticky='w')

        # Heading for the completed tasks listbox
        self.completed_label = ttk.Label(frame, text="COMPLETED - TASKS", style="TLabel")
        self.completed_label.grid(row=3, column=0, columnspan=4, padx=10, pady=10, sticky='nsew')

        self.completed_listbox = tk.Listbox(frame, width=50, height=5, font=('Bell MT', 12))
        self.completed_listbox.grid(row=4, column=0, columnspan=4, padx=10, pady=10, sticky='nsew')

        # Populate listbox with existing tasks and completed tasks
        self.update_listboxes()

        # Center the content in the middle of the page
        self.master.update_idletasks()
        width = self.master.winfo_width()
        height = self.master.winfo_height()
        x = (self.master.winfo_screenwidth() // 2) - (width // 2)
        y = (self.master.winfo_screenheight() // 2) - (height // 2)
        self.master.geometry('{}x{}+{}+{}'.format(width, height, x, y))

        # Configure row and column weights for resizing
        frame.grid_columnconfigure(0, weight=1)
        frame.grid_rowconfigure(1, weight=1)
        frame.grid_rowconfigure(4, weight=1)

    def add_task(self):
        task = self.task_entry.get()

        if task and task != "Task":
            self.tasks.append({"task": task, "completed": False})
            self.update_listboxes()
            self.task_entry.delete(0, tk.END)
            self.task_entry.insert(0, "Task")
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def remove_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task = self.tasks[selected_task_index[0]]
            self.tasks.remove(task)
            self.update_listboxes()
        else:
            messagebox.showwarning("Warning", "Please select a task to remove.")

    def mark_completed(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task = self.tasks[selected_task_index[0]]
            task["completed"] = not task["completed"]
            self.update_listboxes()
        else:
            messagebox.showwarning("Warning", "Please select a task to mark as completed.")

    def clear_tasks(self):
        confirm = messagebox.askyesno("Confirmation", "Are you sure you want to clear all tasks?")
        if confirm:
            self.tasks = []
            self.completed_tasks = []
            self.update_listboxes()

    def update_listboxes(self):
        # Update main tasks listbox
        self.task_listbox.delete(0, tk.END)
        for idx, task in enumerate(self.tasks):
            task_status = "☐" if not task["completed"] else "☑"
            self.task_listbox.insert(tk.END, f"{task_status} {task['task']}")

        # Update completed tasks listbox
        self.completed_listbox.delete(0, tk.END)
        for idx, completed_task in enumerate(self.tasks):
            if completed_task["completed"]:
                self.completed_listbox.insert(tk.END, f"{idx + 1}. {completed_task['task']}")

    def on_hover_enter(self, event):
        self.task_listbox.config(cursor="hand2")

    def on_hover_leave(self, event):
        self.task_listbox.config(cursor="")

    def on_task_click(self, event):
        selected_task_index = self.task_listbox.nearest(event.y)
        task = self.tasks[selected_task_index]
        task["completed"] = not task["completed"]
        self.update_listboxes()

    def clear_task_entry(self, event):
        if self.task_entry.get() == "Task":
            self.task_entry.delete(0, tk.END)


def main():
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
