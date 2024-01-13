from tkinter import *
import tkinter as tk
from tkinter import ttk
from Connect_MSSQL import Connect_DB

class SearchBookView(tk.Frame):
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

        self.canvas.create_text(774.0, 50.0, anchor = "nw", text = "Tìm kiếm sách", fill = "#00054B", font = ("PlayfairDisplay Regular", 80 * -1))

        items = ('ID sách','Tên sách','Tác giả','Nhà xuất bản','Năm xuất bản','Thể loại')
        self.item_string = StringVar(value = items[0])
        combo = ttk.Combobox(self.master, textvariable = self.item_string)
        combo['values'] = items
        combo.place(x = 430, y = 199)
        combo['width'] = 12
        combo['height'] = 50
        combo['font'] = ('Arial', 18)
        combo.bind('<<ComboboxSelected>>', self.itemFillter)


        self.canvas.create_rectangle(100.0, 269.0, 1400.0, 769.0, fill = "#FFFFFF", outline = "")

        # Ô tìm kiếm
        self.img_entry = PhotoImage(file = "./image/Users/timkiemsach/entry.png")
        self.img_entry_search = self.canvas.create_image(816.0, 214.0, image = self.img_entry)
        self.entry = Entry(bd = 0, bg = "#E3E3E3", fg = "#000716", highlightthickness = 0, font = ("Arial", 18))
        self.entry.place(x = 625.0, y = 189.0, width = 382.0, height = 48.0)

        # Bảng filter
        self.table = ttk.Treeview(self.master, show = 'headings', padding = "10px")
        style = ttk.Style()
        style.configure("Treeview", font = ("Tahoma", 10))
        self.table.place(x = 100, y = 269, height = 500, width = 1300)
        self.table['columns'] = ('Id', 'TenSach', 'TacGia', 'NhaXB', 'NamXB', 'TheLoai', 'GiaBan')
        self.table.column('Id', width = 20, anchor = 'center')
        self.table.column('TenSach', width = 400, anchor = 'w')
        self.table.column('TacGia', width = 150, anchor = 'w')
        self.table.column('NhaXB', width = 170, anchor = 'w')
        self.table.column('NamXB', width = 50, anchor = 'center')
        self.table.column('TheLoai', width = 150, anchor = 'w')
        self.table.column('GiaBan', width = 100, anchor = 'e')

        self.table.heading('Id', text = 'Mã sách')
        self.table.heading('TenSach', text = 'Tên sách')
        self.table.heading('TacGia', text = 'Tác giả')
        self.table.heading('NhaXB', text = 'Nhà xuất bản')
        self.table.heading('NamXB', text = 'Năm xuất bản')
        self.table.heading('TheLoai', text = 'Thể loại')
        self.table.heading('GiaBan', text = 'Giá bán')
        self.data = self.loadFromDB()
        self.update(self.data)
        self.entry.bind('<KeyRelease>',self.check)
        scrollbar_table = ttk.Scrollbar(self.table, orient = 'vertical', command = self.table.yview)
        self.table.configure(yscrollcommand = scrollbar_table.set)
        scrollbar_table.place(relx = 1, rely = 0, relheight = 1, anchor = 'ne')

        # Quay về home
        self.img_comeback = PhotoImage(file = "./image/comeback.png")
        self.button_comeback = Button(image =  self.img_comeback, borderwidth = 0, highlightthickness = 0, command = lambda: self.prevHome(), relief = "flat")
        self.button_comeback.place(x = 70.0, y = 798.0, width = 271.0, height = 75.0)

    def prevHome(self):
        if self.user == 'admin':
            self.master.prevHomeAdmin()
        else:
            self.master.prevHomeUser()

    def loadFromDB(self):
        data = []
        database = Connect_DB.MSSQLConnection()
        database.connect()
        query = """SELECT Id_Sach,TenSach,TenTacGia,NhaXB,NamXB,TheLoai.TenTheLoai,GiaSach FROM Sach
                    INNER JOIN TheLoai ON Sach.Id_TheLoai = TheLoai.Id_TheLoai"""
        lst = database.query(query)
        database.close()
        for i in lst:
            i = list(i)
            i[0] = i[0].strip()
            i[6] = '{:,}'.format(int(i[6]))
            i[6] += ' VND'
            data.append(i)
        return data

    def update(self,data):
        for item in self.table.get_children():
            self.table.delete(item)
        for item in data:
            self.table.insert('', 'end', values = item)

    def check(self,e):
        typed = self.entry.get()
        item = self.itemFillter(e)
        if typed == '':
            self.update(self.data)
        else:
            lst = []
            for i in self.data:
                if item == 'ID sách':
                    a = 0
                elif item == 'Tên sách':
                    a = 1
                elif item == 'Tác giả':
                    a = 2
                elif item == 'Nhà xuất bản':
                    a = 3
                elif item == 'Năm xuất bản':
                    a = 4
                else:
                    a = 5
                if typed.lower() in str(i[a]).lower():
                    lst.append(i)
            self.update(lst)

    def itemFillter(self,e):
        return self.item_string.get()

