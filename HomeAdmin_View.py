from tkinter import *
import tkinter as tk
from datetime import datetime 
from Connect_MSSQL import Connect_DB

class HomeAdminView(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

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
        self.canvas.create_text(175.0, 445.0, anchor = "nw", text = "Thư viện sách", fill = "#000000", font = ("RobotoRoman Bold", 30 * -1))
        self.img_button_thuviensach = PhotoImage(file = "./image/Admin/trangchu/thuviensach.png")
        self.button_thuviensach = Button(image = self.img_button_thuviensach, borderwidth = 0, highlightthickness = 0, command = lambda: self.nextShowBook(), relief = "flat")
        self.button_thuviensach.place(x = 171.0, y = 226.0, width = 210.0, height = 210.0)

        # Button Tìm kiếm sách
        self.canvas.create_text(525.0, 445.0, anchor = "nw", text = "Tìm sách", fill = "#000000", font = ("RobotoRoman Bold", 30 * -1))
        self.img_button_timkiemsach = PhotoImage(file = "./image/Admin/trangchu/timkiemsach.png")
        self.button_timkiemsach = Button(image = self.img_button_timkiemsach, borderwidth = 0, highlightthickness = 0, command = lambda: self.nextSearchBook(), relief = "flat")
        self.button_timkiemsach.place(x = 483.0, y = 223.0, width = 210.0, height = 210.0)


        # Button Quản trị sách
        self.canvas.create_text(810.0, 445.0, anchor = "nw", text = "Quản trị sách", fill = "#000000", font = ( "RobotoRoman Bold", 30 * -1))
        self.img_button_sach = PhotoImage(file = "./image/Admin/trangchu/quantrisach.png")
        self.button_sach = Button(image = self.img_button_sach, borderwidth = 0, highlightthickness = 0, command = lambda: self.nextContrlBook(), relief = "flat")
        self.button_sach.place(x = 795.0, y = 226.0, width = 210.0, height = 210.0)

        # Button Mượn trả
        self.canvas.create_text(1144.0, 445.0, anchor = "nw", text = "Mượn Trả", fill = "#000000", font = ("RobotoRoman Bold", 30 * -1))
        self.img_button_muontra = PhotoImage(file = "./image/Admin/trangchu/muontra.png")
        self.button_muontra = Button(image = self.img_button_muontra, borderwidth = 0, highlightthickness = 0, command = lambda: print("button_2 clicked"), relief = "flat")
        self.button_muontra.place(x = 1107.0, y = 226.0, width = 210.0, height = 210.0)

        # Button Người dùng
        self.canvas.create_text(191.0, 793.0, anchor = "nw", text = "Người dùng", fill = "#000000", font = ("RobotoRoman Bold", 30 * -1))
        self.img_button_nguoidung = PhotoImage(file = "./image/Admin/trangchu/nguoidung.png")
        self.button_nguoidung = Button(image = self.img_button_nguoidung, borderwidth = 0, highlightthickness = 0, command = lambda: self.nextDeleteUser(), relief = "flat")
        self.button_nguoidung.place(x = 165.0, y = 570.0, width = 210.0, height = 210.0)

        # Button Thống kê
        self.canvas.create_text(520.0, 793.0, anchor = "nw", text = "Thống kê", fill = "#000000", font = ("RobotoRoman Bold", 30 * -1))
        self.img_button_thongke = PhotoImage(file = "./image/Admin/trangchu/thongke.png")
        self.button_thongke = Button(image = self.img_button_thongke, borderwidth = 0, highlightthickness = 0, command = lambda: self.nextStatistics(), relief = "flat")
        self.button_thongke.place(x = 483.0, y = 570.0, width = 210.0, height = 210.0)

        # Button Thông tin thêm
        self.canvas.create_text(797.0, 793.0, anchor = "nw", text = "Thông tin thêm", fill = "#000000", font = ("RobotoRoman Bold", 30 * -1))
        self.img_button_thongtinthem = PhotoImage(file = "./image/Admin/trangchu/thongtinthem.png")
        self.button_thongtinthem = Button(image = self.img_button_thongtinthem, borderwidth = 0, highlightthickness = 0, command = lambda: self.nextInfoApp(), relief = "flat")
        self.button_thongtinthem.place(x = 795.0, y = 570.0, width = 210.0, height = 210.0)

        # Button Đăng xuất
        self.canvas.create_text(1143.0, 793.0, anchor = "nw", text = "Đăng xuất", fill = "#000000", font = ("RobotoRoman Bold", 30 * -1))
        self.img_button_dangxuat = PhotoImage(file = "./image/Admin/trangchu/dangxuat.png")
        self.button_dangxuat = Button(image = self.img_button_dangxuat, borderwidth = 0, highlightthickness = 0, command = lambda: self.nextLogout(), relief = "flat")
        self.button_dangxuat.place(x = 1107.0, y = 570.0, width = 210.0, height = 210.0)

        # Operation
        self.img_operation = PhotoImage(file = "./image/Admin/trangchu/operation.png")
        self.operation = self.canvas.create_image(197.0, 195.0, image = self.img_operation)

        # Action
        self.img_action = PhotoImage(file = "./image/Admin/trangchu/action.png")
        self.action = self.canvas.create_image(174.0, 538.0, image = self.img_action)

        self.canvas.create_text(1400.0, 61.0, anchor = "ne", text = f"Quản trị viên, Hồ Văn Công Bình", fill = "#000000", font = ("RobotoRoman Bold", 30 * -1))
        current_date = f'{datetime.now().day}/{datetime.now().month}/{datetime.now().year}'
        self.canvas.create_text(1400.0, 120.0, anchor = "ne", text = f"Date: {current_date}", fill = "#000000", font = ("RobotoRoman Bold", 30 * -1))


    def clearView(self):
        self.canvas.delete("all")
        buttons_list = [self.button_thuviensach, self.button_timkiemsach, self.button_muontra, self.button_nguoidung, self.button_thongtinthem, self.button_dangxuat]
        for button in buttons_list:
            button.destroy()

    def clearView(self):
        self.canvas.delete("all")
        buttons_list = [self.button_sach, self.button_muontra, self.button_nguoidung, self.button_dangxuat]
        for button in buttons_list:
            button.destroy()

    def nextContrlBook(self):
        self.clearView()
        self.master.nextContrlBook()

    def nextSearchBook(self):
        self.clearView()
        self.master.nextSearchBook()

    def nextShowBook(self):
        self.clearView()
        self.master.nextShowBook()

    def nextDeleteUser(self):
        self.clearView()
        self.master.nextDeleteUser()

    def nextInfoApp(self):
        self.clearView()
        self.master.nextInfoApp()

    def nextStatistics(self):
        self.clearView()
        self.master.nextStatistics()

    def nextLogout(self):
        self.clearView()
        self.master.nextLogout()
