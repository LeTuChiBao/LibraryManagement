from tkinter import *
import tkinter as tk
import AddBook_View, UpdateBook_View, DeleteBook_View

class ControlBookView(tk.Frame):
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

        self.img_bg_control = PhotoImage(file = "./image/Admin/sach/bg_control.png")
        self.bg_control = self.canvas.create_image(1138.0, 437.0, image = self.img_bg_control)

        self.img_button_themsach = PhotoImage(file = "./image/Admin/sach/themsach.png")
        self.button_themsach = Button(image = self.img_button_themsach, borderwidth = 0, highlightthickness = 0, command = lambda: self.nextAddBook(), relief = "flat")
        self.button_themsach.place(x = 340.0, y = 261.0, width = 295.0, height = 75.0)

        self.img_button_suasach = PhotoImage(file = "./image/Admin/sach/suasach.png")
        self.button_suasach = Button(image = self.img_button_suasach, borderwidth = 0, highlightthickness = 0, command = lambda: self.nextUpdateBook(), relief = "flat")
        self.button_suasach.place(x = 340.0, y = 414.0, width = 295.0, height = 75.0)

        self.img_button_xoasach = PhotoImage(file = "./image/Admin/sach/xoasach.png")
        self.button_xoasach = Button(image = self.img_button_xoasach, borderwidth = 0, highlightthickness = 0, command = lambda: self.nextDeleteBook(), relief = "flat")
        self.button_xoasach.place(x = 340.0, y = 563.0, width = 295.0, height = 75.0)

        # Button comback
        self.img_comeback = PhotoImage(file = "./image/comeback.png")
        self.button_comeback = Button(image = self.img_comeback, borderwidth = 0, highlightthickness = 0, command = lambda: self.prevHomeAdmin(), relief = "flat")
        self.button_comeback.place(x = 84.0, y = 770.0, width = 271.0, height = 75.0)

    def prevHomeAdmin(self):
        self.master.prevHomeAdmin()

    def nextAddBook(self):
        self.destroy()
        AddBook_View.AddBookView(self.master)

    def nextUpdateBook(self):
        self.destroy()
        UpdateBook_View.UpdateBookView(self.master)

    def nextDeleteBook(self):
        self.destroy()
        DeleteBook_View.DeleteBookView(self.master)
