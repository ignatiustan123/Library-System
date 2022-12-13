from tkinter import *
from tkinter import ttk
import tkinter as tk

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

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        label = ttk.Label(self, text = "StartPage", font = LARGEFONT)
        label.grid(row=0,column=4,padx=10,pady=10)

        button1 = ttk.Button(self,text="Page 1",command = lambda : controller.show_frame(Page1))
        button1.grid(row = 1, column = 1, padx = 10, pady = 10)
        button2 = ttk.Button(self,text="Page 2",command = lambda : controller.show_frame(Page2))
        button2.grid(row = 2, column = 1, padx = 10, pady = 10)

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

class ALSMainPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label =ttk.Label(self, text = "(ALS)", font = LARGEFONT)
        label.grid(row = 0, column = 4, padx = 10, pady = 10)

        button1 = ttk.Button(self,text = "Membership", command = lambda : controller.show_frame(Membership))
        button1.grid(row=1,column=1,padx=10,pady=10)
        button2 = ttk.Button(self,text= "Books", command = lambda : controller.show_frame(Books))
        button2.grid(row=2,column=1,padx=10,pady=10)
        button3 = ttk.Button(self,text = "Loans", command = lambda : controller.show_frame(Loans))
        button3.grid(row=1,column=1,padx=10,pady=10)
        button4 = ttk.Button(self,text= "Reservations", command = lambda : controller.show_frame(Reservations))
        button4.grid(row=2,column=1,padx=10,pady=10)
        button5 = ttk.Button(self,text = "Fines", command = lambda : controller.show_frame(Fines))
        button5.grid(row=1,column=1,padx=10,pady=10)
        button6 = ttk.Button(self,text= "Reports", command = lambda : controller.show_frame(Reports))
        button6.grid(row=2,column=1,padx=10,pady=10)

