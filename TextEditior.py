from tkinter import  *
from tkinter import ttk
from  tkinter import filedialog
from tkinter import messagebox
import Survey

root=Tk()
root.title("Editor")
root.geometry("400x380+0+0")

text=Text(root,width=400, height=380,font=('Arial',12),bd=2,highlightthickness=1)
text.pack()

#Methods/functions

def new():
    pass

def open_file():
    pass

def save():
    path=filedialog.asksaveasfilename()
    w=open(path,mode='w')
    w.write(text.get("1.0",END))

def rename():
    pass

def close():
    save()
    root.quit()

def cut():
    root.clipboard_clear()
    text.clipboard_append(string=text.selection_get())
    text.delete(index1=SEL_FIRST, index2=SEL_LAST)

def copy():
    root.clipboard_clear()
    text.clipboard_append(string=text.selection_get())

def paste():
    text.insert(INSERT,root.clipboard_get())

def delete():
    text.delete(index1=SEL_FIRST,index2=SEL_LAST )

def select_all():
    pass


def survey():
    win=Toplevel(root)

#menu

main_menu=Menu(root)
root.config(menu=main_menu)

menubar=Menu(main_menu)
main_menu.add_cascade(label="File",menu=menubar)
menubar.add_command(label="New",command=new)
menubar.add_command(label="Open",command=open_file)
menubar.add_command(label="Save",command=save)
menubar.add_command(label="Rename",command=rename)
menubar.add_separator()
menubar.add_command(label="Close",command=close)

editmenu=Menu(main_menu)
main_menu.add_cascade(label="Edit",menu=editmenu)
editmenu.add_command(label="Cut",command=cut)
editmenu.add_command(label="Copy",command=copy)
editmenu.add_command(label="Paste",command=paste)
editmenu.add_command(label="Delete",command=delete)
editmenu.add_separator()
editmenu.add_command(label="SelectALl",command=select_all)

Feedback=Menu(main_menu)
main_menu.add_cascade(label="Feedback",menu=Feedback)
Feedback.add_command(label="Survey",command=survey)



root.mainloop()