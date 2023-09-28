import tkinter as tk
from tkinter import tkk



window = tk.Tk()
combo = Combobox(window)
combo['values'] = ("IN", "CA", "MA" )
btn = ttk.Button(window, text="submit", comman=submit)


window.mainloop()