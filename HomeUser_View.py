from tkinter import *
import tkinter as tk
from datetime import datetime 
from Connect_MSSQL import Connect_DB

class HomeUsersView(tk.Frame):
    def __init__(self, master, user):
        super().__init__(master)
        self.user = user

        self.canvas = Canvas(self.master, bg = "#FFFFFF", height = 900, width = 1500, bd = 0, highlightthickness = 0, relief = "ridge")
        self.canvas.place(x = 0, y = 0)

        # Background
        self.img_background = PhotoImage(file = "./image/background.png")
        self.background = self.canvas.create_image(750.0, 450.0, image = self.img_background)

        # Logo
        self.img_logo = PhotoImage(file = "./image/logo.png")
        self.logo = self.canvas.create_image(320.0, 95.0, image = self.img_logo)

        # Frame option
        self.canvas.create_rectangle(103.0, 539.0, 1403.0, 839.0, fill = "#FFFFFF", outline = "")
        self.canvas.create_rectangle(100.0, 195.0, 1400.0, 495.0, fill = "#FFFFFF", outline = "")

        # Button Thư viện sách
        self.canvas.create_text(175.0, 445.0, anchor="nw", text="Thư viện sách", fill="#000000", font=("RobotoRoman Bold", 30 * -1))
        self.img_button_thuviensach = PhotoImage(file = "./image/Users/trangchu/thuviensach.png")
        self.button_thuviensach = Button(image = self.img_button_thuviensach, borderwidth = 0, highlightthickness = 0, command = lambda: self.nextShowBook(), relief = "flat")
        self.button_thuviensach.place(x = 171.0, y = 226.0, width = 210.0, height = 210.0)

        # Button Sách mới
        self.canvas.create_text(509.0, 446.0, anchor  ="nw", text = "Sách mới", fill = "#000000", font = ("RobotoRoman Bold", 30 * -1))
        self.img_button_sachmoi = PhotoImage(file = "./image/Users/trangchu/sachmoi.png")
        self.button_sachmoi = Button(image = self.img_button_sachmoi, borderwidth = 0, highlightthickness = 0, command = lambda: self.nextBookNew(), relief = "flat")
        self.button_sachmoi.place( x = 483.0, y = 223.0, width = 210.0, height = 210.0)

        # Button Tìm kiếm sách
        self.canvas.create_text(800.0, 445.0, anchor = "nw", text = "Tìm kiếm sách", fill = "#000000", font = ("RobotoRoman Bold", 30 * -1))
        self.img_button_timkiemsach = PhotoImage(file = "./image/Users/trangchu/timkiemsach.png")
        self.button_timkiemsach = Button(image = self.img_button_timkiemsach, borderwidth = 0, highlightthickness = 0, command = lambda: self.nextSearchBook(), relief = "flat")
        self.button_timkiemsach.place(x = 795.0, y = 226.0, width = 210.0, height = 210.0)

        # Button Mượn sách
        self.canvas.create_text(1144.0, 445.0, anchor = "nw", text = "Mượn sách", fill = "#000000", font = ("RobotoRoman Bold", 30 * -1))
        self.img_button_muonsach = PhotoImage(file = "./image/Users/trangchu/muonsach.png")
        self.button_muonsach = Button(image = self.img_button_muonsach, borderwidth = 0, highlightthickness = 0, command = lambda: self.nextIssueBook(), relief = "flat")
        self.button_muonsach.place(x = 1107.0, y = 226.0, width = 210.0, height = 210.0)

        # Button Người dùng
        self.canvas.create_text(191.0, 793.0, anchor = "nw", text = "Người dùng", fill = "#000000", font = ("RobotoRoman Bold", 30 * -1))
        self.img_button_nguoidung = PhotoImage(file = "./image/Users/trangchu/nguoidung.png")
        self.button_nguoidung = Button(image = self.img_button_nguoidung, borderwidth = 0, highlightthickness = 0, command = lambda: self.nextInfoUser(), relief = "flat")
        self.button_nguoidung.place(x = 165.0, y = 570.0, width = 210.0, height = 210.0)

        # Button Liên hệ
        self.canvas.create_text(539.0, 793.0, anchor = "nw", text = "Liên hệ", fill = "#000000", font = ("RobotoRoman Bold", 30 * -1))
        self.img_button_lienhe = PhotoImage(file = "./image/Users/trangchu/lienhe.png")
        self.button_lienhe = Button(image = self.img_button_lienhe, borderwidth = 0, highlightthickness = 0, command = lambda: self.nextContactUs(), relief = "flat")
        self.button_lienhe.place(x = 483.0, y = 570.0, width = 210.0, height = 210.0)

        # Button Thông tin thêm
        self.canvas.create_text(797.0, 793.0, anchor="nw", text = "Thông tin thêm", fill = "#000000", font = ("RobotoRoman Bold", 30 * -1))
        self.img_button_thongtinthem = PhotoImage(file = "./image/Users/trangchu/thongtinthem.png")
        self.button_thongtinthem = Button(image = self.img_button_thongtinthem, borderwidth = 0, highlightthickness = 0, command = lambda: self.nextInfoApp(), relief = "flat")
        self.button_thongtinthem.place(x = 795.0, y = 570.0, width = 210.0, height = 210.0)

        # Button Đăng xuất
        self.canvas.create_text(1143.0, 793.0, anchor = "nw", text = "Đăng xuất", fill = "#000000", font = ("RobotoRoman Bold", 30 * -1))
        self.img_button_dangxuat = PhotoImage(file = "./image/Users/trangchu/dangxuat.png")
        self.button_dangxuat = Button(image = self.img_button_dangxuat, borderwidth = 0, highlightthickness = 0, command = lambda: self.nextLogout(), relief = "flat")
        self.button_dangxuat.place(x = 1107.0, y = 570.0, width = 210.0, height = 210.0)

        # Operation
        self.img_operation = PhotoImage(file = "./image/Users/trangchu/operation.png")
        self.operation = self.canvas.create_image(197.0, 195.0, image = self.img_operation)

        # Action
        self.img_action = PhotoImage(file = "./image/Users/trangchu/action.png")
        self.action = self.canvas.create_image(174.0, 538.0, image = self.img_action)

        data = self.loadFromDB()
        self.canvas.create_text(1400.0, 61.0, anchor = "ne", text = f"Xin chào, {data[1]}", fill = "#000000", font = ("RobotoRoman Bold", 30 * -1))
        current_date = f'{datetime.now().day}/{datetime.now().month}/{datetime.now().year}'
        self.canvas.create_text(1400.0, 120.0, anchor = "ne", text = f"Date: {current_date}", fill = "#000000", font = ("RobotoRoman Bold", 30 * -1))

    def loadFromDB(self):
        database = Connect_DB.MSSQLConnection()
        database.connect()
        query = f"SELECT * FROM NguoiDung WHERE Id_NguoiDung = '{self.user}'"
        lst = database.query(query)
        database.close()
        lst = lst[0]
        lst = list(lst)
        lst[0] = lst[0].strip()
        return lst

    def clearView(self):
        self.canvas.delete("all")
        buttons_list = [self.button_thuviensach, self.button_sachmoi, self.button_timkiemsach, self.button_muonsach, self.button_nguoidung, self.button_lienhe, self.button_thongtinthem, self.button_dangxuat]
        for button in buttons_list:
            button.destroy()

    def nextShowBook(self):
        self.clearView()
        self.master.nextShowBook()

    def nextBookNew(self):
        self.clearView()
        self.master.nextBookNew()

    def nextSearchBook(self):
        self.clearView()
        self.master.nextSearchBook()
    
    def nextIssueBook(self):
        self.clearView()
        self.master.nextIssueBook()

    def nextInfoUser(self):
        self.clearView()
        self.master.nextInfoUser()

    def nextContactUs(self):
        self.clearView()
        self.master.nextContactUs()

    def nextInfoApp(self):
        self.clearView()
        self.master.nextInfoApp()
        
    def nextLogout(self):
        self.clearView()
        self.master.nextLogout()
