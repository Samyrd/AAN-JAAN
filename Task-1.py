import tkinter
import tkinter.messagebox
import pickle

root = tkinter.Tk()
root.title("To Do List :")

def add_task():
    task = entry_task.get()
    if task != "":
        listbox_tasks.insert(tkinter.END, task)
        entry_task.delete(0, tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="Warning!", message="Please enter desired task")

def delete_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except:
        tkinter.messagebox.showwarning(title="Warning!", message="Hey! select a task.")

def open_tasks():
    try:
        tasks = pickle.load(open("task.tdl", "rb"))
        listbox_tasks.delete(0, tkinter.END)
        for task in tasks:
            listbox_tasks.insert(tkinter.END, task)
    except:
        tkinter.messagebox.showwarning(title="Warning!", message="File not found")

def save_tasks():
    tasks = listbox_tasks.get(0, listbox_tasks.size())
    pickle.dump(tasks, open("task.tdl", "wb"))

# Create GUI
frame_tasks = tkinter.Frame(root)
frame_tasks.pack()

listbox_tasks = tkinter.Listbox(frame_tasks, height=8, width=100)
listbox_tasks.pack(side=tkinter.LEFT)

scrollbar_tasks = tkinter.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tkinter.RIGHT, fill=tkinter.Y)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

entry_task = tkinter.Entry(root, width=70)
entry_task.pack()

button_add_task = tkinter.Button(root, text="Add Task", bg ='Blue', fg='white',font=('TimesNewRoman'), width=48, command=add_task)
button_add_task.pack()

button_delete_task = tkinter.Button(root, text="Delete  Task", bg ='Red',fg='white',font=('TimesNewRoman'), width=48, command=delete_task)
button_delete_task.pack()

button_load_tasks = tkinter.Button(root, text="Open Task",fg='Orange',font=('TimesNewRoman'),  width=48, command=open_tasks)
button_load_tasks.pack()

button_save_tasks = tkinter.Button(root, text="Save Task",bg='Green',fg='white',font=('TimesNewRoman'),width=48, command=save_tasks)
button_save_tasks.pack()

root.mainloop()
