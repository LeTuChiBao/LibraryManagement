import re
from tkinter import *
import tkinter as tk
from tkinter import ttk,messagebox
from Connect_MSSQL import Connect_DB
from PIL import ImageTk
from datetime import datetime
from tkcalendar import Calendar

class IssueBookView(tk.Frame):
    def __init__(self,master,user):
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

        self.image_op1 = PhotoImage(file = "./image/Users/muonsach/op1.png")
        self.op1 = self.canvas.create_image(750.0, 331.0, image = self.image_op1)

        self.image_op2 = PhotoImage(file = "./image/Users/muonsach/op2.png")
        self.op2 = self.canvas.create_image(750.0, 620.0, image = self.image_op2)

        self.img_select = PhotoImage(file = "./image/Users/muonsach/select_book.png")
        self.button_select = Button(image = self.img_select, borderwidth = 0, highlightthickness = 0, command = lambda: self.loadTable(), relief = "flat")
        self.button_select.place(x = 1031.0, y = 300.0, width = 182.0, height = 68.0)

        self.img_issue = PhotoImage(file = "./image/Users/muonsach/issue_book.png")
        self.button_issue = Button(image = self.img_issue, borderwidth = 0, highlightthickness = 0, command = lambda: self.confirm_continue(), relief = "flat")
        self.button_issue.place(x = 1116.0, y = 783.0, width = 238.0,height = 68.0)

        self.img_entry = PhotoImage(file = "./image/Users/muonsach/entry.png")
        # Nhập Id sách
        self.canvas.create_text(209.0, 232.0, anchor = "nw", text = "Mã Sách", fill="#555454", font = ("RobotoRoman Bold", 30 * -1))
        self.img_entry_masach = self.canvas.create_image(491.5, 250.0, image = self.img_entry )
        self.entry_masach = Entry(bd = 0, bg = "#E3E3E3", fg = "#000716", highlightthickness = 0, font = ("Tahoma", 18))
        self.entry_masach.place(x = 410.0, y = 230.0, width = 180.0, height = 38.0)
        # Nhập ngày mượn
        self.canvas.create_text(209.0, 307.0, anchor = "nw", text = "Ngày Mượn", fill = "#555454", font = ("RobotoRoman Bold", 30 * -1))
        self.img_entry_ngaymuon = self.canvas.create_image(491.5, 325.0, image = self.img_entry )
        self.entry_ngaymuon = Entry(bd = 0, bg = "#E3E3E3", fg = "#000716", highlightthickness = 0, font = ("Tahoma", 18))
        self.entry_ngaymuon.place(x = 410.0, y = 305.0, width = 180.0, height = 38.0)
        # Nhập ngày trả
        self.canvas.create_text(209.0, 382.0, anchor = "nw", text = "Ngày Trả", fill = "#555454", font = ("RobotoRoman Bold", 30 * -1))
        self.img_entry_ngaytra = self.canvas.create_image(491.5, 400.0, image = self.img_entry )
        self.entry_ngaytra = Entry(bd = 0, bg = "#E3E3E3", fg = "#000716", highlightthickness = 0, font = ("Tahoma", 18))
        self.entry_ngaytra.place(x = 410.0, y = 380.0, width = 180.0, height = 38.0)
        # Nhập ghi chú
        self.canvas.create_text(830.0, 232.0, anchor = "nw", text = "Ghi Chú", fill = "#555454", font = ("RobotoRoman Bold", 30 * -1))
        self.img_note = PhotoImage(file = "./image/Users/muonsach/entry_note.png")
        self.img_entry_note = self.canvas.create_image(1122.0, 250.0, image = self.img_note)
        self.entry_note = Entry(bd = 0, bg = "#E3E3E3", fg = "#000716", highlightthickness = 0,  font = ("Tahoma", 18))
        self.entry_note.place(x = 1000.0, y = 230.0, width = 262.0, height = 40.0)

        self.img_calendar = PhotoImage(file = "./image/Users/muonsach/calendar.png")
        # Calendar ngày trả
        self.calendar_1 = Button(image = self.img_calendar, borderwidth = 0, highlightthickness = 0, command = lambda: self.calendar(self.entry_ngaymuon), relief = "flat")
        self.calendar_1.place(x = 618.0, y = 305.0, width = 40.0, height = 40.0)
        # Calendar ngày mượn
        self.calendar_2 = Button(image = self.img_calendar, borderwidth = 0, highlightthickness = 0, command = lambda: self.calendar(self.entry_ngaytra), relief = "flat")
        self.calendar_2.place(x = 618.0, y = 380.0, width = 40.0, height = 40.0)

        # Bảng liệt kê sách mượn
        self.table = ttk.Treeview(self.master, show = 'headings', padding = "10px")
        style = ttk.Style()
        style.configure("Treeview", font=("Tahoma", 10))
        self.table.place(x = 150, y = 495, height = 250, width = 1200)
        self.table['columns'] = ('Id_Phieu', 'Id_Sach','TenSach', 'TacGia', 'NgayMuon', 'NgayTra','PhiMuon','GhiChu')
        self.table.column('Id_Phieu', width = 22, anchor = 'center')
        self.table.column('Id_Sach', width = 10, anchor = 'center')
        self.table.column('TenSach', width = 250, anchor = 'w')
        self.table.column('TacGia', width = 110, anchor = 'w')
        self.table.column('NgayMuon', width = 50, anchor = 'center')
        self.table.column('NgayTra', width = 50, anchor = 'center')
        self.table.column('PhiMuon', width = 50, anchor = 'center')
        self.table.column('GhiChu', width = 50, anchor = 'center')
        self.table.heading('Id_Phieu', text = 'Mã phiếu mượn')
        self.table.heading('Id_Sach', text = 'Mã Sách')
        self.table.heading('TenSach', text = 'Tên Sách')
        self.table.heading('TacGia', text = 'Tác Giả')
        self.table.heading('NgayMuon', text = 'Ngày mượn')
        self.table.heading('NgayTra', text = 'Ngày trả')
        self.table.heading('PhiMuon', text = 'Phí')
        self.table.heading('GhiChu', text = 'Ghi Chú')

        scrollbar_table = ttk.Scrollbar(self.table, orient = 'vertical', command = self.table.yview)
        self.table.configure(yscrollcommand = scrollbar_table.set)
        scrollbar_table.place(relx = 1, rely = 0, relheight = 1, anchor = 'ne')

        # Button Comeback
        self.img_comeback = PhotoImage(file = "./image/comeback.png")
        self.button_comeback = Button(image = self.img_comeback, borderwidth = 0, highlightthickness = 0, command = lambda: self.prevHomeUser(), relief = "flat")
        self.button_comeback.place(x = 111.0, y = 783.0, width = 271.0, height = 75.0)

    def prevHomeUser(self):
        self.master.prevHomeUser()

    def calendar(self,entry):
        top = Toplevel(self.master)
        top.geometry("+900+370")
        top.overrideredirect(True)
        top.iconphoto(True, ImageTk.PhotoImage(file = "./image/Users/muonsach/logo_error.png"))
        def set_value(e):
            selected_date = cal.get_date()
            current_date = datetime.now().date()
            selected_datetime = datetime.strptime(selected_date,'%d/%m/%Y').date()
            if selected_datetime < current_date:
                messagebox.showwarning("Warning", "Vui lòng chọn ngày sau ngày hiện tại!")
            else:
                entry.delete(0, tk.END)
                entry.insert(0, selected_date)
                top.destroy()
        cal = Calendar(top, selectmode = 'day', date_pattern = 'dd/MM/yyyy')
        cal.pack(padx = 5, pady = 5)
        cal.bind("<<CalendarSelected>>", set_value)

    def checkInput(self,maSach,ngayMuon,ngayTra):
        regexSach = r'^[Bb]\d{5}$'
        regexNgay = r'^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}$'
        if not re.match(regexSach, maSach):
            messagebox.showwarning("Warning", "Mã sách không đúng! Vui lòng nhập lại.")
            return None
        elif ngayMuon == '' or ngayTra == '' or not re.match(regexNgay, ngayMuon) or not re.match(regexNgay, ngayTra):
            messagebox.showwarning("Warning", "Ngày mượn hoặc ngày trả không đúng! Vui lòng nhập lại.")
            return None
        else:
            return True

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
    
    def getPhieuMuon(self):
        query = """SELECT Id_PhieuMuon FROM PhieuMuon"""
        data = self.loadFromDB(query)
        if data == []:
            return 'PM0000'
        else:
            for i in data:
                i = list(i)
                i[0] = i[0].strip()
            return data[len(data)-1][0]
        
    def getBook(self,id):
        query = f"""SELECT Id_Sach,TenSach,TenTacGia,GiaSach FROM Sach
                    WHERE Id_Sach = '{id}'"""
        data = self.loadFromDB(query)
        data = list(data[0])
        data[0] = data[0].strip()
        return data
    
    def getUser(self,id):
        query = f"""SELECT Id_NguoiDung,VaiTro FROM NguoiDung
                    WHERE Id_NguoiDung = '{id}'"""
        data = self.loadFromDB(query)
        data = list(data[0])
        data[0] = data[0].strip()
        return data
    
    def selectBook(self):
        maSach = self.entry_masach.get()
        ngayMuon = self.entry_ngaymuon.get()
        ngayTra = self.entry_ngaytra.get()
        if self.checkInput(maSach,ngayMuon,ngayTra) is None:
            return False
        else:
            ghiChu = self.entry_note.get()
            if ghiChu == '':
                ghiChu = 'Không'
            maPhieuCu = self.getPhieuMuon()
            maPhieu = int(maPhieuCu[2:]) + 1
            maPhieuMoi = f'{maPhieuCu[:2]}{maPhieu:04}'
            Sach = self.getBook(maSach)
            tenSach = Sach[1]
            tenTacGia = Sach[2]
            giaBan = Sach[3]
            Vaitro = self.getUser(self.user)[1]
            if Vaitro == 'Sinh viên' or Vaitro == 'Giảng viên':
                phiMuon = 'Miễn phí'
            else:
                phiMuon = int(giaBan) * 0.5
                phiMuon = "{:,.0f} VND".format(phiMuon)
            lst = [(maPhieuMoi,maSach.upper(),tenSach,tenTacGia,ngayMuon,ngayTra,phiMuon,ghiChu)]
            return lst
    
    def loadTable(self):
        if self.selectBook() is False:
            return
        lst = self.selectBook()
        column_values = []
        for i in self.table.get_children():
            value = self.table.item(i, 'values')
            column_values.append(value[self.table['columns'].index('Id_Sach')])
        if lst[0][1] not in column_values:
            self.table.insert('','end', values = lst[0])
        else:
            messagebox.showwarning("Warning","Mã sách này đã được chọn!")
            return False

    def confirm_continue(self):
        if self.table.get_children():
            result = messagebox.askyesno("Xác nhận", "Bạn có muốn tiếp tục không?")
            if result:
                self.queryUpdate()  # Thực thi hàm khi người dùng chọn Có
            else:
                pass  # Không làm gì khi người dùng chọn Không
        else:
            messagebox.showwarning("Cảnh báo", "Bạn chưa lựa chọn sách, không thể tiếp tục!")

    def queryUpdate(self):
        phieuMuon = []
        maPhieu = self.table.item(self.table.get_children()[0])['values'][0]
        chiTietPhieuMuon = []
        tongPhiMuon = 0
        for i in self.table.get_children():
            value = self.table.item(i,'values')
            idsach = value[1]
            ngayMuon = value[4]
            ngayTra = value[5]
            soNgayMuon = (datetime.strptime(ngayTra, '%d/%m/%Y') - datetime.strptime(ngayMuon, '%d/%m/%Y')).days
            phiMuon = value[6]
            if phiMuon != 'Miễn phí':
                phiMuon = ''.join(filter(str.isdigit, phiMuon))
                tongPhiMuon += int(phiMuon)
            else:
                tongPhiMuon = 'Miễn phí'
            ghiChu = value[7]
            trangthai = 'Đã mượn'
            chiTietPhieuMuon.append([maPhieu,idsach,ngayMuon,ngayTra,soNgayMuon,str(phiMuon),ghiChu,trangthai])
        # Xử lý chuỗi phieuMuon
        l1 = [maPhieu,self.user,str(tongPhiMuon)]
        for i in l1:
            phieuMuon.append(i)
        # Xử lý chuỗi chiTietPhieuMuon
        values = ''
        for i in chiTietPhieuMuon:
            values += f"('{i[0]}','{i[1]}','{i[2]}','{i[3]}','{i[4]}',N'{i[5]}',N'{i[6]}',N'{i[7]}'),"
        values = values[:-1]
        # Trả về 2 chuỗi query
        queryPhieuMuon = f"""INSERT INTO PhieuMuon VALUES ('{phieuMuon[0]}','{phieuMuon[1]}',N'{phieuMuon[2]}')"""
        self.insertDB(queryPhieuMuon)
        queryChiTietPhieuMuon = """INSERT INTO ChiTietPhieuMuon VALUES """ + values
        self.insertDB(queryChiTietPhieuMuon)
        messagebox.showinfo("Thông báo", """Bạn đã đặt sách thành công! Vui lòng liên hệ quản lí thư viện để nhận sách.""")

        # Xóa toàn bộ dữ liệu trong self.table
        self.table.delete(*self.table.get_children())
        