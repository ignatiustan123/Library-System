from sqlalchemy import create_engine
import pandas as pd
from tkinter import *
from tkinter import ttk
import tkinter as tk
import tkinter.messagebox
from tkinter import simpledialog
from tkinter.messagebox import showinfo
import mysql.connector 

database = create_engine('mysql+mysqlconnector://root:Joemama123@localhost/library')

LARGEFONT = ("Verdana",35)

class tkinterApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side= "top",fill="both",expand = True)

        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)

        self.frames = {}

        for F in (StartPage, Page1, Page2):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row = 0, column = 0, sticky = 'nsew')

        self.show_frame(StartPage)

    def show_frame(self,cont):
        frame = self.frames[cont]
        frame.tkraise()

def printValue():
            #tname = testing.get()
            #pd.read_sql_query("SELECT * FROM Member", database)
    tk.messagebox.showinfo("WELCOME TO CREATE")
    
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        label = ttk.Label(self, text = "StartPage", font = LARGEFONT)
        label.grid(row=0,column=4,padx=10,pady=10)

        def printValue():
            #tname = testing.get()
            #pd.read_sql_query("SELECT * FROM Member", database)
            tk.messagebox.showinfo("WELCOME TO CREATE","HI")   

        def TRY():
            pa = tk.Toplevel()
            testing = Entry()
            testing.pack()

        def popup_bonus():
            win = tk.Toplevel()
            win.wm_title("Window")

            l = tk.Label(win, text="Input")
            l.grid(row=0, column=0)

            b = ttk.Button(win, text="Okay", command=win.destroy)
            b.grid(row=1, column=0)

        def popup_showinfo():
            showinfo("Window", "Hello World!")

        button1 = ttk.Button(self,text="Page 1",command = lambda : controller.show_frame(Page1))
        button1.grid(row = 1, column = 1, padx = 10, pady = 10)
        button2 = ttk.Button(self,text="Page 2",command = lambda : controller.show_frame(Page2))
        button2.grid(row = 2, column = 1, padx = 10, pady = 10)

        button3 = ttk.Button(self,text = "Create", command = printValue)
        button3.grid(row = 3,column = 1,padx=10,pady=10)

        button4 = ttk.Button(self,text = "Extra", command = popup_bonus)
        button4.grid(row=4,column=1,padx=10,pady=10)

        


class Page1(tk.Frame):

    def __init__(self,parent,controller):

        tk.Frame.__init__(self,parent)
        label = ttk.Label(self,text="Page 1", font = LARGEFONT)
        label.grid(row=0, column = 4, padx =10,pady=10)
        button1 = ttk.Button(self,text="StartPage", command = lambda : controller.show_frame(StartPage))
        button1.grid(row = 1, column =1, padx = 10, pady= 10)
        button2 = ttk.Button(self,text="Page 2", command = lambda : controller.show_frame(Page2))
        button2.grid(row = 2, column = 1, padx = 10, pady= 10)


class Page2(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = ttk.Label(self, text = "Page 2", font =LARGEFONT)
        label.grid(row=0, column = 4, padx = 10, pady = 10)

        button1 = ttk.Button(self,text = "Page 1", command = lambda : controller.show_frame(Page1))
        button1.grid(row = 1, column = 1, padx = 10, pady = 10)
        button2 = ttk.Button(self,text="Startpage", command = lambda : controller.show_frame(StartPage))
        button2.grid(row=2,column=1,padx=10,pady=10)

        
app = tkinterApp()
app.mainloop()
