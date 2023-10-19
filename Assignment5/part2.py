import tkinter as tk
window = tk.Tk()
window.geometry = ('500X500')
window.title("Car loan payment")


def calc_Payment():
    Car_Info = float(txtCar.get())
    down_Info = float(txtDown.get())
    PR_Info = float(txtPR.get())
    years_Info = float(txtyears.get())
    i = PR_Info / 1200
    n = years_Info * 12
    monthly = ((Car_Info - down_Info)* i * (1 + i)**n) / ((1 + i)**n - 1)
    lbl_monthly.configure(text=monthly)




# Input for price of car
Car_input = tk.Label(window, text ="Please enter the price of your car: ")
Car_input.grid(column=0, row=10) 
txtCar = tk.Entry(window, width=10,)
txtCar.grid(column=4, row = 10)

# Input for down payment 
down_input = tk.Label(window, text = "Please enter the price of your down payment: ")
down_input.grid(column =0, row=40)
txtDown = tk.Entry(window, width = 10,)
txtDown.grid(column = 4 , row = 40)

#Input annual Percentage Rate
PR_input = tk.Label(window, text = "Please enter your annual percentage rate: ")
PR_input.grid(column =0, row=60)
txtPR = tk.Entry(window, width = 10,)
txtPR.grid(column = 4 , row = 60)


#Input number of years
years_input = tk.Label(window, text = "Please enter the number of years: ")
years_input.grid(column =0, row=80)
txtyears = tk.Entry(window, width = 10,)
txtyears.grid(column = 4 , row = 80)




#payment Calc Button 
btn_Cal = tk.Button(window, text = "loan Payment", command = calc_Payment)
btn_Cal.grid(column = 4, row = 100)


#Result label
lbl_monthly = tk.Label(window, text=" ")
lbl_monthly.grid(column=4, row=600)









window.mainloop()