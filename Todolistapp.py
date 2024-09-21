import tkinter as tk
from tkinter import messagebox

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Benazir's To-Do List Application")
        self.root.configure(bg="#f5f5f5")

        input_frame = tk.Frame(self.root, bg="#d3d3d3")
        input_frame.pack(pady=10)

        self.task_entry = tk.Entry(input_frame, width=50, bg="#ffffff", fg="#000000", borderwidth=2, relief="solid")
        self.task_entry.pack(side=tk.LEFT, padx=10)

        self.add_button = tk.Button(input_frame, text="Add Task", command=self.add_task, bg="#4CAF50", fg="#ffffff", relief="flat")
        self.add_button.pack(side=tk.LEFT)

        self.task_listbox = tk.Listbox(self.root, width=60, height=15, selectmode=tk.SINGLE, bg="#ffffff", fg="#000000", selectbackground="#a8d5e2", selectforeground="#000000")
        self.task_listbox.pack(padx=10, pady=10)

        action_frame = tk.Frame(self.root, bg="#d3d3d3")
        action_frame.pack(pady=10)

        self.completed_button = tk.Button(action_frame, text="Mark as Completed", command=self.mark_as_completed, bg="#FFC107", fg="#000000", relief="flat")
        self.completed_button.pack(side=tk.LEFT, padx=10)

        self.delete_button = tk.Button(action_frame, text="Delete Task", command=self.delete_task, bg="#F44336", fg="#ffffff", relief="flat")
        self.delete_button.pack(side=tk.LEFT)

    def add_task(self):
        """Add a new task to the list."""
        task = self.task_entry.get()
        if task:  
            self.task_listbox.insert(tk.END, task)  
            self.task_entry.delete(0, tk.END)  
        else:
            messagebox.showwarning("Input Error", "Please enter a task.")

    def mark_as_completed(self):
        """Mark the selected task as completed."""
        try:
            selected_index = self.task_listbox.curselection()[0]  
            task = self.task_listbox.get(selected_index)  
            self.task_listbox.delete(selected_index)  
            completed_task = f"{task} - Completed"
            self.task_listbox.insert(tk.END, completed_task)  
            self.task_listbox.itemconfig(tk.END, {'fg': 'green'})  
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to mark as completed.")

    def delete_task(self):
        """Delete the selected task from the list."""
        try:
            selected_index = self.task_listbox.curselection()[0]  
            self.task_listbox.delete(selected_index)  
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to delete.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
