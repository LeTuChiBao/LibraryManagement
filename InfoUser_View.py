from tkinter import *
import tkinter as tk
from tkinter import ttk,messagebox
from Connect_MSSQL import Connect_DB
import Edit_InfoUser_View

class InfoUserView(tk.Frame):
    def __init__(self,master,user):
        super().__init__(master)
        self.user = user
        self.editing = False
        dataUser = self.loadFromDB()

        self.canvas = Canvas(self.master, bg = "#FFFFFF", height = 900, width = 1500, bd = 0, highlightthickness = 0, relief = "ridge")
        self.canvas.place(x = 0, y = 0)

        # Background
        self.img_background = PhotoImage(file = "./image/background.png")
        self.background = self.canvas.create_image(750.0, 450.0, image = self.img_background)

        # Logo
        self.img_logo = PhotoImage(file = "./image/logo.png")
        self.logo = self.canvas.create_image(320.0, 95.0, image = self.img_logo)

        self.canvas.create_text(771.0, 64.0, anchor = "nw", text = "Thông tin cá nhân", fill = "#00054B", font = ("PlayfairDisplay Regular", 60 * -1))

        self.img_form_info = PhotoImage(file = "./image/Users/nguoidung/bg_form_info.png")
        self.bg_form_info = self.canvas.create_image(1013.0, 467.0, image = self.img_form_info)

        self.img_form_avatar = PhotoImage(file = "./image/Users/nguoidung/bg_form_avatar.png")
        self.bg_form_avatar = self.canvas.create_image(329.0, 467.0, image = self.img_form_avatar)

        tennguoidung = dataUser[1]
        vaitro = dataUser[8]
        self.canvas.create_rectangle(139.0, 554.0, 529.0, 614.0, fill = "#F5F5F5", outline = "")
        self.canvas.create_rectangle(210.0, 657.0, 450.0, 717.0, fill = "#CCFFFF", outline = "")
        self.canvas.create_text(214.0, 566.0, anchor = "nw", text = f"{tennguoidung}", fill = "#000000", font = ("RobotoRoman Bold", 30 * -1))
        self.canvas.create_text(330.0, 687.0, anchor = "center", text = f"{vaitro}", fill = "#000000", font = ("RobotoRoman Bold", 30 * -1))

        # Mã người dùng
        manguoidung = dataUser[0]
        self.img_id = PhotoImage(file = "./image/Users/nguoidung/id.png")
        self.id = self.canvas.create_image(768.0, 221.0, image = self.img_id)
        self.canvas.create_text(908.0, 208.0, anchor = "nw", text = f'{manguoidung}', fill = "#000000", font = ("RobotoRoman Bold", 25 * -1))
        # Giới tính
        gioitinh = dataUser[2]
        self.img_gioitinh = PhotoImage(file = "./image/Users/nguoidung/gioitinh.png")
        self.gioitinh = self.canvas.create_image(735.0, 291.0, image = self.img_gioitinh)
        self.canvas.create_text(908.0, 276.0, anchor = "nw", text = f'{gioitinh}', fill = "#000000", font = ("RobotoRoman Bold", 25 * -1))
        # Ngày sinh
        ngaysinh = dataUser[3]
        self.img_ngaysinh = PhotoImage(file = "./image/Users/nguoidung/ngaysinh.png")
        self.ngaysinh = self.canvas.create_image(739.0, 361.0, image = self.img_ngaysinh)
        self.canvas.create_text(908.0, 346.0, anchor = "nw", text = f'{ngaysinh}', fill = "#000000", font = ("RobotoRoman Bold", 25 * -1))
        # Email
        email = dataUser[7]
        self.img_email = PhotoImage(file = "./image/Users/nguoidung/email.png")
        self.email = self.canvas.create_image(715.0, 431.0, image = self.img_email)
        self.canvas.create_text(908.0, 416.0, anchor = "nw", text = f'{email}', fill = "#000000", font = ("RobotoRoman Bold", 25 * -1))
        # Địa chỉ
        diachi = dataUser[5]
        self.img_diachi = PhotoImage(file = "./image/Users/nguoidung/diachi.png")
        self.diachi = self.canvas.create_image(719.0, 501.0, image = self.img_diachi)
        self.canvas.create_text(908.0, 486.0, anchor = "nw", text = f'{diachi}', fill = "#000000", font = ("RobotoRoman Bold", 25 * -1))
        # Số điện thoại
        sodienthoai = dataUser[4]
        self.img_sdt = PhotoImage(file = "./image/Users/nguoidung/sdt.png")
        self.sdt = self.canvas.create_image(758.0, 571.0, image = self.img_sdt)
        self.canvas.create_text(908.0, 556.0, anchor = "nw", text = f'{sodienthoai}', fill = "#000000", font = ("RobotoRoman Bold", 25 * -1))
        # Nơi công tác
        noicongtac = dataUser[6]
        self.img_noicongtac = PhotoImage(file = "./image/Users/nguoidung/noicongtac.png")
        self.noicongtac = self.canvas.create_image(754.0, 641.0, image = self.img_noicongtac)
        self.canvas.create_text(908.0, 629.0, anchor = "nw", text = f'{noicongtac}', fill = "#000000", font = ("RobotoRoman Bold", 25 * -1))
        # Ngày tham gia
        ngaythamgia = dataUser[9]
        self.img_ngaythamgia = PhotoImage(file = "./image/Users/nguoidung/ngaythamgia.png")
        self.ngaythamgia = self.canvas.create_image(766.0, 713.0, image = self.img_ngaythamgia)
        self.canvas.create_text(908.0, 698.0, anchor = "nw", text = f'{ngaythamgia}', fill = "#000000", font = ("RobotoRoman Bold", 25 * -1))

        if gioitinh == 'Nam':
            avt = 'nam'
        else:
            avt = 'nu'
        self.img_avt = PhotoImage(file = f"./image/Users/nguoidung/{avt}.png")
        self.image_5 = self.canvas.create_image(334.0, 361.0, image = self.img_avt)

        self.img_chinhsua = PhotoImage(file = "./image/Users/nguoidung/chinhsuathongtin.png")
        self.button_chinhsua = Button(image = self.img_chinhsua, borderwidth = 0, highlightthickness = 0, command = lambda: self.nextEditInfo(), relief = "flat")
        self.button_chinhsua.place(x = 877.0, y = 786.0, width = 305.0, height = 68.0)

        self.img_doimatkhau = PhotoImage(file = "./image/Users/nguoidung/doimatkhau.png")
        self.button_doimatkhau = Button(image = self.img_doimatkhau, borderwidth = 0, highlightthickness = 0, command = lambda: self.changePassWord(), relief = "flat")
        self.button_doimatkhau.place(x = 1204.0, y = 786.0, width = 212.0, height = 68.0)

        # Button comback
        self.img_comeback = PhotoImage(file = "./image/comeback.png")
        self.button_comeback = Button(image = self.img_comeback, borderwidth = 0, highlightthickness = 0, command = lambda: self.prevHomeUser(), relief = "flat")
        self.button_comeback.place(x = 59.0, y = 782.0, width = 271.0, height = 75.0)

    def prevHomeUser(self):
        self.master.prevHomeUser()

    def nextEditInfo(self):
        self.destroy()
        Edit_InfoUser_View.EditInfoUser_View(self.master,self.user)
    
    def queryUpdateDB(self,query):
        database = Connect_DB.MSSQLConnection()
        database.connect()
        database.update(query)
        database.close()

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
        lst[9] = lst[9].strftime("%d/%m/%Y")
        return lst
    
    def loadPassWord(self):
        database = Connect_DB.MSSQLConnection()
        database.connect()
        query = f"SELECT MatKhau FROM DangNhap WHERE Id_NguoiDung = '{self.user}'"
        lst = database.query(query)
        database.close
        lst = lst[0]
        lst = list(lst)
        return lst[0]
    

    def changePassWord(self):
        top = Toplevel(self.master)
        top.geometry("300x200+%d+%d" % (800, 450))
        #top.iconphoto(True, PhotoImage(file="./image/Users/muonsach/logo_error.png"))
        top.overrideredirect(True)
        top.title("Đổi mật khẩu")

        current_password = self.loadPassWord()
        user = self.user

        def change_password(current_password,old_password,new_password,confirm_password,user):
            if current_password == old_password:
                if new_password == confirm_password:
                    query = f"UPDATE DangNhap SET MatKhau = '{new_password}' WHERE Id_NguoiDung = '{user}';"
                    self.queryUpdateDB(query)
                    messagebox.showinfo("Thông báo", "Thay đổi mật khẩu thành công!")
                    close_window()
                else:
                    messagebox.showwarning("Thông báo", "Nhập lại mật khẩu không chính xác!")
                    self.changePassWord()
            else:
                messagebox.showwarning("Thông báo", "Mật khẩu cũ không đúng!")
                self.changePassWord()
        def close_window():
            top.destroy()
        label_old_password = Label(top, text = "Mật khẩu cũ:")
        label_old_password.place(x = 10.0, y = 20.0)

        entry_old_password = Entry(top, show='●')
        entry_old_password.place(x = 140.0, y = 20.0)


        label_new_password = Label(top, text = "Mật khẩu mới:")
        label_new_password.place(x = 10.0, y = 70.0)

        entry_new_password = Entry(top, show = '●')
        entry_new_password.place(x = 140.0, y = 70.0)


        label_confirm_password = Label(top, text = "Nhập lại mật khẩu mới:")
        label_confirm_password.place(x = 10.0, y = 120.0)

        entry_confirm_password = Entry(top, show = '●')
        entry_confirm_password.place(x = 140.0, y = 120.0)


        button_change = Button(top, text = "Đổi mật khẩu", command = lambda: change_password(current_password, entry_old_password.get(), entry_new_password.get(), entry_confirm_password.get(), user))
        button_change.place(x = 190.0, y = 155.0)

        button_close = Button(top, text = "Quay lại", command = close_window)
        button_close.place(x = 30.0, y = 155.0)
            