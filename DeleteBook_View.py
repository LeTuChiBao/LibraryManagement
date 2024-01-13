import os
from tkinter import *
import tkinter as tk
from tkinter import ttk,messagebox
from Connect_MSSQL import Connect_DB
import ControlBook_View

class DeleteBookView(tk.Frame):
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

        self.img_bg_delete = PhotoImage(file = "./image/Admin/sach/bg_delete.png")
        self.bg_delete = self.canvas.create_image(750.0, 443.0, image = self.img_bg_delete)

        self.img_button_delete = PhotoImage(file = "./image/Admin/sach/deletesach.png")
        self.button_delete = Button(image = self.img_button_delete, borderwidth = 0, highlightthickness = 0, command = lambda: self.delbook(), relief = "flat")
        self.button_delete.place(x = 650.0, y = 577.0, width = 200.0, height = 68.0)

        self.img_entry_delete = PhotoImage(file = "./image/Admin/sach/entry_delete.png")
        self.entry_bg_delete = self.canvas.create_image(750.0, 458.0, image = self.img_entry_delete)
        self.entry_delete = Entry(bd = 0, bg = "#FFFFFF", fg = "#000716", highlightthickness = 0, font = ("Arial", 18), justify = 'center')
        self.entry_delete.place(x = 615.0, y = 439.0, width = 270.0, height = 38.0)

        self.canvas.create_text(605.0, 379.0, anchor = "nw", text = "Nhập ID Sách cần xóa", fill = "#555454", font = ("RobotoRoman Bold", 30 * -1))

        # Button comback
        self.img_comeback = PhotoImage(file = "./image/comeback.png")
        self.button_comeback = Button(image = self.img_comeback, borderwidth = 0, highlightthickness = 0, command = lambda: self.prevControlBook(), relief = "flat")
        self.button_comeback.place(x = 49.0, y = 776.0, width = 271.0, height = 75.0)

    def prevControlBook(self):
        self.destroy()
        ControlBook_View.ControlBookView(self.master)

    def loadFromDB(self,query):
        database = Connect_DB.MSSQLConnection()
        database.connect()
        data = database.query(query)
        database.close()
        return data
    
    def deleteDB(self,query):
        database = Connect_DB.MSSQLConnection()
        database.connect() 
        database.delete(query)
        database.close()
        return True
    
    def getMaSach(self):
        listsach = []
        query = "SELECT Id_Sach FROM Sach"
        data = self.loadFromDB(query)
        for i in data:
            i = list(i)
            i[0] = i[0].strip()
            listsach.append(i[0])
        return listsach
    
    def delbook(self):
        listsach = self.getMaSach()
        idsach = self.entry_delete.get()
        idsach = idsach.upper()
        for i in listsach:
            if i == idsach:
                query = f"DELETE FROM Sach WHERE Id_Sach = '{idsach}'"
                self.deleteDB(query)
                os.remove(f"./image/image_book/{i}.png")
                messagebox.showinfo("Thông báo", "Sách đã được xóa thành công!")
                break
        else:
            messagebox.showwarning("Warning", "Mã sách không tồn tại!")


