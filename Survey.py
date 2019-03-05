from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog

class Feedback:
    def __init__(self,master):

        master.title("Feedback")
        master.resizable(False,False)
        master.configure(background="navajo white")

        self.style=ttk.Style()
        self.style.configure('TFrame',background="navajo white")
        self.style.configure('TLabel',background="navajo white",font=('Arial',11))
        self.style.configure('TButton',background="navajo white")
        self.style.theme_use('clam')



        self.frame_header=ttk.Frame(master)
        self.frame_header.pack()

        self.logo=PhotoImage(file="f1.gif").subsample(4,4)
        self.lable1=ttk.Label(self.frame_header, image=self.logo)
        self.lable1.grid(row=0,column=0,rowspan=2)
        self.lable2=ttk.Label(self.frame_header, text="Feedback Hub",font=('Arial',15,'bold'))
        self.lable2.grid(row=0,column=1)
        self.lable3 = ttk.Label(self.frame_header,wraplength=300, text="This is our feedback software you can  give your review here what you feel about us and can share your thoughts to improve us.")
        self.lable3.grid(row=1, column=1, )

        self.frame_content=ttk.Frame(master)
        self.frame_content.pack()
        self.labelc1=ttk.Label(self.frame_content, text="Name:")
        self.labelc1.grid(row=0,column=0,padx=5,sticky='sw')
        self.labelc2 = ttk.Label(self.frame_content, text="Email:")
        self.labelc2.grid(row=0, column=1,padx=5,sticky='sw')
        self.labelc3 = ttk.Label(self.frame_content, text="Comment:")
        self.labelc3.grid(row=2, column=0,padx=5,sticky='sw')

        self.entry_name=ttk.Entry(self.frame_content, width=24,font=('Arial',11))
        self.entry_name.grid(row=1,column=0,padx=5)
        self.entry_email = ttk.Entry(self.frame_content, width=24,font=('Arial',11))
        self.entry_email.grid(row=1, column=1,padx=5)
        self.entry_comment = Text(self.frame_content, width=50, height=10,font=('Arial',11))
        self.entry_comment.grid(row=3, column=0,columnspan=2,padx=5)

        self.buttonsub=ttk.Button(self.frame_content,text="Submit",command=self.submit)
        self.buttonsub.grid(row=4,column=0,padx=5,sticky='e')

        self.buttonclear = ttk.Button(self.frame_content, text="Clear",command=self.Clear)
        self.buttonclear.grid(row=4, column=1,padx=5,sticky='w')
        self.buttonsearch = ttk.Button(self.frame_content, text="Search")
        self.buttonsearch.grid(row=5, column=0,padx=5,sticky='e')
        self.buttonexit = ttk.Button(self.frame_content, text="Exit",command=self.Exit)
        self.buttonexit.grid(row=5, column=1,padx=5,sticky='w')

    def submit(self):
        print("Name:{}".format(self.entry_name.get()))
        print("Email:{}".format(self.entry_email.get()))
        print("Comments:{}".format(self.entry_comment.get(1.0, 'end')))
        #self.clear()
        messagebox.showinfo(title="Feedback", message="feedback Submitted!")

    def Clear(self):
        self.entry_name.delete('0','end')
        self.entry_email.delete('0','end')
        self.entry_comment.delete('1.0','end')

    def Exit(self):
        iexit = messagebox.askokcancel(title="Exit", message="Do you want to Exit?")
        if iexit > 0:
            root.destroy()
            return


if __name__=="__main__":
    root=Tk()
   # root.title("Feedback")
    feedback=Feedback(root)
    root.mainloop()