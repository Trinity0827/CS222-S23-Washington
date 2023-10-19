import tkinter as tk
window = tk.Tk()
window.geometry = ('500X500')
window.title("Find Your BMI")
 
def calBMI():
    weight_Info = float(txtWeight.get())
    height_Info = float(txtHeight.get())
    bmi = (weight_Info * 703) / (height_Info)**2
    lbl_bmi.configure(text=bmi)
    if bmi < 18.5:
        lbl.configure(text = "Underweight")
    elif bmi > 25:
        lbl.configure(text= "Overweight")
    elif bmi  >=18.5 and bmi<25:
        lbl.configure(text = "Optimal")   



    
# Input for Weight
inputWeight = tk.Label(window, text ="Please enter your weight in cm")
inputWeight.grid(column=0, row=15) 
txtWeight = tk.Entry(window, width=10,)
txtWeight.grid(column=4, row = 15)

#Input for Height 
inputHeight = tk.Label(window, text ="Please enter your Height in inches")
inputHeight.grid(column=0, row=40) 
txtHeight = tk.Entry(window, width=10,)
txtHeight.grid(column=4, row = 40)



#Bmi Calc Button 
btn_Cal = tk.Button(window, text = "Calculated BMI", command = calBMI)
btn_Cal.grid(column = 4, row = 100)



#Result Label
lbl_bmi = tk.Label(window, text=" ")
lbl_bmi.grid(column=4, row=600)

lbl = tk.Label(window, text= " ")
lbl.grid(column=4, row = 300)




window.mainloop()


