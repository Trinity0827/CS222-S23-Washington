import tkinter as tk

window = tk.Tk()
def decrease():
    pass

def increase():
    pass

btnDecrease = tk.Button(window, text ="-", command=decrease)
lblCounter = tk.Label(window, text="0")
btnIncrease = tk.Button(window, text="+", command=increase)
btnDecrease.grid(column=0, row=0)
lblCounter.grid(column=1, row=0)
btnIncrease.grid(column=2, row=0)

window.mainloop()