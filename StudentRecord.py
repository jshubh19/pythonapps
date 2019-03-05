import tkinter as tk
import MySQLdb
from tkinter import messagebox,ttk,simpledialog

def search():
    try:
       con=MySQLdb.connect(user="root",password="",host="localhost",db="db")
       cur=con.cursor()
       q="select * from StudentRecord where rollno='%s'"%rollno.get()
       cur.execute(q)
       result = cur.fetchone()
       name.set(result[0])
       age.set(result[1])
       #e1.configure(state="")
       con.close()
       
    except:
        tk.messagebox.showinfo('No data availale for this user','no user exist')
        clear() 
               
       
           
     

def clear():
    rollno.set('')
    name.set('')
    age.set('')

def add():
    try:
        con=MySQLdb.connect(user="root",password="",host="localhost",db="db")
        cur=con.cursor()
        q="insert into StudentRecord  values('%s','%s','%s')"%(name.get(),age.get(),rollno.get())
        cur.execute(q)
        con.commit()
        con.close()
        tk.messagebox.showinfo('User added successfully','Recored Saved')
    except:
        tk.messagebox.showinfo('Error','Error in user entry')
    finally:
        clear()
def update():
    try:
        con=MySQLdb.connect(user="root",password="",host="localhost",db="db")
        cur=con.cursor()
        q="update StudentRecord  set name='%s',age='%s' where rollno='%s' "%(name.get(),age.get(),rollno.get())
        cur.execute(q)
        con.commit()
        con.close()
        tk.messagebox.showinfo('Recored Updated Successfully')
    except:
        tk.messagebox.showinfo('Error','Error in update')
    finally:
        clear()
def delete():
    try:
        con=MySQLdb.connect(user="root",password="",host="localhost",db="db")
        cur=con.cursor()
        q="delete from StudentRecord  where rollno='%s' "%(rollno.get())
        cur.execute(q)
        con.commit()
        con.close()
        tk.messagebox.showinfo('Recored Deleted Successfully')
    except:
        tk.messagebox.showinfo('Error','Error in Delation')
    finally:
        clear()
def exit():
    iexit=tk.messagebox.askokcancel("Recoreds",'do you want to exit ')
    if iexit>0:
        root.destroy()
        return

root=tk.Tk()
root.geometry("500x300+0+0")
root.title("Records")
lbl=tk.Label(root, text="Programe For studends records").grid(row=0,column=0)

rollno=tk.StringVar()
name=tk.StringVar()
age=tk.StringVar()

l1=tk.Label(root, text="Rollno",font=('freesansbold','10','bold')).grid(row=1,column=0)
e1 = tk.Entry(root, textvariable=rollno, font=('arial', 16, 'bold'),  insertwidth=4, justify='right', fg='#C34B7B',
bg="powder blue").grid(row=1, column=1)

l2 = tk.Label(root, text="Name",font=('freesansbold','10','bold')).grid(row=2, column=0)
e2 = tk.Entry(root, textvariable=name,font=('arial',16,'bold'),  insertwidth=4, justify='right', fg='#3f3f3f',
bg="powder blue").grid(row=2, column=1)

l3 = tk.Label(root, text="Age",font=('freesansbold','10','bold')).grid(row=3, column=0)
e3 = tk.Entry(root, textvariable=age,font=('arial',16,'bold'),  insertwidth=4, justify='right', fg='#6f6f6f',
bg="powder blue").grid(row=3, column=1)

btn1 = tk.Button(root, text='search', command=search,font=('arial',10,'bold'),padx=2,pady=1, bd=4,
 width=7,bg="powder blue",
).grid(row=4, column=0)

btn2 = tk.Button(root, text='add', command=add,font=('arial',10,'bold'),padx=2,pady=1, bd=4,
 width=7,bg="powder blue").grid(row=4, column=1)

btn3 = tk.Button(root, text='update', command=update,font=('arial',10,'bold'),padx=2,pady=1, bd=4,
 width=7,bg="powder blue").grid(row=5, column=0)

btn4 = tk.Button(root, text='delete', command=delete,font=('arial',10,'bold'),padx=2,pady=1, bd=4,
 width=7,bg="powder blue").grid(row=5, column=1)
btn5= tk.Button(root, text='clear', command=clear,font=('arial',10,'bold'),padx=2,pady=1, bd=4,
 width=7,bg="powder blue").grid(row=6, column=0)
btn6= tk.Button(root, text='Exit', command=exit,font=('arial',10,'bold'),padx=2,pady=1, bd=4,
 width=7,bg="powder blue").grid(row=6, column=1)



root.mainloop()


          
