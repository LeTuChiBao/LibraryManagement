import re
from tkinter import *
import tkinter as tk
from tkinter import ttk,messagebox
from datetime import datetime 
from Connect_MSSQL import Connect_DB
import ControlBook_View

class UpdateBookView(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.listsach = None

        self.canvas = Canvas(self.master, bg = "#FFFFFF", height = 900, width = 1500, bd = 0, highlightthickness = 0, relief = "ridge")
        self.canvas.place(x = 0, y = 0)

        # Background
        self.img_background = PhotoImage(file = "./image/background.png")
        self.background = self.canvas.create_image(750.0, 450.0, image = self.img_background)

        # Logo
        self.img_logo = PhotoImage(file = "./image/logo.png")
        self.logo = self.canvas.create_image(320.0, 95.0, image = self.img_logo)

        self.img_bg_update = PhotoImage(file = "./image/Admin/sach/bg_update.png")
        self.bg_update = self.canvas.create_image(1053.0, 455.0, image = self.img_bg_update)

        self.img_button_timkiem = PhotoImage(file = "./image/Admin/sach/timkiem.png")
        self.button_timkiem = Button(image = self.img_button_timkiem, borderwidth = 0, highlightthickness = 0, command = lambda: self.checkID(), relief = "flat")
        self.button_timkiem.place(x = 1215.0, y = 230.0, width = 40.0, height = 40.0)

        self.canvas.create_text(963.0, 176.0, anchor = "nw", text = "Nhập ID Sách ", fill = "#555454", font = ("RobotoRoman Bold", 30 * -1))


        self.canvas.create_text(864.0, 54.0, anchor = "nw", text = "Cập nhật sách", fill = "#00054B", font = ("PlayfairDisplay Regular", 60 * -1))

        self.canvas.create_text(1204.0, 684.0, anchor = "nw", text = "VND", fill = "#555454", font = ("RobotoRoman Bold", 30 * -1))

        self.img_entry_2 = PhotoImage(file = "./image/Admin/sach/entry_2.png")

        self.canvas.create_text(838.0, 687.0, anchor = "nw", text = "Giá bán", fill = "#555454", font = ("RobotoRoman Bold", 30 * -1))
        self.entry_bg_giaban = self.canvas.create_image(1090.0, 702.0, image = self.img_entry_2)
        self.entry_giaban = Entry(bd = 0, bg = "#E3E3E3", fg = "#000716", highlightthickness = 0, font = ("Arial", 18))
        self.entry_giaban.place(x = 1000.0, y = 682.0, width = 180.0, height = 38.0)


        self.img_button_capnhat = PhotoImage(file = "./image/Admin/sach/capnhat.png")
        self.button_capnhat = Button(image = self.img_button_capnhat, borderwidth = 0, highlightthickness = 0, command = lambda: self.getInfo(), relief = "flat")
        self.button_capnhat.place(x = 973.0, y = 783.0, width = 200.0, height = 68.0)


        self.img_entry_1 = PhotoImage(file = "./image/Admin/sach/entry_1.png")

        self.canvas.create_text(839.0, 362.0, anchor = "nw", text = "Tác giả", fill = "#555454", font = ("RobotoRoman Bold", 30 * -1))
        self.entry_bg_tacgia = self.canvas.create_image(1135.0, 377.0, image = self.img_entry_1)
        self.entry_tacgia = Entry(bd = 0, bg = "#E3E3E3", fg = "#000716", highlightthickness = 0, font = ("Arial", 18))
        self.entry_tacgia.place(x = 1000.0, y = 357.0, width = 270.0, height = 38.0)



        self.canvas.create_text(838.0, 492.0, anchor = "nw", text = "Năm XB", fill = "#555454", font = ("RobotoRoman Bold", 30 * -1))
        self.entry_bg_namxb = self.canvas.create_image(1135.0, 507.0, image = self.img_entry_1)
        self.entry_namxb = Entry(bd = 0, bg = "#E3E3E3", fg = "#000716", highlightthickness = 0, font = ("Arial", 18))
        self.entry_namxb.place(x = 1000.0, y = 487.0, width = 270.0, height = 38.0)


        self.canvas.create_text(839.0, 557.0, anchor = "nw", text = "Thể loại", fill = "#555454", font = ("RobotoRoman Bold", 30 * -1))
        itemsTheLoai = self.loadTheLoaiFromDB()
        self.itemTL_string = StringVar(value = itemsTheLoai[0])
        comboTL = ttk.Combobox(self.master, textvariable = self.itemTL_string)
        comboTL['values'] = itemsTheLoai
        comboTL.place(x = 990.0, y = 555.0)
        comboTL['width'] = 20
        comboTL['height'] = 50
        comboTL['font'] = ('Arial', 18)

        self.canvas.create_text(839.0, 622.0, anchor = "nw", text = "Vị trí", fill = "#555454", font = ("RobotoRoman Bold", 30 * -1))
        itemsViTri = ('K1','K2','K3','K4','K5','K6','K7','K8','K9','K10','K11','K12','K13')
        self.itemVT_string = StringVar(value = itemsViTri[0])
        comboVT = ttk.Combobox(self.master, textvariable = self.itemVT_string)
        comboVT['values'] = itemsViTri
        comboVT.place(x = 990.0, y = 620.0)
        comboVT['width'] = 20
        comboVT['height'] = 50
        comboVT['font'] = ('Arial', 18)


        self.canvas.create_text(840.0, 427.0, anchor = "nw", text = "Nhà XB", fill = "#555454", font = ("RobotoRoman Bold", 30 * -1))
        self.entry_bg_nhaxb = self.canvas.create_image(1135.0, 442.0, image = self.img_entry_1)
        self.entry_nhaxb = Entry(bd = 0, bg = "#E3E3E3", fg = "#000716", highlightthickness = 0, font = ("Arial", 18))
        self.entry_nhaxb.place(x = 1000.0, y = 422.0, width = 270.0, height = 38.0)

        self.canvas.create_text(839.0, 232.0, anchor = "nw", text = "ID Sách", fill = "#555454", font = ("RobotoRoman Bold", 30 * -1))
        self.entry_bg_masach = self.canvas.create_image(1090.0, 247.0, image = self.img_entry_2)
        self.entry_masach = Entry(bd = 0, bg = "#E3E3E3", fg = "#000716", highlightthickness = 0, font = ("Arial", 18))
        self.entry_masach.place(x = 1000.0, y = 227.0, width = 180.0, height = 38.0)

        self.canvas.create_text(839.0, 297.0, anchor = "nw", text = "Tên sách", fill = "#555454", font = ("RobotoRoman Bold", 30 * -1))
        self.entry_bg_tensach = self.canvas.create_image(1135.0, 312.0, image = self.img_entry_1)
        self.entry_tensach = Entry(bd = 0, bg = "#E3E3E3", fg = "#000716", highlightthickness = 0, font = ("Arial", 18))
        self.entry_tensach.place(x = 1000.0, y = 292.0, width = 270.0, height = 38.0)

        self.img_bg_update1 = PhotoImage(file = "./image/Admin/sach/bg_update1.png")
        self.bg_update1 = self.canvas.create_image(401.0, 480.0, image = self.img_bg_update1)

        # Button comback
        self.img_comeback = PhotoImage(file = "./image/comeback.png")
        self.button_comeback = Button(image = self.img_comeback, borderwidth = 0, highlightthickness = 0, command = lambda: self.prevControlBook(), relief = "flat")
        self.button_comeback.place(x = 49.0,  y = 776.0, width = 271.0, height = 75.0)

    def prevControlBook(self):
        self.destroy()
        ControlBook_View.ControlBookView(self.master)

    def loadFromDB(self,query):
        database = Connect_DB.MSSQLConnection()
        database.connect()
        data = database.query(query)
        database.close()
        return data
	
    def queryUpdateDB(self,query):
        database = Connect_DB.MSSQLConnection()
        database.connect()
        database.update(query)
        database.close()

    def loadTheLoaiFromDB(self):
        lstTheLoai = []
        query = "SELECT TenTheLoai FROM TheLoai"
        lst = self.loadFromDB(query)
        for i in lst:
            i = list(i)
            lstTheLoai.append(i[0])
        return lstTheLoai

    def listSach(self):
        lstSach = []
        query = """SELECT *,Theloai.TenTheLoai FROM Sach INNER JOIN TheLoai ON TheLoai.Id_TheLoai = Sach.Id_TheLoai"""
        data = self.loadFromDB(query)
        for i in data:
            i = list(i)
            i[0] = i[0].strip()
            lstSach.append(i)
        return lstSach
       
    def checkID(self):
        lstEntry = [self.entry_giaban,self.entry_tensach,self.entry_nhaxb,self.entry_namxb,self.entry_tacgia]
        
        for entry in lstEntry:
            entry.delete(0, END)
        self.listsach = self.listSach()
        masach = self.entry_masach.get()
        masach = masach.upper()
        for i in self.listsach:
            if masach == i[0]:
                self.entry_giaban.insert(0, i[7])
                self.entry_tacgia.insert(0, i[2])
                self.entry_namxb.insert(0, i[4])
                self.entry_theloai = i[9]
                self.entry_tensach.insert(0, i[1])
                self.entry_vitri = i[6]
                self.itemVT_string.set(self.entry_vitri)
                self.entry_nhaxb.insert(0, i[3])
                self.itemTL_string.set(self.entry_theloai)
                break
        else:
            messagebox.showwarning("Warning", "Mã sách không tồn tại!")
        
    def getInfo(self):
        self.masach = self.entry_masach.get()
        self.masach = self.masach.upper()
        tensach = self.entry_tensach.get()
        tacgia = self.entry_tacgia.get()
        if "'" in tacgia:
            tacgia = re.sub(r"'", "''", tacgia)
        nhaxb = self.entry_nhaxb.get()
        if "'" in nhaxb:
            nhaxb = re.sub(r"'", "''", nhaxb)
        namxb = self.entry_namxb.get()
        if not namxb.isdigit():
            messagebox.showwarning("Warning", "Năm xuất bản không đúng, vui lòng thử lại.")
            return False
        namxb = int(namxb)
        tentheloai = self.itemTL_string.get()
        queryTL = f"SELECT Id_TheLoai FROM TheLoai WHERE TenTheLoai = N'{tentheloai}'"
        matheloai = self.loadFromDB(queryTL)
        matheloai = list(matheloai[0])
        matheloai = matheloai[0].strip()
        vịtri = self.itemVT_string.get()
        giaban = self.entry_giaban.get()
        listupdate = [tensach,tacgia,nhaxb,namxb,matheloai,vịtri,giaban]
        for i in listupdate:
            if i == '':
                messagebox.showwarning("Warning", "Thông tin sách không được bỏ trống.")
                return False
        self.updateBook(listupdate)

    def updateBook(self,listupdate):
        infoBook = listupdate
        query = f"""UPDATE Sach SET TenSach = N'{infoBook[0]}',TenTacGia = N'{infoBook[1]}',NhaXB = N'{infoBook[2]}', NamXB = {infoBook[3]}, Id_TheLoai = '{infoBook[4]}', TenKe = '{infoBook[5]}', GiaSach = '{infoBook[6]}'  WHERE Id_Sach = '{self.masach}';"""
        self.queryUpdateDB(query)
        lstEntry = [self.entry_masach,self.entry_giaban,self.entry_tensach,self.entry_nhaxb,self.entry_namxb,self.entry_tacgia]
        for entry in lstEntry:
            entry.delete(0, END)
        messagebox.showinfo("Thông báo", "Sách đã được cập nhật thành công!")