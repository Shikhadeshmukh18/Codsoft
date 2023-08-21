import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        tasks_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def remove_task():
    selected_task_index = tasks_listbox.curselection()
    if selected_task_index:
        tasks_listbox.delete(selected_task_index)

def clear_tasks():
    tasks_listbox.delete(0, tk.END)


root = tk.Tk()
root.title("TO-DO LIST")
task_entry = tk.Entry(root, width=55,background= "black",fg="white",font=(" sans Serif",15,"bold","italic"))
add_button = tk.Button(root, text="ADD TASK", command=add_task,background="aqua",font=("Sans serif",17,"bold","italic"))
remove_button = tk.Button(root, text="REMOVE TASK", command=remove_task,background="Coral",font=("devnagri",17 ,"bold","italic"))
clear_button = tk.Button(root, text="CLEAR TASK ", command=clear_tasks,background="Chartreuse",font=( "helvetica",17 ,"bold","italic"))
tasks_listbox = tk.Listbox(root, selectmode=tk.SINGLE,height=25, width=55,background="AntiqueWhite",fg="black",font=("Serif",15,"bold","italic"))

task_entry.pack(pady=10)
add_button.pack()
remove_button.pack()
clear_button.pack()
tasks_listbox.pack(pady=10)


root.mainloop()
