import tkinter as tk
from tkinter import messagebox
import random
import time
import os

root = tk.Tk()
root.geometry("1600x800+0+0")
root.title("Restaurent Management Systems")
#-------------------------define variables------------------------------------------#
text_input = tk.StringVar()
rand = tk.StringVar()
Burger = tk.StringVar()
Pizza = tk.StringVar()
Pasta = tk.StringVar()
Cold_drink = tk.StringVar()
Cup_cake= tk.StringVar()
f_fries=tk.StringVar()
full_meal=tk.StringVar()
Total = tk.StringVar()
sub_total = tk.StringVar()
tax = tk.StringVar()
p_charge=tk.StringVar()

operator=""

Burger.set(0)
Pizza.set(0)
Pasta.set(0)
Cold_drink.set(0)
Cup_cake.set(0)
f_fries.set(0)
#-------------------------Frame for window------------------------------------------#
Tops = tk.Frame(root, width=1600,height=50,relief=tk.SUNKEN)
Tops.pack(side=tk.TOP)
F1 = tk.Frame(root, width=800, height=700, relief=tk.SUNKEN)
F1.pack(side=tk.LEFT)
F2 = tk.Frame(root, width=300, height=700, relief=tk.SUNKEN)
F2.pack(side=tk.RIGHT)
#--------------------------Time------------------------------------------------------#
localtime=time.asctime(time.localtime(time.time()))
#--------------------------Info------------------------------------------------------#
lblinfo = tk.Label(Tops, font=('arial', 50, 'bold'),text="Restaurent Management System", fg="steel blue", bd=10, anchor='w')
lblinfo.grid(row=0,column=0)
lblinfo = tk.Label(Tops, font=('arial', 20, 'bold'),text=localtime,fg="steel blue", bd=10, anchor='w')
lblinfo.grid(row=1, column=0)
lblinfo = tk.Label(Tops, font=('arial', 15, 'bold'),text="Shubham Jangid",fg="steel blue", bd=10, anchor='w')
lblinfo.grid(row=2, column=0)
#-------------------------Calculator-------------------------------------------------#
def btnclick(numbers):
    global operator
    operator=operator + str(numbers)
    text_input.set(operator)
    pass
def btnClearDisplay():
    global operator
    operator=""
    text_input.set("")
    pass
def btnEqualsInput():
    global operator
    sumup= str(eval(operator))
    text_input.set(sumup)
    operator=""

def Ref():
    x=random.randint(10908, 500876)
    randomRef=str(x)
    rand.set("BILL" + randomRef)
    
    CoB=float(Burger.get())
    CoP=float(Pizza.get())
    CoPT=float(Pasta.get())
    CoD=float(Cold_drink.get())
    CoCK=float(Cup_cake.get())
    CoFF=float(f_fries.get())

    CostofBurger= CoB * 55
    CostofPizza= CoP *99.99
    CostofPasta= CoPT * 74
    CostofDrink= CoD * 17
    CostofCake= CoCK * 25
    CostofFries= CoFF *45
    
    CostofMeal = "R", str('%.2f' % (CostofBurger + CostofPizza + CostofPasta + CostofDrink + CostofCake + CostofFries))

    PayTax=((CostofBurger + CostofPizza + CostofPasta + CostofDrink + CostofCake + CostofFries)*0.7)

    TotalCost= (CostofBurger + CostofPizza + CostofPasta + CostofDrink + CostofCake + CostofFries)
    
    #Parking_charge=30
    #p_c= str(30)
    pc="R"+str(30)

    AllCost= "R", str('%.2f'%(PayTax + TotalCost ))

    PaidTax= "R", str('%.2f'% PayTax)

    full_meal.set(CostofMeal)
    tax.set(PaidTax)
    sub_total.set(CostofMeal)
    p_charge.set(pc)
    Total.set(AllCost)
    

def qExit():
    iExit=tk.messagebox.askyesno("Restaurent Management System", "Do you want exit the system")
    if iExit >0:
        root.destroy()
        return
    