class Membership(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = ttk.Label(self, text = "Select one of the Options below:", font = LARGEFONT)
        label.grid(row=0,column = 4, padx = 10, pady = 10)

        button1 = ttk.Button(self,text = "1. Creation", command = lambda : controller.show_frame(MemberCreation))
        button1.grid(row=1,column=1,padx=10,pady=10)
        button2 = ttk.Button(self,text = "2. Deletion", command = lambda : controller.show_frame(MemberDeletion))
        button2.grid(row=1,column=1,padx=10,pady=10)
        button3 = ttk.Button(self,text = "3. Update", command = lambda : controller.show_frame(MemberUpdate))
        button3.grid(row=1,column=1,padx=10,pady=10)
        button4 = ttk.Button(self,text = "Back To Main Menu", command = lambda : controller.show_frame(ALSMainPage))
        button4.grid(row=1,column=1,padx=10,pady=10)

class MemberCreation(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = ttk.Label(self, text = "To create Member, Please Enter Requested Information Below:", font = LARGEFONT)
        label.grid(row=0,column = 4, padx = 10, pady = 10)

        button1 = ttk.Button(self,text="Create Member", command = memberCreate())
        button1.grid(row=1,column=1, padx=10,pady=10)
        button2 = ttk.Button(self,text="Back to Main Menu", command = lambda : controller.show_frame(ALSMainPage))
        button2.grid(row=1,column=1,padx=10,pady=10)

    #def memberCreate():
                             
                             

class MemberDeletion(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = ttk.Label(self,text = "To Delete Member, Please Enter Membership ID:", font = LARGEFONT)
        label.grid(row=0,column = 4, padx=10,pady=10)

        button1 = ttk.Button(self,text="Delete Member", command = memberDelete())
        button1.grid(row=1,column=1,padx=10,pady=10)
        button2 = ttk.Button(self,text="Back to Membership Menu", command = lambda : controller.show_frame(Membership))
        button2.grid(row=1,column=1,padx=10,pady=10)

    #def memberDelete():

class MemberUpdate(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = ttk.Label(self,text = "To Update a Member, Please Enter Membership ID:", font = LARGEFONT)
        label.grid(row=0,column = 4, padx=10,pady=10)

        button1 = ttk.Button(self,text="Update Member",command = lambda : controller.show_frame(MemberUpdatePageTwo))
        button1.grid(row=1,column=1,padx=10,pady=10)
        button2 = ttk.Button(self,text="Back to Membership Menu", command = lambda : controller.show_frame(Membership))
        button2.grid(row=1,column=1,padx=10,pady=10)

class MemberUpdatePageTwo(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = ttk.Label(self,text = "Please Enter Requested Information Below:", font = LARGEFONT)
        label.grid(row=0,column = 4,padx=10,pady=10)

        button1 = ttk.Button(self,text="Update Member",command = memberUpdate())
        button1.grid(row=1,column=1,padx=10,pady=10)
        button2 = ttk.Button(self,text="Back to Membership Menu", command = lambda : controller.show_frame(Membership))
        button2.grid(row=1,column=1,padx=10,pady=10)

        
    #def memberUpdate():


class Books(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = ttk.Label(self, text = "Select one of the Options below:", font = LARGEFONT)
        label.grid(row=0,column = 4, padx = 10, pady = 10)

        button1 = ttk.Button(self,text = "4. Acquisition", command = lambda : controller.show_frame(BookAcquisition))
        button1.grid(row=1,column=1,padx=10,pady=10)
        button2 = ttk.Button(self,text = "5. Withdrawal", command = lambda : controller.show_frame(BookWithdrawal))
        button2.grid(row=1,column=1,padx=10,pady=10)
        button3 = ttk.Button(self,text = "Back to Main Menu", command = lambda : controller.show_frame(ALSMainPage))
        button3.grid(row=1,column=1,padx=10,pady=10)

class BookAcquisition(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = ttk.Label(self, text = "For New Book Acquisition, Please Enter Required Information Below:", font = LARGEFONT)
        label.grid(row=0,column = 4, padx = 10, pady = 10)

        button1 = ttk.Button(self,text = "Add New Book", command = bookAcquire())
        button1.grid(row=1,column =1 ,padx =10,pady=10)
        button2 = ttk.Button(self,text="Back to Books Menu", command = lambda : controller.show_frame(Books))
        button2.grid(row=1,column=1,padx=10,pady=10)

    #def bookAcquire():
        
class BookWithdrawal(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = ttk.Label(self, text = "To Remove Outdated Books From System, Please Enter Required Information Below:", font = LARGEFONT)
        label.grid(row=0,column = 4, padx = 10, pady = 10)

        button1 = ttk.Button(self,text = "Withdraw Book",command = bookWithdraw())
        button1.grid(row=1,column =1 ,padx =10,pady=10)
        button2 = ttk.Button(self,text="Back to Books Menu", command = lambda : controller.show_frame(Books))
        button2.grid(row=1,column=1,padx=10,pady=10)

    #def bookWithdraw():

class Loans(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = ttk.Label(self, text = "Select one of the Options below:", font = LARGEFONT)
        label.grid(row=0,column = 4, padx = 10, pady = 10)

        button1 = ttk.Button(self,text = "6. Borrow", command = lambda : controller.show_frame(BookBorrow))
        button1.grid(row=1,column=1,padx=10,pady=10)
        button2 = ttk.Button(self,text = "7. Return", command = lambda : controller.show_frame(BookReturn))
        button2.grid(row=1,column=1,padx=10,pady=10)
        button3 = ttk.Button(self,text = "Back to Main Menu", command = lambda : controller.show_frame(ALSMainPage))
        button3.grid(row=1,column=1,padx=10,pady=10)

class BookBorrow(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = ttk.Label(self,text = "To Borrow a Book, Please Enter Information Below:", font = LARGEFONT)
        label.grid(row=0,column = 4,padx=10,pady=10)

        button1 = ttk.Button(self,text = "Borrow Book", command = bookBorrow())
        button1.grid(row=1,column =1 ,padx =10,pady=10)
        button2 = ttk.Button(self,text="Back to Loans Menu", command = lambda : controller.show_frame(Loans))
        button2.grid(row=1,column=1,padx=10,pady=10)

    #def bookBorrow():
    
        
class BookReturn(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = ttk.Label(self,text = "To Return a Book, Please Enter Information Below:", font = LARGEFONT)
        label.grid(row=0,column = 4,padx=10,pady=10)

        button1 = ttk.Button(self,text = "Return Book", command = bookReturn())
        button1.grid(row=1,column =1 ,padx =10,pady=10)
        button2 = ttk.Button(self,text="Back to Loans Menu", command = lambda : controller.show_frame(Loans))
        button2.grid(row=1,column=1,padx=10,pady=10)

    #def bookReturn():
        
class Reservations(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = ttk.Label(self, text = "Select one of the Options below:", font = LARGEFONT)
        label.grid(row=0,column = 4, padx = 10, pady = 10)

        button1 = ttk.Button(self,text = "8. Reserve a Book", command = lambda : controller.show_frame(BookReserve))
        button1.grid(row=1,column=1,padx=10,pady=10)
        button2 = ttk.Button(self,text = "9. Cancel Reservation", command = lambda : controller.show_frame(CancelReserve))
        button2.grid(row=1,column=1,padx=10,pady=10)
        button3 = ttk.Button(self,text = "Back to Main Menu", command = lambda : controller.show_frame(ALSMainPage))
        button3.grid(row=1,column=1,padx=10,pady=10)

        
class BookReserve(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = ttk.Label(self, text = "To Reserve a Book, Please Enter Information Below:", font = LARGEFONT)
        label.grid(row=0,column=4,padx=10,pady=10)

        button1 = ttk.Button(self,text = "Reserve Book",command = bookReserve())
        button1.grid(row=1,column =1 ,padx =10,pady=10)
        button2 = ttk.Button(self,text="Back to Reservations Menu", command = lambda : controller.show_frame(Reservations))
        button2.grid(row=1,column=1,padx=10,pady=10)

    #def bookReserve():
        
class CancelReserve(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = ttk.Label(self, text = "To Cancel a Reservation, Please Enter Information Below:", font = LARGEFONT)
        label.grid(row=0,column=4,padx=10,pady=10)

        button1 = ttk.Button(self,text = "Cancel Reservation", command = cancelReserve())
        button1.grid(row=1,column =1 ,padx =10,pady=10)
        button2 = ttk.Button(self,text="Back to Reservations Menu", command = lambda : controller.show_frame(Reservations))
        button2.grid(row=1,column=1,padx=10,pady=10)

    #def cancelReserve():

class Fines(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = ttk.Label(self,text="Select one of the Options below:",font=LARGEFONT)
        label.grid(row=0,column=4,padx=10,pady=10)

        
        button1 = ttk.Button(self,text = "10. Payment", command = lambda : controller.show_frame(FinePayment))
        button1.grid(row=1,column=1,padx=10,pady=10)
        button2 = ttk.Button(self,text = "Back to Main Menu", command = lambda : controller.show_frame(ALSMainPage))
        button2.grid(row=1,column=1,padx=10,pady=10)

class FinePayment(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = ttk.Label(self, text = "To Pay a Fine, Please Enter Information Below:", font = LARGEFONT)
        label.grid(row=0,column=4,padx=10,pady=10)

        button1 = ttk.Button(self,text = "Pay Fine", command = payFine())
        button1.grid(row=1,column =1 ,padx =10,pady=10)
        button2 = ttk.Button(self,text="Back to Fines Menu", command = lambda : controller.show_frame(Fines))
        button2.grid(row=1,column=1,padx=10,pady=10)

    #def payFine()

class Reports(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = ttk.Label(self,text="Select one of the Options below:",font=LARGEFONT)
        label.grid(row=0,column=4,padx=10,pady=10)

        button1 = ttk.Button(self,text = "11. Book Search", command = lambda : controller.show_frame(BookSearch))
        button1.grid(row=1,column=1,padx=10,pady=10)
        button2 = ttk.Button(self,text = "12. Books on Loan", command )#command
        button2.grid(row=1,column=1,padx=10,pady=10)
        button3 = ttk.Button(self,text = "13. Books on Reservation", command ) #command
        button3.grid(row=1,column=1,padx=10,pady=10)
        button4 = ttk.Button(self,text = "14. Outstanding Fines", command) #command
        button4.grid(row=1,column=1,padx=10,pady=10)
        button5 = ttk.Button(self,text = "15. Books on Loan to Member", command = lambda : controller.show_frame(BooksOnLoanToMember))
        button5.grid(row=1,column=1,padx=10,pady=10)
        button6 = ttk.Button(self,text = "Back to Main Menu", command = lambda : controller.show_frame(ALSMainPage))
        button6.grid(row=1,column=1,padx=10,pady=10)

class BookSearch(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = ttk.Label(self, text = "Search based on one of the categories below:", font = LARGEFONT)
        label.grid(row=0,column=4,padx=10,pady=10)

        button1 = ttk.Button(self,text = "Search Book",command = bookSearch())
        button1.grid(row=1,column =1 ,padx =10,pady=10)
        button2 = ttk.Button(self,text="Back to Reports Menu", command = lambda : controller.show_frame(Reports))
        button2.grid(row=1,column=1,padx=10,pady=10)

    #def bookSearch():

class booksOnLoan(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = ttk.Label(self, text = "Books on Loan Report", font = LARGEFONT)
        label.grid(row=0,column=4,padx=10,pady=10)

        button1 = ttk.Button(self,text="Back to Reports Menu", command = lambda : controller.show_frame(Reports))
        button1.grid(row=1,column=1,padx=10,pady=10)

class booksOnReservation(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = ttk.Label(self, text = "Books on Reservation Report", font = LARGEFONT)
        label.grid(row=0,column=4,padx=10,pady=10)

        button1 = ttk.Button(self,text="Back to Reports Menu", command = lambda : controller.show_frame(Reports))
        button1.grid(row=1,column=1,padx=10,pady=10)

class outstandingFines(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = ttk.Label(self, text = "Members With Outstanding Fines", font = LARGEFONT)
        label.grid(row=0,column=4,padx=10,pady=10)

        button1 = ttk.Button(self,text="Back to Reports Menu", command = lambda : controller.show_frame(Reports))
        button1.grid(row=1,column=1,padx=10,pady=10)
        
class BooksOnLoanToMember(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = ttk.Label(self, text = "Books on Loan to Member", font = LARGEFONT)
        label.grid(row=0,column=4,padx=10,pady=10)

        button1 = ttk.Button(self,text = "Search Member", command = booksOnLoanToMember())
        button1.grid(row=1,column =1 ,padx =10,pady=10)
        button2 = ttk.Button(self,text="Back to Reports Menu", command = lambda : controller.show_frame(Reports))
        button2.grid(row=1,column=1,padx=10,pady=10)

    #def booksOnLoanToMember():

        
app = tkinterApp()
app.mainloop()
