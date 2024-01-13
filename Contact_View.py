from tkinter import *
import tkinter as tk
from datetime import datetime 
from Connect_MSSQL import Connect_DB

class ContactUsView(tk.Frame):
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

        # Background contact
        self.img_bg_contact= PhotoImage(file = "./image/Users/lienhe/bg_contact.png")
        self.bg_contact = self.canvas.create_image(325.0, 526.0, image = self.img_bg_contact)

        self.canvas.create_text(885.0, 50.0, anchor = "nw", text = "Liên hệ", fill = "#00054B", font = ("PlayfairDisplay Regular", 100 * -1))

        self.img_entry = PhotoImage(file = "./image/Users/lienhe/entry.png")

        # Họ tên
        self.canvas.create_text(634.0, 216.0, anchor="nw", text="Họ và tên", fill="#000000", font=("Montserrat Regular", 32 * -1))
        self.bg_hoten = self.canvas.create_image(839.0,293.0, image = self.img_entry)
        self.entry_hoten = Entry(bd = 0, bg = "#FFFFFF", fg = "#000716", highlightthickness = 0)
        self.entry_hoten.place(x = 639.0, y = 254.0, width = 400.0, height = 76.0)

        # Email
        self.canvas.create_text(634.0, 374.0, anchor="nw", text="Email", fill="#000000", font=("Montserrat Regular", 32 * -1))
        self.bg_email = self.canvas.create_image(839.0, 451.0, image = self.img_entry)
        self.entry_email = Entry(bd = 0, bg = "#FFFFFF", fg = "#000716", highlightthickness = 0)
        self.entry_email.place(x = 639.0, y = 412.0, width = 400.0, height = 76.0)

        # Tin nhắn
        self.canvas.create_text(634.0, 532.0, anchor="nw", text="Tin nhắn", fill="#000000", font=("Montserrat Regular", 32 * -1))
        self.bg_tinnhan = self.canvas.create_image(839.0, 609.0, image = self.img_entry)
        self.entry_tinnhan = Entry(bd = 0, bg = "#FFFFFF", fg = "#000716", highlightthickness = 0)
        self.entry_tinnhan.place(x = 639.0, y = 570.0, width = 400.0, height = 76.0)

        # Button Contact Us
        self.img_contact = PhotoImage(file = "./image/Users/lienhe/contact_us.png")
        self.button_contact = Button(image = self.img_contact, borderwidth = 0, highlightthickness = 0, command = lambda: print("button_1 clicked"), relief = "flat")
        self.button_contact.place(x = 639.0, y = 712.0, width = 374.0, height = 77.0)

        # Button Facebook
        self.img_facebook = PhotoImage(file = "./image/Users/lienhe/facebook.png")
        self.button_facebook = Button(image = self.img_facebook, borderwidth = 0, highlightthickness = 0, command = lambda: print("button_2 clicked"), relief = "flat")
        self.button_facebook.place(x = 1118.0, y = 507.0, width = 50.0, height = 50.0)
        
        # Button Instagram
        self.img_instagram = PhotoImage(file = "./image/Users/lienhe/instagram.png")
        self.button_instagram = Button(image = self.img_instagram, borderwidth = 0, highlightthickness = 0, command = lambda: print("button_3 clicked"), relief = "flat")
        self.button_instagram.place(x = 1210.0, y = 507.0, width = 50.0, height = 50.0)

        # Button Skype
        self.img_skype = PhotoImage(file = "./image/Users/lienhe/skype.png")
        self.button_skype = Button(image = self.img_skype, borderwidth = 0, highlightthickness = 0, command = lambda: print("button_4 clicked"), relief = "flat")
        self.button_skype.place(x = 1302.0, y = 507.0, width = 50.0, height = 50.0)

        # Button LinkedIn
        self.img_linkedin = PhotoImage(file = "./image/Users/lienhe/linkedin.png")
        self.button_linkedin = Button(image = self.img_linkedin, borderwidth = 0, highlightthickness = 0, command = lambda: print("button_5 clicked"), relief = "flat")
        self.button_linkedin.place(x = 1394.0, y = 507.0, width = 50.0, height = 50.0)

        self.img_location = PhotoImage(file = "./image/Users/lienhe/location.png")
        self.image_location = self.canvas.create_image(1214.0, 265.0, image = self.img_location)

        self.img_phone = PhotoImage(file = "./image/Users/lienhe/phone.png")
        self.image_phone = self.canvas.create_image(1222.0, 342.0, image = self.img_phone)

        self.img_email = PhotoImage(file = "./image/Users/lienhe/email.png")
        self.image_email = self.canvas.create_image(1282.0, 419.0, image = self.img_email)

        # Button Comeback
        self.img_comeback = PhotoImage(file = "./image/comeback.png")
        self.button_comeback = Button(image = self.img_comeback, borderwidth = 0, highlightthickness = 0, command = lambda: self.prevHomeUser(), relief = "flat")
        self.button_comeback.place(x = 1146.0, y = 752.0, width = 271.0, height = 75.0)

    def prevHomeUser(self):
        self.master.prevHomeUser()