def Reset():
    rand.set("")  
    Burger.set(0)
    Pizza.set(0)
    Pasta.set(0)
    Cold_drink.set(0)
    Cup_cake.set(0)
    f_fries.set(0)
    full_meal.set("")
    Total.set("")
    sub_total.set("")
    tax.set("")
    p_charge.set("")
     

textDisplay=tk.Entry(F2, font=('arial',20,'bold'), text=text_input, bd=30, insertwidth=4, bg="powder blue", 
justify='right')
textDisplay.grid(columnspan=4)

btn7=tk.Button(F2, padx=16, pady=16, bd=8,fg="white", font=('arial',20,'bold'), 
bg="#C34B7B", text="7", command=lambda: btnclick(7)).grid(row=2, column=0)

btn8=tk.Button(F2, padx=16, pady=16, bd=8,fg="white", font=('arial',20,'bold'), 
bg="#232a3b", text="8", command=lambda: btnclick(8)).grid(row=2, column=1)

btn9=tk.Button(F2, padx=16, pady=16, bd=8,fg="white", font=('arial',20,'bold'), 
bg="#101f41", text="9", command=lambda: btnclick(9)).grid(row=2, column=2)

Addition=tk.Button(F2, padx=16, pady=16, bd=8,fg="black", font=('arial',20,'bold'), 
bg="powder blue", text="+", command=lambda: btnclick("+")).grid(row=2, column=3)


btn4=tk.Button(F2, padx=16, pady=16, bd=8,fg="black", font=('arial',20,'bold'), 
bg="powder blue", text="4", command=lambda: btnclick(4)).grid(row=3, column=0)

btn5=tk.Button(F2, padx=16, pady=16, bd=8,fg="black", font=('arial',20,'bold'), 
bg="powder blue", text="5", command=lambda: btnclick(5)).grid(row=3, column=1)

btn6=tk.Button(F2, padx=16, pady=16, bd=8,fg="black", font=('arial',20,'bold'), 
bg="powder blue", text="6", command=lambda: btnclick(6)).grid(row=3, column=2)

Subtraction=tk.Button(F2, padx=16, pady=16, bd=8,fg="black", font=('arial',20,'bold'), 
bg="powder blue", text="-", command=lambda: btnclick("-")).grid(row=3, column=3)

btn1=tk.Button(F2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20,'bold'),
bg="powder blue", text="1",command=lambda: btnclick(1)).grid(row=4, column=0)

btn2=tk.Button(F2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20,'bold'),
bg="powder blue", text="2",command=lambda: btnclick(2)).grid(row=4, column=1)

btn3=tk.Button(F2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20,'bold'),
bg="powder blue", text="3",command=lambda: btnclick(3)).grid(row=4, column=2)

Multiply=tk.Button(F2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20,'bold'),
bg="powder blue", text="*",command=lambda: btnclick("*")).grid(row=4, column=3)


btn0=tk.Button(F2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20,'bold'),
bg="powder blue", text="0",command=lambda: btnclick(0)).grid(row=5, column=0)

btnClear=tk.Button(F2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20,'bold'),
bg="powder blue", text="C",command=btnClearDisplay).grid(row=5, column=1)

btnEquals=tk.Button(F2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20,'bold'),
bg="powder blue", text="=",command=btnEqualsInput).grid(row=5, column=2)

Division=tk.Button(F2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20,'bold'),
bg="powder blue", text="/",command=lambda: btnclick("/")).grid(row=5, column=3)

#------------------------ Restaurent Menu 1 ------------------------------------------------#
lblReference=tk.Label(F1,font=('arial',16,'bold'),bd=16, anchor='w', text="Reference").grid(row=0, column=0)
TxtReference=tk.Entry(F1,font=('arial',16,'bold'), textvariable=rand, insertwidth=4, justify='right', bd=10,
bg="powder blue").grid(row=0, column=1)

lblBurger=tk.Label(F1,font=('arial',16,'bold'),bd=16, anchor='w', text="Burger_G").grid(row=1, column=0)
TxtBurger=tk.Entry(F1,font=('arial',16,'bold'), textvariable=Burger, insertwidth=4, justify='right', bd=10,
bg="powder blue").grid(row=1, column=1)

