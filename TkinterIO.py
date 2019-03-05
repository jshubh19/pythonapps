import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

root=tk.Tk()
T= tk.Label(root,text="I/O programe").pack()
tk.messagebox.showinfo("Welcome","Enter your welcome message here")
name=tk.simpledialog.askstring("name","what is your name")
age=tk.simpledialog.askfloat("age","what is your age")
output= "Hello, %s.I hope you are fine today."%(name)
output +="And i think your are %d years old." %(age)
tk.messagebox.showinfo("Result",output)
