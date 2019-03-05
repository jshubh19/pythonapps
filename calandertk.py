import tkinter as tk
from tkinter import ttk
import calendar

root=tk.Tk()
root.geometry("300x300+0+0")
root.title("calender")

#month=tk.IntVar()
year=tk.IntVar()
month=(1,2,3,4,5,6,7,8,9,10,11,12)

def Caln():
    month.get()
    year.get()


lblm=tk.Label(font=('freesansbold','10','bold'),bd=10,bg="white",fg="blue",text="month").grid(row=0,column=0)
mbox=tk.ttk.Combobox(textvariable=month,width=10,font=('freesansbold','10','bold'))
mbox.current()
mbox.grid(row=0,column=1)

lbly=tk.Label(font=('freesansbold','10','bold'),bd=10,bg="white",fg="blue",text="year").grid(row=0,column=2)
ey=tk.Entry(font=('freesansbold','10','bold'),bg="white",fg="blue",textvariable="year",
width=14).grid(row=0,column=3)
area=tk.Text(font=('freesansbold','10','bold'),bg="white",fg="blue",width=20,height=12,bd=10)
btn=tk.Button(font=('freesansbold','10','bold'),bg="white",fg="blue",width=8,height=2,command=Caln,
text="calender")
btn.grid(row=8,column=0)
root.mainloop()