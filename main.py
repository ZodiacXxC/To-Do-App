from tkinter import INSERT, ttk , END ,messagebox
import tkinter as tk
import json
import datetime
from turtle import update

initial_data = {}

try:
    with open("data.json", 'r', encoding='utf-8') as json_file:
        task_dict = json.load(json_file)
        

except:
    with open("data.json", 'w', encoding='utf-8') as json_file:
        json.dump(initial_data, json_file, ensure_ascii=False, indent=4)
    with open("data.json", 'r', encoding='utf-8') as json_file:
        task_dict = json.load(json_file)


def changeStatus(event):
    with open("data.json", 'r', encoding='utf-8') as json_file:
                task_dict = json.load(json_file)
    selected_item = treeview.selection()
    if selected_item:
        item = treeview.item(selected_item)
        data = item['values']
        if data[4] == "Active":
            no = str(data[0])
            task_dict[no] = (data[1],data[2],data[3],"Finished")
            with open("data.json", 'w', encoding='utf-8') as json_file:
                json.dump(task_dict, json_file, ensure_ascii=False, indent=4)
            treeview.delete(*treeview.get_children())
            for key, value in task_dict.items():
                treeview.insert('', tk.END, values=(key, value[0], value[1],value[2],value[3]))
        else:
            no = str(data[0])
            task_dict[no] = (data[1],data[2],data[3],"Active")
            with open("data.json", 'w', encoding='utf-8') as json_file:
                json.dump(task_dict, json_file, ensure_ascii=False, indent=4)
                
            treeview.delete(*treeview.get_children())
            for key, value in task_dict.items():
                treeview.insert('', tk.END, values=(key, value[0], value[1],value[2],value[3]))
            
def addTask():
    task = taskEntry.get()
    lenth = len(task)
    min_chars_per_line = 45
    avg_chars_per_line = 90
    max_chars_per_line = 135
    if len(task) > max_chars_per_line:
        last_space_index = task.rfind(" ", 0, max_chars_per_line)
        if last_space_index == -1:
            last_space_index = max_chars_per_line
        task = task[:last_space_index] + "\n" + task[last_space_index+1:]
        
    if len(task) > avg_chars_per_line:
        last_space_index = task.rfind(" ", 0, avg_chars_per_line)
        if last_space_index == -1:
            last_space_index = avg_chars_per_line
        task = task[:last_space_index] + "\n" + task[last_space_index+1:]
        
    if len(task) > min_chars_per_line:
        last_space_index = task.rfind(" ", 0, min_chars_per_line)
        if last_space_index == -1:
            last_space_index = min_chars_per_line
        task = task[:last_space_index] + "\n" + task[last_space_index+1:]
        
    if task != "":
        current_time = datetime.datetime.now()
        current_time_formated = current_time.strftime("%Y-%m-%d %H:%M:%S")
        day = int(dayEntry.get())
        hour = int(hourEntry.get())
        adjusted_time = current_time + datetime.timedelta(days=day, hours=hour)
        current_adjusted_time = adjusted_time.strftime("%Y-%m-%d %H:%M:%S")
        with open("data.json", 'r', encoding='utf-8') as json_file:
            task_dict = json.load(json_file)
    
        if not task_dict:
            current_element = 1
        else:
            current_element = int(list(task_dict.keys())[-1]) + 1
        
        task_dict[current_element] = (task,current_time_formated,current_adjusted_time,"Active")
        with open("data.json", 'w', encoding='utf-8') as json_file:
            json.dump(task_dict, json_file, ensure_ascii=False, indent=4)
        
        treeview.delete(*treeview.get_children())
        for key, value in task_dict.items():
            treeview.insert('', tk.END, values=(key, value[0], value[1],value[2],"Active"))
        dayEntry.delete("0",END)
        dayEntry.insert(END,0)
        hourEntry.delete("0",END)
        hourEntry.insert(END,0)
        taskEntry.delete("0",END)
    else:
        messagebox.showerror("Error","Please add a task !!")

def validate_numeric_input(P):
    if P == "" or P == "." or P.isdigit():
        return True
    elif P.count('.') == 1 and P.replace(".", "").isdigit():
        return True
    else:
        return False
    

