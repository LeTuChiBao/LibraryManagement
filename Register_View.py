import re
import Login_View
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import ttk,messagebox
from tkcalendar import Calendar
from datetime import datetime
from Connect_MSSQL import Connect_DB


class RegisterView(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('1225x550+300+250')
        self.iconbitmap('./image/Icon_Book_Library.ico')
        self.title('Library Management System')

        self.canvas = Canvas(self, bg = "#FFFFFF", height = 550, width = 1225, bd = 0, highlightthickness = 0, relief = "ridge")
        self.canvas.place(x = 0, y = 0)

        self.canvas.create_text(270.0, 30.0, anchor = "nw", text = "CREATE ACCOUNT", fill =  "#9377EE", font = ("RobotoRoman Bold", 40 * -1))
        self.entry_image = PhotoImage(file = './image/entry_register.png')

        self.canvas.create_text(109.0, 100.0, anchor = "nw", text = "Tên đăng nhập", fill = "#555454", font = ("RobotoRoman Bold", 16 * -1))
        self.entry_bg_1 = self.canvas.create_image(246.0, 144.0, image = self.entry_image)
        self.entry_1 = Entry(bd = 0, bg = "#E3E3E3", fg = "#000716", highlightthickness = 0, font = ("Tahoma", 16))
        self.entry_1.place(x = 120.0, y = 124.0, width = 261.0, height = 38.0)

        self.canvas.create_text(449.0, 100.0, anchor = "nw", text = "Mật khẩu", fill = "#555454", font = ("RobotoRoman Bold", 16 * -1))
        self.entry_bg_2 = self.canvas.create_image(586.0, 144.0, image = self.entry_image)
        self.entry_2 = Entry(bd = 0, bg = "#E3E3E3", fg = "#000716", highlightthickness = 0, font = ("Tahoma", 16), show = '●')
        self.entry_2.place(x = 460.0, y = 124.0, width = 261.0, height = 38.0)

        self.canvas.create_text(109.0, 187.0, anchor = "nw", text = "Họ và tên", fill = "#555454", font = ("RobotoRoman Bold", 16 * -1))
        self.entry_bg_3 = self.canvas.create_image(246.0, 231.0, image = self.entry_image)
        self.entry_3 = Entry(bd = 0, bg = "#E3E3E3", fg = "#000716", highlightthickness = 0, font = ("Tahoma", 16))
        self.entry_3.place(x = 120.0, y = 211.0, width = 261.0, height = 38.0)

        self.canvas.create_text(449.0, 187.0, anchor = "nw", text = "Ngày Sinh", fill = "#555454", font = ("RobotoRoman Bold", 16 * -1))
        self.entry_bg_4 = self.canvas.create_image(586.0, 231.0, image = self.entry_image)
        self.entry_4 = Entry(bd = 0, bg="#E3E3E3", fg = "#000716", highlightthickness = 0, font = ("Tahoma", 16))
        self.entry_4.place(x = 460.0, y = 211.0, width = 261.0, height = 38.0)

        self.canvas.create_text(109.0, 267.0, anchor = "nw", text = "Địa chỉ", fill = "#555454", font = ("RobotoRoman Bold", 16 * -1))
        self.entry_bg_5 = self.canvas.create_image(246.0, 311.0, image = self.entry_image)
        self.entry_5 = Entry(bd = 0, bg = "#E3E3E3", fg = "#000716", highlightthickness = 0, font = ("Tahoma", 16))
        self.entry_5.place(x = 120.0, y = 291.0, width = 261.0, height = 38.0)

        self.canvas.create_text(449.0, 267.0, anchor="nw", text = "Số điện thoại", fill="#555454", font=("RobotoRoman Bold", 16 * -1))
        self.entry_bg_6 = self.canvas.create_image(586.0, 311.0, image = self.entry_image)
        self.entry_6 = Entry(bd = 0, bg = "#E3E3E3", fg = "#000716", highlightthickness = 0, font = ("Tahoma", 16))
        self.entry_6.place(x = 460.0, y = 291.0, width = 261.0, height = 38.0)

        self.canvas.create_text(109.0, 347.0, anchor = "nw", text = "Giới tính", fill = "#555454", font = ("RobotoRoman Bold", 16 * -1))
        itemsGT = ('Nam','Nữ')
        self.item_stringGT = StringVar(value = itemsGT[0])
        comboGT = ttk.Combobox(self.master, textvariable = self.item_stringGT)
        comboGT['values'] = itemsGT
        comboGT.place(x = 101, y = 371)
        comboGT['width'] = 24
        comboGT['height'] = 50
        comboGT['font'] = ('Tahoma', 16)


        self.canvas.create_text(449.0, 347.0, anchor = "nw", text = "Bạn là", fill = "#555454", font = ("RobotoRoman Bold", 16 * -1))
        itemsVT = ('Sinh viên','Giảng viên','Người dùng khác')
        self.item_stringVT = StringVar(value = itemsVT[0])
        comboVT = ttk.Combobox(self.master, textvariable = self.item_stringVT)
        comboVT['values'] = itemsVT
        comboVT.place(x = 441, y = 371)
        comboVT['width'] = 24
        comboVT['height'] = 50
        comboVT['font'] = ('Tahoma', 16)

        self.img_button_calendar = PhotoImage(file = "./image/Users/nguoidung/calendar.png")
        self.button_calendar = Button(image = self.img_button_calendar, borderwidth = 0, highlightthickness = 0, command = lambda:  self.calendar(self.entry_4), relief = "flat")
        self.button_calendar.place(x = 750.0, y = 211.0, width = 40.0, height = 40.0)

        button_image_1 = PhotoImage(file = './image/button_create.png')
        self.button_1 = Button(image = button_image_1, borderwidth = 0, highlightthickness = 0, command = lambda: self.getInfoUser(), relief = "flat")
        self.button_1.place(x = 341.0, y = 425.0, width = 164.0, height = 40.0)

        self.canvas.create_text(260.0, 492.0, anchor = "nw", text = "Already have an account?", fill = "#555454", font = ("RobotoRoman Regular", 16 * -1))
        button_image_2 = PhotoImage(file = './image/button_login2.png')
        self.button_2 = Button(image = button_image_2, borderwidth = 0, highlightthickness = 0, command = lambda: self.nextLogin(), relief = "flat")
        self.button_2.place(x = 454.0, y = 488.0, width = 103.0, height = 26.0)

        image_image = PhotoImage(file = './image/Library_Register.png')
        self.image_1 = self.canvas.create_image(990.0, 254.0,image = image_image)
        self.resizable(False, False)
        self.mainloop()

    def nextLogin(self):
        self.destroy()
        Login_View.LoginView()

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

    def calendar(self, entry):
        top = tk.Toplevel(self)
        top.geometry("+1050+470")
        top.overrideredirect(True)
        top.iconphoto(True, tk.PhotoImage(file="./image/Users/muonsach/logo_error.png"))

        def set_value(e):
            selected_date = cal.get_date()
            selected_datetime = datetime.strptime(selected_date, '%d/%m/%Y').date()
            current_date = datetime.now().date()

            if selected_datetime >= current_date:
                messagebox.showwarning("Warning", "Vui lòng chọn lại!")
            else:
                entry.delete(0, tk.END)
                entry.insert(0, selected_date)
                top.destroy()
        cal = Calendar(top, selectmode='day', date_pattern='dd/MM/yyyy')
        cal.pack(padx=5, pady=5)
        cal.bind("<<CalendarSelected>>", set_value)

    def getIdMoi(self):
        query = "SELECT Id_NguoiDung FROM NguoiDung"
        data = self.loadFromDB(query)
        if data == []:
            return 'ND0000'
        else:
            for i in data:
                i = list(i)
                i[0] = i[0].strip()
            maSachCu = data[len(data)-1][0]
            maSach = int(maSachCu[2:]) + 1
            maSachMoi = f'{maSachCu[:2]}{maSach:05}'
            return maSachMoi
        
    def getTenDangNhap(self):
        lstTenDangNhap = []
        query = "SELECT TenDangNhap FROM DangNhap"
        data = self.loadFromDB(query)
        for i in data:
            i = list(i)
            lstTenDangNhap.append(i[0])
        return lstTenDangNhap
    
    def checkInput(self,ngaySinh):
        regexNgay = r'^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}$'
        if ngaySinh == '' or not re.match(regexNgay, ngaySinh):
            messagebox.showwarning("Warning", "Ngày sinh không hợp lệ! Vui lòng nhập lại.")
            return None
        else:
            return True
        
    def checkDN(self,string):
        pattern = r"""[àáảãạâầấẩẫậăằắẳẵặèéẻẽẹêềếểễệđìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳỹỷỵ!@#$%^&*(),.?":{}|<>';]"""
        match = re.search(pattern, string)
        if match:
            return True
        return False
        
    def getInfoUser(self):
        lstTenDangNhap = self.getTenDangNhap()
        manguoidung = self.getIdMoi()
        tendangnhap = self.entry_1.get()
        matkhau = self.entry_2.get()
        if tendangnhap in lstTenDangNhap:
            messagebox.showwarning("Warning", "Tên đăng nhập này đã có người sử dụng")
            return False
        elif self.checkDN(tendangnhap) or self.checkDN(matkhau):
            messagebox.showwarning("Warning", "Tên đăng nhập và mật khẩu không chứ ký tự đặc biệt")
            return False
        hoten = self.entry_3.get()
        gioitinh = self.item_stringGT.get()
        ngaysinh = self.entry_4.get()
        if self.checkInput(ngaysinh) is None:
            return False
        sodienthoai = self.entry_6.get()
        diachi = self.entry_5.get()
        noicongtac = 'Không'
        email = 'Không'
        vaitro = self.item_stringVT.get()
        ngaythamgia = f'{datetime.now().day}/{datetime.now().month}/{datetime.now().year}'
        lstDN = [tendangnhap,matkhau,manguoidung]
        for i in lstDN:
            if i == '':
                messagebox.showwarning("Warning", "Không được bỏ trống thông tin")
                return False
        queryDangNhap = f"""INSERT INTO DangNhap VALUES ('{lstDN[0]}','{lstDN[1]}','{lstDN[2]}')"""
        lstND = [manguoidung,hoten,gioitinh,ngaysinh,sodienthoai,diachi,noicongtac,email,vaitro,ngaythamgia]
        for i in lstND:
            if i == '':
                messagebox.showwarning("Warning", "Không được bỏ trống thông tin")
                return False
        queryNguoiDung = f"""INSERT INTO NguoiDung VALUES ('{lstND[0]}',N'{lstND[1]}',N'{lstND[2]}','{lstND[3]}',{lstND[4]},N'{lstND[5]}',N'{lstND[6]}',N'{lstND[7]}',N'{lstND[8]}','{lstND[9]}')"""
        self.insertDB(queryNguoiDung)
        self.insertDB(queryDangNhap)
        messagebox.showinfo("Thông báo", "Bạn đã đăng ký thành công, Vui lòng đăng nhập lại!")
        self.nextLogin()






if __name__ == "__main__":
    register = RegisterView()
    register.mainloop()