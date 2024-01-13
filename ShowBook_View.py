from tkinter import *
import tkinter as tk
from tkinter import ttk
from Connect_MSSQL import Connect_DB
from PIL import ImageTk

class ShowBookView(tk.Frame):
    def __init__(self, master,user):
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

        # Background book
        self.img_background_book = PhotoImage(file = "./image/Users/thongtinsach/background_book.png")
        self.background_book = self.canvas.create_image(1162.0, 473.0, image = self.img_background_book)

        # Bảng liệt kê tất cả sách
        self.table = ttk.Treeview(self.master, show = 'headings', padding = "10px")
        style = ttk.Style()
        style.configure("Treeview", font=("Tahoma", 10))
        self.table.place(x = 46, y = 173, height = 600, width = 760)
        self.table['columns'] = ('STT', 'Id', 'TenSach', 'TacGia', 'NhaXB')
        self.table.column('STT', width = 5, anchor = 'center')
        self.table.column('Id', width = 30, anchor = 'center')
        self.table.column('TenSach', width = 250, anchor = 'w')
        self.table.column('TacGia', width = 100, anchor = 'w')
        self.table.column('NhaXB', width = 100, anchor = 'w')
        self.table.heading('STT', text = 'STT')
        self.table.heading('Id', text = 'Mã sách')
        self.table.heading('TenSach', text = 'Tên Sách')
        self.table.heading('TacGia', text = 'Tác Giả')
        self.table.heading('NhaXB', text = 'Nhà XB')
        data = self.loadFromDB()
        for i in data:
            self.table.insert('','end', values = i)
        scrollbar_table = ttk.Scrollbar(self.table, orient = 'vertical', command = self.table.yview)
        self.table.configure(yscrollcommand = scrollbar_table.set)
        scrollbar_table.place(relx = 1, rely = 0, relheight = 1, anchor = 'ne')
        self.table.bind('<<TreeviewSelect>>', self.book_select)

        # Button Comeback
        self.img_comeback = PhotoImage(file = "./image/comeback.png")
        self.button_comeback = Button(image = self.img_comeback, borderwidth = 0, highlightthickness = 0, command = lambda: self.prevHome(), relief = "flat")
        self.button_comeback.place(x = 70.0, y = 798.0, width = 271.0, height = 75.0)

    def prevHome(self):
        if self.user == 'admin':
            self.master.prevHomeAdmin()
        else:
            self.master.prevHomeUser()

    def book_select(self,e):
        self.book = Label(self.master)
        self.book.place(x = 912.0, y = 143.0)
        selection = self.table.focus()
        values = self.table.item(selection,'values')
        img_book = ImageTk.PhotoImage(file = f"./image/image_book/{values[1]}.png")
        self.book.config(image = img_book)
        self.book.image = img_book

    def loadFromDB(self):
        data = []
        n = 0
        database = Connect_DB.MSSQLConnection()
        database.connect()
        query = "SELECT Id_Sach,TenSach,TenTacGia,NhaXB FROM Sach"
        lst = database.query(query)
        database.close()
        for i in lst:
            i = list(i)
            i.insert(0,n)
            i[1] = i[1].strip()
            data.append(i)
            n += 1
        return data