def select_view(event):
    selection = category.get()
    if selection == "All":
        with open("data.json", 'r', encoding='utf-8') as json_file:
            task_dict = json.load(json_file)
        treeview.delete(*treeview.get_children())
        for key, value in task_dict.items():
            treeview.insert('', tk.END, values=(key, value[0], value[1],value[2],value[3]))
    elif selection == "Active":
        with open("data.json", 'r', encoding='utf-8') as json_file:
            task_dict = json.load(json_file)
        treeview.delete(*treeview.get_children())
        for key, value in task_dict.items():
            if value[3] == "Active":
                treeview.insert('', tk.END, values=(key, value[0], value[1],value[2],value[3]))
    else:
        with open("data.json", 'r', encoding='utf-8') as json_file:
            task_dict = json.load(json_file)
        treeview.delete(*treeview.get_children())
        for key, value in task_dict.items():
            if value[3] == "Finished":
                treeview.insert('', tk.END, values=(key, value[0], value[1],value[2],value[3]))
    

def deleteTask():
    with open("data.json", 'r', encoding='utf-8') as json_file:
                task_dict = json.load(json_file)
    selected_item = treeview.selection()
    selection = category.get()
    if selected_item:
        item = treeview.item(selected_item)
        data = item['values']
        task_dict.pop(str(data[0]),None)
        with open('data.json', 'w', encoding="utf-8") as json_file:
            json.dump(task_dict, json_file, ensure_ascii=False, indent=4)
        treeview.delete(*treeview.get_children())
        if selection == "All":
            with open("data.json", 'r', encoding='utf-8') as json_file:
                task_dict = json.load(json_file)
            treeview.delete(*treeview.get_children())
            for key, value in task_dict.items():
                treeview.insert('', tk.END, values=(key, value[0], value[1],value[2],value[3]))
        elif selection == "Active":
            with open("data.json", 'r', encoding='utf-8') as json_file:
                task_dict = json.load(json_file)
            treeview.delete(*treeview.get_children())
            for key, value in task_dict.items():
                if value[3] == "Active":
                    treeview.insert('', tk.END, values=(key, value[0], value[1],value[2],value[3]))
        else:
            with open("data.json", 'r', encoding='utf-8') as json_file:
                task_dict = json.load(json_file)
            treeview.delete(*treeview.get_children())
            for key, value in task_dict.items():
                if value[3] == "Finished":
                    treeview.insert('', tk.END, values=(key, value[0], value[1],value[2],value[3]))
    
    

def updateTask():
    def save_update():
        with open("data.json", 'r', encoding='utf-8') as json_file:
            task_dict = json.load(json_file)
        task_dict[str(data[0])] = (newTaskEntry.get(),data[2],newDateFinishedEntry.get(),data[4])
        with open('data.json', 'w', encoding="utf-8") as json_file:
            json.dump(task_dict, json_file, ensure_ascii=False, indent=4)
        treeview.delete(*treeview.get_children())
        for key, value in task_dict.items():
            treeview.insert('', tk.END, values=(key, value[0], value[1],value[2],value[3]))
                
    selected_item = treeview.selection()
    item = treeview.item(selected_item)
    data = item['values']
    if selected_item:
        updateFrame = tk.Toplevel(root)
        updateFrame.resizable(False,False)
    
        frame1 = ttk.LabelFrame(updateFrame,text="Edit Task:")
        frame1.grid(row=0,column=0,pady=10,padx=10)
        newTaskLabel = ttk.Label(frame1,text="New Task:")
        newTaskLabel.grid(row=0,column=0,padx=(10,0),pady=10)
        newTaskEntry = ttk.Entry(frame1)
        newTaskEntry.grid(row=0,column=1,padx=10,pady=10)
        newTaskEntry.insert(END,data[1])

        newDateFinishedLabel = ttk.Label(frame1,text="New Time:")
        newDateFinishedLabel.grid(row=0,column=2,padx=(10,0),pady=10)
        newDateFinishedEntry = ttk.Entry(frame1)
        newDateFinishedEntry.grid(row=0,column=3,padx=10,pady=10)
        newDateFinishedEntry.insert(END,data[3])
        
        saveUpdate = ttk.Button(frame1,text="Save",command=save_update)
        saveUpdate.grid(row=0,column=4,padx=10,pady=10)
        updateFrame.update_idletasks()
        root_width = updateFrame.winfo_width()
        root_height = updateFrame.winfo_height()
        screen_width = updateFrame.winfo_screenwidth()
        screen_height = updateFrame.winfo_screenheight()
        x = (screen_width - root_width) // 2
        y = (screen_height - root_height) // 2
        updateFrame.geometry("+{}+{}".format(x, y))
        updateFrame.mainloop()


