from tkinter import *
import tkinter as tk
import Login_View
import HomeUser_View, ShowBook_View, BookNew_View,SearchBook_View, IssueBook_View, InfoUser_View, Contact_View, InfoApp_View

class BaseUserControl(tk.Tk):
    def __init__(self,user):
        super().__init__()
        self.user = user
        self.iconbitmap('./image/Icon_Book_Library.ico')
        self.title("Library Management System")
        self.geometry("1500x900")
        self.geometry("+%d+%d" % (200, 50))

        self.HomeUser_View = HomeUser_View.HomeUsersView(self,self.user)
        self.HomeUser_View.pack()

    def start(self):     
        self.resizable(False, False)
        self.mainloop()

    def prevHomeUser(self):
        self.HomeUser_View = HomeUser_View.HomeUsersView(self,self.user)
        self.HomeUser_View.pack()

    def nextShowBook(self,):
        self.HomeUser_View.destroy()
        self.ShowBook_View = ShowBook_View.ShowBookView(self,self.user)
        self.ShowBook_View.pack()
    
    def nextBookNew(self):
        self.HomeUser_View.destroy()
        self.BookNew_View = BookNew_View.BookNewView(self)
        self.BookNew_View.pack()

    def nextSearchBook(self):
        self.HomeUser_View.destroy()
        self.SearchBook_View = SearchBook_View.SearchBookView(self,self.user)
        self.SearchBook_View.pack()

    def nextIssueBook(self):
        self.HomeUser_View.destroy()
        self.IssueBook_View = IssueBook_View.IssueBookView(self,self.user)
        self.IssueBook_View.pack()

    def nextInfoUser(self):
        self.HomeUser_View.destroy()
        self.InfoUser_View = InfoUser_View.InfoUserView(self,self.user)
        self.InfoUser_View.pack()

    def nextContactUs(self):
        self.HomeUser_View.destroy()
        self.Contact_View = Contact_View.ContactUsView(self,self.user)
        self.Contact_View.pack()

    def nextInfoApp(self):
        self.HomeUser_View.destroy()
        self.InfoApp_View = InfoApp_View.InfoAppView(self,self.user)
        self.InfoApp_View.pack()

    def nextLogout(self):
        self.destroy()
        self.Login = Login_View.LoginView()

if __name__ == "__main__":
    base_view = BaseUserControl('ND00005')
    base_view.start()
