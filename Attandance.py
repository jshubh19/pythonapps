import tkinter as tk
from tkinter import StringVar,ttk
from tkinter import messagebox
import time
import datetime
import sys

root = tk.Tk()
root.geometry("1600x800+0+0")
root.title("Student Register")
root.configure(background='black')
#----------------------------------Frames-------------------------------------------------------------------#
LeftFrame=tk.Frame(root, width=1000, height=800,bd=8, relief='raise')
LeftFrame.pack(side=tk.LEFT)
RightFrame=tk.Frame(root, width=300, height=800, bd=10,relief='raise')
RightFrame.pack(side=tk.RIGHT)

LeftFrame1 = tk.Frame(LeftFrame, width=1000, height=100, bd=8, relief='raise')
LeftFrame1.pack(side=tk.TOP)
LeftFrame2 = tk.Frame(LeftFrame, width=1000, height=800, bd=8, relief='raise')
LeftFrame2.pack(side=tk.TOP)

RightFrame1 = tk.Frame(RightFrame, width=300, height=300, bd=10, relief='raise')
RightFrame1.pack(side=tk.TOP)
RightFrame2 = tk.Frame(RightFrame, width=300, height=800, bd=10, relief='raise')
RightFrame2.pack(side=tk.TOP)
#-----------------------------------Variables----------------------------------------------------------------#
DateofOrder=tk.StringVar()
value0=StringVar()
value1 = StringVar()
value2 = StringVar()
value3 = StringVar()
value4 = StringVar()
value5 = StringVar()
value6 = StringVar()
value7 = StringVar()
value8 = StringVar()
value9 = StringVar()
value10 = StringVar()
valueo11 = StringVar()

DateofOrder.set(time.strftime("%d/%m/%y"))


def Exit():
    qExit=tk.messagebox.askokcancel("Student Register","Do you want to Exit ")
    if qExit>0:
        root.destroy()
        return

#--------------------------Labels----------------------------------------------------------------------------#
lblNo=tk.Label(LeftFrame1,font=('arial',10,'bold'),text="Sr No.",bd=16).grid(row=0,column=0,sticky=tk.W)
lblStuID=tk.Label(LeftFrame1,font=('arial',10,'bold'),text="Student ID",bd=16).grid(row=0,column=1,sticky=tk.W)
lblStuName=tk.Label(LeftFrame1,font=('arial',10,'bold'),text="Student Name",bd=16).grid(row=0,column=2,sticky=tk.W)
lblCourseCode=tk.Label(LeftFrame1,font=('arial',10,'bold'),text="Course Code",bd=16).grid(row=0,column=3,sticky=tk.W)

box=tk.ttk.Combobox(LeftFrame1,textvariable=value0, state='readonly')
box['values']=('','/','L','0','A','S')
box.current(0)
box.grid(row=0,column=4)

btnArrow=tk.Button(LeftFrame1,font=('arial',10,'bold'),padx=2, pady=2, bd=2, text="Fill", width=10,
height=1,fg='Black').grid(row=0,column=5)
btnReset=tk.Button(LeftFrame1,font=('arial',10,'bold'),padx=2, pady=2, bd=2, text="Reset", width=10,
height=1,fg='Black').grid(row=0,column=6)
btnExit=tk.Button(LeftFrame1,font=('arial',10,'bold'),padx=2, pady=2, bd=2, text="Exit", width=10,
height=1,fg='Black',command=Exit).grid(row=0,column=7)

lblDateofOrder=tk.Label(LeftFrame1,font=('arial',10,'bold'),padx=2, pady=2,textvariable=DateofOrder,fg="black",
bg="white",relief='sunken',width=10).grid(row=0,column=8, sticky=tk.W)

#-------------------------------------LeftFrame2 row 0-------------------------------------------------------#

    
lblNo=tk.Label(LeftFrame2,font=('arial',10,'bold'),text="1",bd=16,width=2).grid(row=0,column=0,sticky=tk.W)
lblStuID_1=tk.Label(LeftFrame2,font=('arial',10,'bold'),text="BT1133",bd=16,width=12).grid(row=0,column=1,sticky=tk.W)
lblStuName=tk.Label(LeftFrame2,font=('arial',10,'bold'),text="Hari",bd=16,width=10).grid(row=0,column=2,sticky=tk.W)
lblCourseCode=tk.Label(LeftFrame2,font=('arial',10,'bold'),text="101",bd=16,width=10).grid(row=0,column=3,sticky=tk.W)


box = tk.ttk.Combobox(LeftFrame2, textvariable=value1, state='readonly')
box['values'] = ('', '/', 'L', '0', 'A', 'S')
box.current(0)
box.grid(row=0, column=4)

btnSpace=tk.Button(LeftFrame2,font=('arial',10,'bold'),padx=2, pady=2, width=10, height=1,bd=2, fg="black",
bg="white",text="").grid(row=0,column=5)

btnSpace=tk.Button(LeftFrame2,font=('arial',10,'bold'),padx=2, pady=2, width=10, height=1,bd=2, fg="black",
bg="white",text="").grid(row=0,column=6)

btnSpace=tk.Button(LeftFrame2,font=('arial',10,'bold'),padx=2, pady=2, width=10, height=1,bd=2, fg="black",
bg="white",text="").grid(row=0,column=7)


btnSpace=tk.Button(LeftFrame2,font=('arial',10,'bold'),padx=2, pady=2, width=10, height=1,bd=2, fg="black",
bg="white",text="").grid(row=0,column=8)
root.mainloop()

#-------------------------------------LeftFrame2 row 1-------------------------------------------------------#
#try:
lblNo1 = tk.Label(LeftFrame2, font=('arial', 10, 'bold'), text="2", bd=16, width=2).grid(row=1, column=0, sticky=tk.W)
lblStuID_1 = tk.Label(LeftFrame2, font=('arial', 10, 'bold'), text="BT11332", bd=16, width=12).grid(row=1, column=1,
                                                                                                    sticky=tk.W)
lblStuName = tk.Label(LeftFrame2, font=('arial', 10, 'bold'), text="Shubh", bd=16, width=10).grid(row=1, column=2,
                                                                                                  sticky=tk.W)
lblCourseCode = tk.Label(LeftFrame2, font=('arial', 10, 'bold'), text="101", bd=16, width=10).grid(row=1, column=3,
                                                                                                   sticky=tk.W)

box = tk.ttk.Combobox(LeftFrame2, textvariable=value2, state='readonly')
box['values'] = ('', '/', 'L', '0', 'A', 'S')
box.current(0)
box.grid(row=1, column=4)

btnSpace = tk.Button(LeftFrame2, font=('arial', 10, 'bold'), padx=2, pady=2, width=10, height=1, bd=2, fg="black",
                     bg="white", text="").grid(row=1, column=5)

btnSpace = tk.Button(LeftFrame2, font=('arial', 10, 'bold'), padx=2, pady=2, width=10, height=1, bd=2, fg="black",
                     bg="white", text="").grid(row=1, column=6)

btnSpace = tk.Button(LeftFrame2, font=('arial', 10, 'bold'), padx=2, pady=2, width=10, height=1, bd=2, fg="black",
                     bg="white", text="").grid(row=1, column=7)

btnSpace = tk.Button(LeftFrame2, font=('arial', 10, 'bold'), padx=2, pady=2, width=10, height=1, bd=2, fg="black",
                     bg="white", text="").grid(row=1, column=8)

#except:
    #pass

root.mainloop()

