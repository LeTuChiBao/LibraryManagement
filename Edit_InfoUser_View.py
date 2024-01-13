import re
from tkinter import *
import tkinter as tk
from tkinter import ttk,messagebox
from datetime import datetime
from PIL import ImageTk 
from tkcalendar import Calendar
from Connect_MSSQL import Connect_DB
import InfoUser_View


class EditInfoUser_View(tk.Frame):
    def __init__(self, master, user):
        super().__init__(master)
        self.user = user
        self.var = IntVar()
        dataUser = self.loadFromDB()

        self.canvas = Canvas(self.master, bg = "#FFFFFF", height = 900, width = 1500, bd = 0, highlightthickness = 0, relief = "ridge")
        self.canvas.place(x = 0, y = 0)

        # Background
        self.img_background = PhotoImage(file = "./image/background.png")
        self.background = self.canvas.create_image(750.0, 450.0, image = self.img_background)

        # Logo
        self.img_logo = PhotoImage(file = "./image/logo.png")
        self.logo = self.canvas.create_image(320.0, 95.0, image = self.img_logo)


        self.img_button_luu = PhotoImage(file = "./image/Users/nguoidung/luu.png")
        self.button_luu = Button(image = self.img_button_luu, borderwidth = 0, highlightthickness = 0, command = lambda: self.updateInfo(), relief = "flat")
        self.button_luu.place(x = 1204.0, y = 786.0, width = 149.0, height = 68.0)

        self.canvas.create_text(547.0, 164.0, anchor = "nw", text = "Thông tin cá nhân", fill = "#00054B", font = ("PlayfairDisplay Regular", 50 * -1))

        self.img_bg_form_edit = PhotoImage(file = "./image/Users/nguoidung/bg_form_edit.png")
        self.bg_form_edit = self.canvas.create_image(750.0, 545.0,image = self.img_bg_form_edit)


        self.img_button_calendar = PhotoImage(file = "./image/Users/nguoidung/calendar.png")
        self.button_calendar = Button(image = self.img_button_calendar, borderwidth = 0, highlightthickness = 0, command = lambda: self.calendar(self.entry_ngaysinh), relief = "flat")
        self.button_calendar.place(x = 986.0, y = 440.0, width = 40.0, height = 40.0)

        self.img_entry = PhotoImage(file = "./image/Users/nguoidung/entry.png")
        ngaysinh = dataUser[3]
        self.canvas.create_text(503.0, 442.0, anchor = "nw",text = "Ngày sinh", fill = "#555454", font = ("RobotoRoman Bold", 30 * -1))
        self.bg_entry_ngaysinh = self.canvas.create_image(830.0, 460.0, image = self.img_entry)
        self.entry_ngaysinh = Entry(bd = 0, bg = "#E3E3E3", fg = "#000716", highlightthickness = 0, font = ("Tahoma", 18))
        self.entry_ngaysinh.place(x = 695.0, y = 440.0, width = 270.0, height = 38.0)
        self.entry_ngaysinh.insert(0, ngaysinh)

        gioitinh = dataUser[2]
        self.canvas.create_text(503.0, 367.0, anchor = "nw", text = "Giới tính", fill = "#555454", font = ("RobotoRoman Bold", 30 * -1))
        self.canvas.create_text(744.0, 367.0, anchor = "nw", text = "Nam", fill = "#555454", font = ("RobotoRoman Bold", 30 * -1))
        self.canvas.create_text(880.0, 367.0, anchor = "nw", text = "Nữ", fill = "#555454", font = ("RobotoRoman Bold", 30 * -1))
        if gioitinh == 'Nam':
            self.check_button_nam = Checkbutton(self.master, variable = self.var, onvalue = 0, offvalue = 1)
            self.check_button_nam.place(x = 720.0, y = 385.0, anchor = "center")
            self.check_button_nu = Checkbutton(self.master, variable = self.var, onvalue = 1, offvalue = 0)
            self.check_button_nu.place(x = 855.0, y = 385.0, anchor = "center")
        else:
            self.check_button_nam = Checkbutton(self.master, variable = self.var, onvalue = 1, offvalue = 0)
            self.check_button_nam.place(x = 720.0, y = 385.0, anchor = "center")
            self.check_button_nu = Checkbutton(self.master, variable = self.var, onvalue = 0, offvalue = 1)
            self.check_button_nu.place(x = 855.0, y = 385.0, anchor = "center")

        tennguoidung = dataUser[1]
        self.canvas.create_text(503.0, 292.0, anchor = "nw", text = "Họ và tên", fill = "#555454", font = ("RobotoRoman Bold", 30 * -1))
        self.bg_entry_hoten = self.canvas.create_image(830.0, 310.0, image = self.img_entry)
        self.entry_hoten = Entry(bd = 0, bg = "#E3E3E3", fg = "#000716", highlightthickness = 0, font = ("Tahoma", 18))
        self.entry_hoten.place(x = 695.0, y = 290.0, width = 270.0, height = 38.0)
        self.entry_hoten.insert(0, tennguoidung)

        email = dataUser[7]
        self.canvas.create_text(503.0, 522.0, anchor = "nw", text = "Email", fill = "#555454", font = ("RobotoRoman Bold", 30 * -1))
        self.bg_entry_email = self.canvas.create_image(830.0, 540.0, image = self.img_entry)
        self.entry_email = Entry(bd = 0, bg = "#E3E3E3", fg = "#000716", highlightthickness = 0, font = ("Tahoma", 18))
        self.entry_email.place(x = 695.0, y = 520.0, width = 270.0, height = 38.0)
        self.entry_email.insert(0, email)

        diachi = dataUser[5]
        self.canvas.create_text(503.0, 602.0, anchor = "nw", text = "Địa chỉ", fill = "#555454", font = ("RobotoRoman Bold", 30 * -1))
        self.bg_entry_diachi = self.canvas.create_image(830.0, 620.0, image = self.img_entry)
        self.entry_diachi = Entry(bd = 0, bg = "#E3E3E3", fg = "#000716", highlightthickness = 0, font = ("Tahoma", 18))
        self.entry_diachi.place(x = 695.0, y = 600.0, width = 270.0, height = 38.0)
        self.entry_diachi.insert(0, diachi)
        
        sodienthoai = dataUser[4]
        self.canvas.create_text(503.0, 682.0, anchor = "nw", text = "Số điện thoại", fill = "#555454", font = ("RobotoRoman Bold", 30 * -1))
        self.bg_entry_sodienthoai = self.canvas.create_image(830.0, 697.0, image = self.img_entry)
        self.entry_sodienthoai = Entry(bd = 0, bg = "#E3E3E3", fg = "#000716", highlightthickness = 0, font = ("Tahoma", 18))
        self.entry_sodienthoai.place(x = 695.0, y = 677.0, width = 270.0, height = 38.0)
        self.entry_sodienthoai.insert(0, sodienthoai)

        noicongtac = dataUser[6]
        self.canvas.create_text(503.0, 762.0, anchor = "nw", text = "Nơi công tác", fill = "#555454", font = ("RobotoRoman Bold", 30 * -1))
        self.bg_entry_noicongtac = self.canvas.create_image(830.0, 780.0, image = self.img_entry)
        self.entry_noicongtac = Entry(bd = 0, bg = "#E3E3E3", fg = "#000716", highlightthickness = 0, font = ("Tahoma", 18))
        self.entry_noicongtac.place(x = 695.0, y = 760.0, width = 270.0, height = 38.0)
        self.entry_noicongtac.insert(0, noicongtac)

        # Button comback
        self.img_comeback = PhotoImage(file = "./image/comeback.png")
        self.button_comeback = Button(image = self.img_comeback, borderwidth = 0, highlightthickness = 0, command = lambda: self.prevInfoUser(), relief = "flat")
        self.button_comeback.place(x = 59.0, y = 782.0, width = 271.0, height = 75.0)

    def prevInfoUser(self):
        self.destroy()
        InfoUser_View.InfoUserView(self.master,self.user)
    
    def calendar(self, entry):
        top = tk.Toplevel(self.master)
        top.geometry("+1250+500")
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

        cal = Calendar(top, selectmode='day', date_pattern = 'dd/MM/yyyy')
        cal.pack(padx=5, pady=5)
        cal.bind("<<CalendarSelected>>", set_value)

    def loadFromDB(self):
        database = Connect_DB.MSSQLConnection()
        database.connect()
        query = f"SELECT * FROM NguoiDung WHERE Id_NguoiDung = '{self.user}'"
        lst = database.query(query)
        database.close
        lst = lst[0]
        lst = list(lst)
        lst[0] = lst[0].strip()
        lst[3] = lst[3].strftime("%d/%m/%Y")
        return lst
    
    def queryUpdateDB(self,query):
        database = Connect_DB.MSSQLConnection()
        database.connect()
        database.update(query)
        database.close()
    
    def checkInput(self,ngaySinh):
        regexNgay = r'^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}$'
        if ngaySinh == '' or not re.match(regexNgay, ngaySinh):
            messagebox.showwarning("Warning", "Ngày sinh không hợp lệ! Vui lòng nhập lại.")
            return None
        else:
            return True

    def saveInfo(self):
        ngaysinh = self.entry_ngaysinh.get()
        if self.checkInput(ngaysinh) is None:
            return False
        else:
            hoten = self.entry_hoten.get()
            gioitinh = self.var.get()
            if gioitinh == 1:
                gioitinh = 'Nam'
            else:
                gioitinh = 'Nữ'
            email = self.entry_email.get()    
            diachi = self.entry_diachi.get()   
            sodienthoai = self.entry_sodienthoai.get()  
            noicongtac = self.entry_noicongtac.get()
            lst = [hoten,gioitinh,ngaysinh,sodienthoai,diachi,noicongtac,email]
            return lst

    def updateInfo(self):
        dataInfo = self.saveInfo()   
        query = f"UPDATE NguoiDung SET Hoten = N'{dataInfo[0]}',GioiTinh = N'{dataInfo[1]}',NgaySinh = '{dataInfo[2]}',SoDT = '{dataInfo[3]}',DiaChi = N'{dataInfo[4]}',NoiCongTac = N'{dataInfo[5]}',Email = '{dataInfo[6]}' WHERE Id_NguoiDung = '{self.user}';"         
        self.queryUpdateDB(query)
        self.prevInfoUser()