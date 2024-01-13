from tkinter import *
import tkinter as tk
import Login_View
import ShowBook_View, SearchBook_View, InfoApp_View, HomeAdmin_View, ControlBook_View, DeleteUser_View, StatisticsLib_View

class BaseAdminControl(tk.Tk):
    def __init__(self,admin):
        super().__init__()
        self.admin = admin
        self.iconbitmap('./image/Icon_Book_Library.ico')
        self.title("Library Management System")
        self.geometry("1500x900")
        self.geometry("+%d+%d" % (200, 50))

        self.HomeAdmin_View = HomeAdmin_View.HomeAdminView(self)
        self.HomeAdmin_View.pack()

    def start(self):     
        self.resizable(False, False)
        self.mainloop()

    def prevHomeAdmin(self):
        self.HomeAdmin_View = HomeAdmin_View.HomeAdminView(self)
        self.HomeAdmin_View.pack()

    def nextShowBook(self):
        self.HomeAdmin_View.destroy()
        self.ShowBook_View = ShowBook_View.ShowBookView(self,self.admin)
        self.ShowBook_View.pack()

    def nextSearchBook(self):
        self.HomeAdmin_View.destroy()
        self.SearchBook_View = SearchBook_View.SearchBookView(self,self.admin)
        self.SearchBook_View.pack()

    def nextInfoApp(self):
        self.HomeAdmin_View.destroy()
        self.InfoApp_View = InfoApp_View.InfoAppView(self,self.admin)
        self.InfoApp_View.pack()

    def nextContrlBook(self):
        self.HomeAdmin_View.destroy()
        self.ControlBook_View = ControlBook_View.ControlBookView(self)
        self.ControlBook_View.pack()

    def nextDeleteUser(self):
        self.HomeAdmin_View.destroy()
        self.DeleteUser_View = DeleteUser_View.DeleteUserView(self)
        self.DeleteUser_View.pack()

    def nextStatistics(self):
        self.HomeAdmin_View.destroy()
        self.StatisticsLibrary_View = StatisticsLib_View.StatisticsLibView(self)
        self.StatisticsLibrary_View.pack()

    def nextLogout(self):
        self.destroy()
        self.Login = Login_View.LoginView()

if __name__ == "__main__":
    base_view = BaseAdminControl('admin')
    base_view.start()
