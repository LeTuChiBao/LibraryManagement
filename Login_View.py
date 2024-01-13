from tkinter import messagebox
import tkinter as tk
from tkinter import *
from Connect_MSSQL import Connect_DB
import Register_View
import BaseUser_Control
import BaseAdmin_Control

class LoginView(tk.Tk):
    def __init__(self):
        super().__init__()
        self.iconbitmap('./image/Icon_Book_Library.ico')
        self.title("Library Management System")
        self.geometry("1000x500")
        self.geometry("+%d+%d" % (500, 250))

        canvas = Canvas(self, bg = "#FFFFFF", height = 500, width = 1000, bd = 0, highlightthickness = 0, relief = "ridge")
        canvas.place(x = 0, y = 0)
        canvas.create_text(195.0, 70.0, anchor = "nw", text = "LOGIN", fill = "#9377EE", font = ("RobotoRoman Bold", 40 * -1))

        entry_image = PhotoImage(file = './image/entry_login.png')

        canvas.create_text(99.0, 123.0, anchor = "nw", text = "User name:", fill = "#555454", font = ("RobotoRoman Bold", 16 * -1))
        self.entry_bg_user = canvas.create_image(253.0, 167.0, image = entry_image)
        self.entry_user = Entry(bd = 0, bg = "#E3E3E3", fg = "#000716", highlightthickness = 0, font = ("RobotoRoman Bold", 16 * -1))
        self.entry_user.place(x = 101.0, y = 147.0, width = 304.0, height = 38.0)

        canvas.create_text(99.0, 200.0, anchor = "nw", text = "Password:", fill = "#555454", font = ("RobotoRoman Bold", 16 * -1))
        self.entry_bg_password = canvas.create_image(253.0, 244.0, image = entry_image)
        self.entry_password = Entry(bd = 0, bg = "#E3E3E3", fg = "#000716", highlightthickness = 0, font = ("RobotoRoman Bold", 16 * -1), show = '●')
        self.entry_password.place(x = 101.0, y = 224.0, width = 304.0, height = 38.0)

        img_button_login = PhotoImage(file = './image/button_login1.png')
        self.img_button_login = Button(image = img_button_login, borderwidth = 0, highlightthickness = 0, command = lambda: self.checkLogin(Event), relief = "flat")
        self.img_button_login.place( x = 171.0, y = 325.0, width = 164.0, height = 40.0)
        self.bind("<Return>", self.checkLogin)


        canvas.create_text(119.0, 394.0, anchor = "nw", text = "Don't have an account", fill = "#555454", font = ("RobotoRoman Regular", 16 * -1))
        button_image_2 = PhotoImage(file = './image/button_register.png')
        button_2 = Button(image = button_image_2, borderwidth = 0, highlightthickness = 0, command = lambda: self.nextRegister(), relief = "flat")
        button_2.place(x = 284.0, y = 391.0, width = 103.0, height = 26.0)

        button_image_3 = PhotoImage(file = './image/button_forgot.png')
        button_3 = Button(image = button_image_3, borderwidth = 0, highlightthickness = 0, command = lambda: print("button_3 clicked"), relief = "flat")
        button_3.place(x = 273.0, y = 283.0, width = 142.0, height = 26.0)

        image_image_1 = PhotoImage(file = './image/Library_Login.png')
        self.image_1 = canvas.create_image(713.0, 261.0, image = image_image_1)
        self.resizable(False, False)
        self.mainloop()
    
    def nextRegister(self):
        self.destroy()
        Register_View.RegisterView()

    def loadFromDB(self):
        database = Connect_DB.MSSQLConnection()
        database.connect()
        query = "SELECT * FROM DangNhap"
        lst = database.query(query)
        database.close()
        lst = list(lst)
        sublists = [list(item) for item in lst]
        for i in sublists:
            i[2] = i[2].strip()
        return sublists
    
    def checkLogin(self,e):
        data = self.loadFromDB()
        tenDangNhap = self.entry_user.get()
        matKhau = self.entry_password.get()
        if tenDangNhap == 'admin' and matKhau == 'admin':
            tenDangNhap = tenDangNhap.lower()
            self.destroy()
            BaseAdmin_Control.BaseAdminControl(tenDangNhap)
            return
        for user in data:
            if tenDangNhap != user[0] or matKhau != user[1]:
                continue
            elif  tenDangNhap == user[0] or matKhau == user[1]:
                self.destroy()
                user = user[2]
                BaseUser_Control.BaseUserControl(user)
                return
        else:
            messagebox.showwarning("Warning", "Tài khoản hoặc mật khẩu không chính xác!")
            return

if __name__ == '__main__':
    uilogin = LoginView()
    uilogin.mainloop()