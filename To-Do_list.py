#task 1
#To-Do list
import tkinter as tk
from tkinter import messagebox

# Create the main window
root = tk.Tk()
root.title("To-Do List App")
root.geometry("400x450")

tasks = []

# Functions
def add_task():
    task = task_entry.get()
    if task:
        tasks.append(task)
        listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def delete_task():
    selected = listbox.curselection()
    if selected:
        task_index = selected[0]
        listbox.delete(task_index)
        tasks.pop(task_index)
    else:
        messagebox.showwarning("Warning", "No task selected.")

def update_task():
    selected = listbox.curselection()
    if selected:
        task_index = selected[0]
        updated_task = task_entry.get()
        if updated_task:
            tasks[task_index] = updated_task
            listbox.delete(task_index)
            listbox.insert(task_index, updated_task)
            task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Updated task cannot be empty!")
    else:
        messagebox.showwarning("Warning", "No task selected.")

# GUI Layout
task_entry = tk.Entry(root, font=("Arial", 14))
task_entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", command=add_task, width=15)
add_button.pack(pady=5)

update_button = tk.Button(root, text="Update Task", command=update_task, width=15)
update_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", command=delete_task, width=15)
delete_button.pack(pady=5)

listbox = tk.Listbox(root, font=("Arial", 14), width=30, height=10)
listbox.pack(pady=10)

root.mainloop()
