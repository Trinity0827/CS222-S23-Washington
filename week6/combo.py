import tkinter as tk
from tkinter.ttk import *
window = tk.Tk()
window.geometry('500x300')
window.title("Third Python GUI") # give an title 
combo = Combobox(window)
combo['values'] = ("IN", "CA", "MA" )
combo.current(1)
combo.grid(cloumn=0, row=0)
window.mainloop()