lblPizza=tk.Label(F1,font=('arial',16,'bold'),bd=16, anchor='w', text="Pizza_hatt").grid(row=2, column=0)
TxtPizza=tk.Entry(F1,font=('arial',16,'bold'), textvariable=Pizza, insertwidth=4, justify='right', bd=10,
bg="powder blue").grid(row=2, column=1)

lblPasta=tk.Label(F1,font=('arial',16,'bold'),bd=16, anchor='w', text="The_Pasta").grid(row=3, column=0)
TxtPasta=tk.Entry(F1,font=('arial',16,'bold'), textvariable=Pasta, insertwidth=4, justify='right', bd=10,
bg="powder blue").grid(row=3, column=1)

lblDrink=tk.Label(F1,font=('arial',16,'bold'),bd=16, anchor='w', text="Cold_drink").grid(row=4, column=0)
TxtDrink=tk.Entry(F1,font=('arial',16,'bold'), textvariable=Cold_drink, insertwidth=4, justify='right', bd=10,
bg="powder blue").grid(row=4, column=1)

lblCake=tk.Label(F1,font=('arial',16,'bold'),bd=16, anchor='w', text="Cup Cake").grid(row=5, column=0)
TxtCake=tk.Entry(F1,font=('arial',16,'bold'), textvariable=Cup_cake, insertwidth=4, justify='right', bd=10,
bg="powder blue").grid(row=5, column=1)
#-----------------------Resturent Menu 2---------------------------------------------------------#
lblFries=tk.Label(F1,font=('arial',16,'bold'),bd=16, anchor='w', text="Fries").grid(row=0, column=2)
TxtFries=tk.Entry(F1,font=('arial',16,'bold'), textvariable=f_fries, insertwidth=4, justify='right', bd=10,
bg="powder blue").grid(row=0, column=3)

lblMeal=tk.Label(F1,font=('arial',16,'bold'),bd=16, anchor='w', text="Cost of Meal").grid(row=1, column=2)
TxtMeal=tk.Entry(F1,font=('arial',16,'bold'), textvariable=full_meal, insertwidth=4, justify='right', bd=10,
bg="powder blue").grid(row=1, column=3)

lblTax=tk.Label(F1,font=('arial',16,'bold'),bd=16, anchor='w', text="GST").grid(row=2, column=2)
TxtTax=tk.Entry(F1,font=('arial',16,'bold'), textvariable=tax, insertwidth=4, justify='right', bd=10,
bg="powder blue").grid(row=2, column=3)

lblParkingCharge=tk.Label(F1,font=('arial',16,'bold'),bd=16, anchor='w', text="Prking Charge").grid(row=3, column=2)
TxtParkingCharge=tk.Entry(F1,font=('arial',16,'bold'), textvariable=p_charge, insertwidth=4, justify='right', bd=10,
bg="powder blue").grid(row=3, column=3)



lblSubTotal=tk.Label(F1,font=('arial',16,'bold'),bd=16, anchor='w', text="Sub Total").grid(row=4, column=2)
TxtSubTotal=tk.Entry(F1,font=('arial',16,'bold'), textvariable=sub_total, insertwidth=4, justify='right', bd=10,
bg="powder blue").grid(row=4, column=3)

lblTotal=tk.Label(F1,font=('arial',16,'bold'),bd=16, anchor='w', text="Total").grid(row=5, column=2)
TxtTotal=tk.Entry(F1,font=('arial',16,'bold'), textvariable=Total, insertwidth=4, justify='right', bd=10,
bg="powder blue").grid(row=5, column=3)

#-------------------Button-------------------------------------------------------#
BtnTotal=tk.Button(F1,font=('arial',16,'bold'),padx=16,pady=8, bd=16, width=10,text="Total",bg="powder blue",
command=Ref).grid(row=7,column=1)
BtnReset=tk.Button(F1,font=('arial',16,'bold'),padx=16,pady=8, bd=16, width=10,text="Reset",bg="powder blue",
command=Reset).grid(row=7,column=2)
BtnExit=tk.Button(F1,font=('arial',16,'bold'),padx=16,pady=8, bd=16, width=10,text="Exit",bg="powder blue",
command=qExit).grid(row=7,column=3)

root.mainloop()