root = tk.Tk()
root.resizable(False,False)
root.title("To-Do App")
root.geometry("+%d+%d" % ((root.winfo_screenwidth() - root.winfo_reqwidth()) / 2,
                                       (root.winfo_screenheight() - root.winfo_reqheight()) / 2))

style = ttk.Style(root)


root.tk.call("source","forest-light.tcl")
style.theme_use("forest-light")
style.configure('Treeview', rowheight=70)
validate_numeric = root.register(validate_numeric_input)
frame = ttk.Frame(root)
frame.pack()
root.iconbitmap(default="To-Do.ico")
controlFrame = ttk.LabelFrame(frame,text="Control")
controlFrame.grid(row=0,column=0,padx=10,pady=10)

selected_category = tk.StringVar()
category = ttk.Combobox(controlFrame, textvariable=selected_category,state="readonly")
category['values'] = ["All","Active","Finished"]
category.current(0)
category.bind("<<ComboboxSelected>>", select_view)
category.grid(row=0,column=0,padx=(5,20),pady=5)

taskLab = ttk.Label(controlFrame,text="Task: ")
taskLab.grid(row=0,column=1,padx=(20,0),pady=5)
taskEntry = ttk.Entry(controlFrame)
taskEntry.grid(row=0,column=2,padx=(0,10),pady=5)

dayLab = ttk.Label(controlFrame,text="Days: ")
dayLab.grid(row=0,column=3,padx=(10,0),pady=5)
dayEntry = ttk.Entry(controlFrame,validate="key",validatecommand=(validate_numeric, "%P"),width=7)
dayEntry.grid(row=0,column=4,padx=(0,10),pady=5)
dayEntry.insert(END,0)

hourLab = ttk.Label(controlFrame,text="Hours: ")
hourLab.grid(row=0,column=5,padx=(10,0),pady=5)
hourEntry = ttk.Entry(controlFrame,validate="key",validatecommand=(validate_numeric, "%P"),width=7)
hourEntry.grid(row=0,column=6,padx=(0,10),pady=5)
hourEntry.insert(END,0)

insertButton = ttk.Button(controlFrame,text="Insert",command=addTask)
insertButton.grid(row=0,column=7,padx=5,pady=5)

updateButton = ttk.Button(controlFrame, text="Update",command=updateTask)
updateButton.grid(row=1, column=0, padx=(5,110),pady=10, sticky="W")

deleteButton = ttk.Button(controlFrame, text="Delete",command=deleteTask)
deleteButton.grid(row=1, column=0, padx=10,pady=10, sticky="E")

treeFrame = ttk.Frame(frame)
treeFrame.grid(row=1,column=0,padx=10,pady=10)
treeScroll = ttk.Scrollbar(treeFrame)
treeScroll.pack(side="right", fill="y")

cols = ("No.","Task","Addition time","Finished time","Status")
treeview = ttk.Treeview(treeFrame,show="headings",yscrollcommand=treeScroll.set,columns=cols,height=7)
treeview.column("No.", width=50, anchor="center")
treeview.column("Task", width=310, anchor="center")
treeview.column("Addition time", width=150, anchor="center")
treeview.column("Finished time", width=150, anchor="center")
treeview.column("Status", width=80, anchor="center")
treeview.bind("<Double-Button-1>",changeStatus)
treeview.pack()
treeScroll.config(command=treeview.yview)
treeview.heading("#1", text="No.")
treeview.heading("#2", text="Task")
treeview.heading("#3", text="Addition time")
treeview.heading("#4", text="Finished time")
treeview.heading("#5", text="Status")

for key, value in task_dict.items():
    treeview.insert('', tk.END, values=(key, value[0], value[1],value[2],value[3]))



root.update_idletasks()
root_width = root.winfo_width()
root_height = root.winfo_height()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width - root_width) // 2
y = (screen_height - root_height) // 2
root.geometry("+{}+{}".format(x, y))
root.mainloop()

