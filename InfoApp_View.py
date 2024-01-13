from tkinter import *
import tkinter as tk
from PIL import ImageTk

class InfoAppView(tk.Frame):
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

        self.canvas.create_text(795.0, 48.0, anchor = "nw", text = "Thông tin", fill = "#00054B", font = ("PlayfairDisplay", 100 * -1))

        # Background info
        self.img_bg_info = PhotoImage(file = "./image/Users/thongtinungdung/bg_info1.png")
        self.bg_info = self.canvas.create_image(432.0, 487.0, image = self.img_bg_info)

        self.img_thongtinungdung = ImageTk.PhotoImage(file = "./image/Users/thongtinungdung/thongtinungdung.png")
        self.thongtinungdung = self.canvas.create_image(1100.0, 465.0, image = self.img_thongtinungdung)

        # Button comback
        self.img_comeback = PhotoImage(file = "./image/comeback.png")
        self.button_comeback = Button(image = self.img_comeback, borderwidth = 0, highlightthickness = 0, command = lambda: self.prevHome(), relief = "flat")
        self.button_comeback.place(x = 1146.0, y = 780.0, width = 271.0, height = 75.0)

    def prevHome(self):
        if self.user == 'admin':
            self.master.prevHomeAdmin()
        else:
            self.master.prevHomeUser()