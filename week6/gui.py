import tkinter as tk
window = tk.Tk()
hello = tk.Label(text="Hello World") # creates a new lael
welcome = tk.Label(text="Welcome to CS222", foreground="white", background="black")
clickMe = tk.Button(text="ok",width =25, height=7, fg="blue", bg="yellow")





hello.pack() # add it to label
welcome.pack()
clickMe.pack()
window.mainloop()