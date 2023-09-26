import tkinter as tk
window = tk.Tk()
window.title("Second Python GUI")
window.geometry('500x300') #resize window
lbl = tk.Label(window, text = "OK") # 

lbl.grid(column=0, row=0) #replacelbl.pack(), # grid places where u wnat it to be
txt = tk.Entry(window, width=10,)
txt.grid(column=1, row = 0)

def clicked():
    result = "Welcome " + txt.get () # get that txt u typed 
    lbl.configure(text=result) # what ever is typed is what going to be return 


btn = tk.Button(window, text = "Welcome", command = clicked)
btn.grid(column = 2, row = 0)
window.mainloop()