import tkinter as tk

class Todo:
    def __init__(self, root):
        self.root = root
        self.root.title("ToDo list")
        self.tasks = [] 
        self.taskEntry = tk.Entry(root, width=50) #textbox 
        self.addButton = tk.Button(root, text="Add Task", command = self.AddTask)
        self.taskList = tk.Listbox(root, selectmode=tk.SINGLE, width=50)
        self.deleteButton = tk.Button(root, text="Delete Task", command = self.DeleteTask)
        self.taskEntry.pack()
        self.addButton.pack()
        self.taskList.pack()
        self.deleteButton.pack()

    #from the command self.addTask
    def AddTask(self):
        task = self.taskEntry.get()
        if task:
            self.tasks.append(task)
            self.UpdateTaskList()
            self.taskEntry.delete(0, tk.END)


    def DeleteTask(self): # in the gui delete whatever is made, # updating GUI 
        selectedIndex = self.taskList.curselection()
        if  selectedIndex:
            self.tasks.pop(selectedIndex[0])
            self.UpdateTaskList()


    def UpdateTaskList(self): # from line 22, #updateing GUI
        self.taskList.delete(0, tk.END)
        for task in self.tasks: # from Line 10
            self.taskList.insert(tk.END, task)


    


if __name__ == "__main__":
    root = tk.Tk()
    app = Todo(root)
    root.mainloop()