import os
import re
from tkinter import *
import tkinter as tk
from tkinter import ttk,messagebox,filedialog
from PIL import ImageTk,Image
import ControlBook_View
from Connect_MSSQL import Connect_DB

class AddBookView(tk.Frame):
	def __init__(self, master):
		super().__init__(master)
		self.book = None

		self.canvas = Canvas(self.master, bg = "#FFFFFF", height = 900, width = 1500, bd = 0, highlightthickness = 0, relief = "ridge")
		self.canvas.place(x = 0, y = 0)

		# Background
		self.img_background = PhotoImage(file = "./image/background.png")
		self.background = self.canvas.create_image(750.0, 450.0, image = self.img_background)

		# Logo
		self.img_logo = PhotoImage(file = "./image/logo.png")
		self.logo = self.canvas.create_image(320.0, 95.0, image = self.img_logo)
		
		self.img_bg_upload = PhotoImage(file = "./image/Admin/sach/bg_upload.png")
		self.bg_upload = self.canvas.create_image(1109.0, 467.0, image = self.img_bg_upload)

		self.img_bg_infosach = PhotoImage(file = "./image/Admin/sach/bg_infosach.png")
		self.bg_infosach = self.canvas.create_image(430.0, 457.0, image = self.img_bg_infosach)

		self.img_button_upload = PhotoImage(file = "./image/Admin/sach/upload.png")
		self.button_upload = Button(image = self.img_button_upload, borderwidth = 0, highlightthickness = 0, command = lambda: self.open_file_dialog(), relief = "flat")
		self.button_upload.place(x = 1059.0, y = 417.0, width = 100.0, height = 100.0)

		self.canvas.create_text(963.0, 39.0, anchor = "nw", text = "Thêm sách", fill = "#00054B", font = ("PlayfairDisplay Regular", 60 * -1))

		self.canvas.create_text(582.0, 648.0, anchor = "nw", text = "VND", fill = "#555454", font = ("RobotoRoman Bold", 30 * -1))

		self.img_entry_giaban = PhotoImage(file = "./image/Admin/sach/entry_2.png")
		self.canvas.create_text(194.0, 648.0, anchor = "nw", text = "Giá bán", fill = "#555454", font = ("RobotoRoman Bold", 30 * -1))
		self.entry_bg_giaban = self.canvas.create_image(468.0, 666.0, image = self.img_entry_giaban)
		self.entry_giaban = Entry(bd = 0, bg = "#E3E3E3", fg = "#000716", highlightthickness = 0, font = ("Arial", 18))
		self.entry_giaban.place(x = 378.0, y = 646.0, width = 180.0, height = 38.0)

		self.img_entry = PhotoImage(file = "./image/Admin/sach/entry_1.png")

		self.canvas.create_text(195.0, 298.0, anchor = "nw", text = "Tác giả", fill = "#555454", font = ("RobotoRoman Bold", 30 * -1))
		self.img_entry_tacgia = self.canvas.create_image(513.0, 316.0, image = self.img_entry)
		self.entry_tacgia = Entry(bd = 0, bg = "#E3E3E3", fg = "#000716", highlightthickness = 0, font = ("Arial", 18))
		self.entry_tacgia.place(x = 378.0, y = 296.0, width = 270.0, height = 38.0)

		self.canvas.create_text(194.0, 438.0, anchor = "nw", text = "Năm XB", fill = "#555454", font = ("RobotoRoman Bold", 30 * -1))
		self.img_entry_namxb = self.canvas.create_image(513.0, 456.0, image = self.img_entry)
		self.entry_namxb = Entry(bd = 0, bg = "#E3E3E3", fg = "#000716", highlightthickness = 0, font = ("Arial", 18))
		self.entry_namxb.place(x = 378.0, y = 436.0, width = 270.0, height = 38.0)

		self.canvas.create_text(194.0, 508.0, anchor = "nw", text = "Thể loại", fill = "#555454", font = ("RobotoRoman Bold", 30 * -1))
		itemsTheLoai = self.loadTheLoaiFromDB()
		self.itemTL_string = StringVar(value = itemsTheLoai[0])
		comboTL = ttk.Combobox(self.master, textvariable = self.itemTL_string)
		comboTL['values'] = itemsTheLoai
		comboTL.place(x = 368.0, y = 506.0)
		comboTL['width'] = 20
		comboTL['height'] = 50
		comboTL['font'] = ('Arial', 18)

		self.canvas.create_text(194.0, 578.0, anchor = "nw", text = "Vị trí", fill = "#555454", font = ("RobotoRoman Bold", 30 * -1))
		itemsViTri = ('K1','K2','K3','K4','K5','K6','K7','K8','K9','K10','K11','K12','K13')
		self.itemVT_string = StringVar(value = itemsViTri[0])
		comboVT = ttk.Combobox(self.master, textvariable = self.itemVT_string)
		comboVT['values'] = itemsViTri
		comboVT.place(x = 368.0, y = 576.0)
		comboVT['width'] = 20
		comboVT['height'] = 50
		comboVT['font'] = ('Arial', 18)

		self.canvas.create_text(194.0, 368.0, anchor = "nw", text = "Nhà XB", fill = "#555454", font = ("RobotoRoman Bold", 30 * -1))
		self.img_entry_nhaxb = self.canvas.create_image(513.0, 386.0, image = self.img_entry)
		self.entry_nhaxb = Entry(bd = 0, bg = "#E3E3E3", fg = "#000716", highlightthickness = 0, font = ("Arial", 18))
		self.entry_nhaxb.place(x = 378.0, y = 366.0, width = 270.0, height = 38.0)

		self.canvas.create_text(195.0, 228.0, anchor = "nw", text = "Tên sách", fill = "#555454", font = ("RobotoRoman Bold", 30 * -1))
		self.img_entry_tensach = self.canvas.create_image(513.0, 246.0, image = self.img_entry)
		self.entry_tensach = Entry(bd = 0, bg = "#E3E3E3", fg = "#000716", highlightthickness = 0, font = ("Arial", 18))
		self.entry_tensach.place(x = 378.0, y = 226.0, width = 270.0, height = 38.0)

		self.img_button_themsach = PhotoImage(file = "./image/Admin/sach/addsach.png")
		self.button_themsach = Button(image = self.img_button_themsach, borderwidth = 0, highlightthickness = 0, command = lambda: self.getInfo(), relief = "flat")
		self.button_themsach.place(x = 533.0, y = 776.0, width = 200.0, height = 68.0)

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
	
	def insertDB(self,query):
		database = Connect_DB.MSSQLConnection()
		database.connect()
		database.insert(query)
		database.close()

	def loadTheLoaiFromDB(self):
		lstTheLoai = []
		query = "SELECT TenTheLoai FROM TheLoai"
		lst = self.loadFromDB(query)
		for i in lst:
			i = list(i)
			lstTheLoai.append(i[0])
		return lstTheLoai
	
	def getMaSach(self):
		query = "SELECT Id_Sach FROM Sach"
		data = self.loadFromDB(query)
		if data == []:
			return 'B0000'
		else:
			for i in data:
				i = list(i)
				i[0] = i[0].strip()
			maSachCu = data[len(data)-1][0]
			maSach = int(maSachCu[1:]) + 1
			maSachMoi = f'{maSachCu[:2]}{maSach:04}'
			return maSachMoi
		
	def getInfo(self):
		self.masach = self.getMaSach()
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
		listupdate = [self.masach,tensach,tacgia,nhaxb,namxb,matheloai,vịtri,giaban]
		for i in listupdate:
			if i == '':
				messagebox.showwarning("Warning", "Thông tin sách không được bỏ trống.")
				return False
		self.addBook(listupdate)
	
	def addBook(self,lst):
		if self.book:
			infoBook = lst
			query = f"""INSERT INTO Sach VALUES ('{infoBook[0]}',N'{infoBook[1]}',N'{infoBook[2]}',N'{infoBook[3]}',{infoBook[4]},'{infoBook[5]}','{infoBook[6]}','{infoBook[7]}')"""
			self.insertDB(query)
			self.save_img()
			lstEntry = [self.entry_giaban,self.entry_tensach,self.entry_nhaxb,self.entry_namxb,self.entry_tacgia]
			for entry in lstEntry:
				entry.delete(0, END)
			self.upload_book.destroy()
			self.img_bg_upload = PhotoImage(file = "./image/Admin/sach/bg_upload.png")
			self.bg_upload = self.canvas.create_image(1109.0, 467.0, image = self.img_bg_upload)
			messagebox.showinfo("Thông báo", "Sách đã được thêm thành công!")
		else:
			messagebox.showwarning("Warning", "Vui lòng tải lên hình ảnh của sách")
			return False

	def open_file_dialog(self):
		img_path = filedialog.askopenfilename(initialdir = os.getcwd(), title = "Select an Image", filetypes = [("PNG file", "*.png")])
		if img_path:
			img_book = Image.open(img_path)
			img_book = img_book.resize((500, 660), Image.ANTIALIAS)
			self.book = img_book
			img_book = ImageTk.PhotoImage(img_book)
			if self.bg_upload:
				self.canvas.delete(self.bg_upload)
			self.upload_book = Label(self.master)
			self.upload_book.place(x = 859, y = 137)
			self.upload_book.configure(image = img_book)
			self.upload_book.image = img_book
		
	def save_img(self):
		self.book.save(f"./image/image_book/{self.masach}.png")

	
