import tkinter as tk
from tkinter import ttk, messagebox

from models.task import Task
from services import storage_service


class TodoApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Desktop Todo Manager")
        self.root.geometry("500x400")

        self.tasks = storage_service.load_tasks()

        self.build_ui()
        self.refresh_tasks()

    def build_ui(self):

        top_frame = ttk.Frame(self.root)
        top_frame.pack(fill="x", padx=10, pady=10)

        self.task_entry = ttk.Entry(top_frame)
        self.task_entry.pack(side="left", fill="x", expand=True)

        add_btn = ttk.Button(top_frame, text="Add Task", command=self.add_task)
        add_btn.pack(side="left", padx=5)

        list_frame = ttk.Frame(self.root)
        list_frame.pack(fill="both", expand=True, padx=10)

        self.task_listbox = tk.Listbox(list_frame)
        self.task_listbox.pack(side="left", fill="both", expand=True)

        scrollbar = ttk.Scrollbar(list_frame)
        scrollbar.pack(side="right", fill="y")

        self.task_listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.task_listbox.yview)

        button_frame = ttk.Frame(self.root)
        button_frame.pack(fill="x", padx=10, pady=10)

        complete_btn = ttk.Button(
            button_frame,
            text="Toggle Complete",
            command=self.toggle_task
        )
        complete_btn.pack(side="left")

        delete_btn = ttk.Button(
            button_frame,
            text="Delete Task",
            command=self.delete_task
        )
        delete_btn.pack(side="left", padx=5)

    def refresh_tasks(self):

        self.task_listbox.delete(0, tk.END)

        for task in self.tasks:

            title = task["title"]

            if task["completed"]:
                title = "✔ " + title
            else:
                title = "✘ " + title

            self.task_listbox.insert(tk.END, title)

    def add_task(self):

        title = self.task_entry.get().strip()

        if not title:
            messagebox.showwarning("Warning", "Task title cannot be empty")
            return

        task = Task(title)

        self.tasks.append(task.to_dict())

        storage_service.save_tasks(self.tasks)

        self.task_entry.delete(0, tk.END)

        self.refresh_tasks()

    def toggle_task(self):

        selection = self.task_listbox.curselection()

        if not selection:
            return

        index = selection[0]

        task = self.tasks[index]

        task["completed"] = not task["completed"]

        storage_service.save_tasks(self.tasks)

        self.refresh_tasks()

    def delete_task(self):

        selection = self.task_listbox.curselection()

        if not selection:
            return

        index = selection[0]

        confirm = messagebox.askyesno(
            "Delete Task",
            "Are you sure you want to delete this task?"
        )

        if confirm:

            del self.tasks[index]

            storage_service.save_tasks(self.tasks)

            self.refresh_tasks()
