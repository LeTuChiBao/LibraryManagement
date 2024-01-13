from tkinter import *
import tkinter as tk
from tkinter import ttk,messagebox
from Connect_MSSQL import Connect_DB

class DeleteUserView(tk.Frame):
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

        self.img_bg_nguoidung = PhotoImage(file = "./image/Admin/nguoidung/bg_nguoidung.png")
        self.bg_nguoidung = self.canvas.create_image(750.0, 504.0, image = self.img_bg_nguoidung)

        # Bảng filter
        self.table = ttk.Treeview(self.master, show = 'headings', padding = "20px")
        style = ttk.Style()
        style.configure("Treeview", font = ("Tahoma", 10))
        self.table.place(x = 100, y = 254, height = 500, width = 1300)
        self.table['columns'] = ('Id', 'HoTen', 'GioiTinh', 'NgaySinh', 'SoDienThoai', 'DiaChi', 'NoiCongTac','Email','VaiTro','NgayThamGia')
        self.table.column('Id', width = 20, anchor = 'center')
        self.table.column('HoTen', width = 100, anchor = 'w')
        self.table.column('GioiTinh', width = 20, anchor = 'center')
        self.table.column('NgaySinh', width = 50, anchor = 'center')
        self.table.column('SoDienThoai', width = 70, anchor = 'center')
        self.table.column('DiaChi', width = 150, anchor = 'w')
        self.table.column('NoiCongTac', width = 150, anchor = 'w')
        self.table.column('Email', width = 150, anchor = 'w')
        self.table.column('VaiTro', width = 70, anchor = 'center')
        self.table.column('NgayThamGia', width = 50, anchor = 'center')

        self.table.heading('Id', text = 'ID')
        self.table.heading('HoTen', text = 'Họ và Tên')
        self.table.heading('GioiTinh', text = 'Giới tính')
        self.table.heading('NgaySinh', text = 'Ngày sinh')
        self.table.heading('SoDienThoai', text = 'Số điện thoại')
        self.table.heading('DiaChi', text = 'Địa chỉ')
        self.table.heading('NoiCongTac', text = 'Nơi Công tác')
        self.table.heading('Email', text = 'Email')
        self.table.heading('VaiTro', text = 'Vai trò')
        self.table.heading('NgayThamGia', text = 'Ngày tham gia')
        self.loadTable()
        scrollbar_table = ttk.Scrollbar(self.table, orient = 'vertical', command = self.table.yview)
        self.table.configure(yscrollcommand = scrollbar_table.set)
        scrollbar_table.place(relx = 1, rely = 0, relheight = 1, anchor = 'ne')
        self.table.bind('<<TreeviewSelect>>', self.user_select)

        self.img_button_xoanguoidung = PhotoImage(file = "./image/Admin/nguoidung/xoanguoidung.png")
        self.button_xoanguoidung = Button(image = self.img_button_xoanguoidung, borderwidth = 0, highlightthickness = 0, command = lambda: self.confirm_continue(), relief = "flat")
        self.button_xoanguoidung.place(x = 1134.0, y = 776.0, width = 266.0, height = 68.0)

        self.canvas.create_text(508.0, 173.0, anchor = "nw", text = "Thông tin người dùng", fill = "#00054B", font = ("PlayfairDisplay Regular", 50 * -1))

        # Button comback
        self.img_comeback = PhotoImage(file = "./image/comeback.png")
        self.button_comeback = Button(image = self.img_comeback, borderwidth = 0, highlightthickness = 0, command = lambda: self.prevHomeAdmin(), relief = "flat")
        self.button_comeback.place(x = 49.0, y = 776.0, width = 271.0, height = 75.0)

    def prevHomeAdmin(self):
        self.master.prevHomeAdmin()

    def loadFromDB(self):
        dataUser = []
        database = Connect_DB.MSSQLConnection()
        database.connect()
        query = f"SELECT * FROM NguoiDung"
        lst = database.query(query)
        database.close
        for i in lst:
            i = list(i)
            i[0] = i[0].strip()
            i[3] = i[3].strftime("%d/%m/%Y")
            i[9] = i[9].strftime("%d/%m/%Y")
            dataUser.append(i)
        return dataUser
    
    def deleteDB(self,query):
        database = Connect_DB.MSSQLConnection()
        database.connect() 
        database.delete(query)
        database.close()
        return True
    
    def loadTable(self):
        users = self.loadFromDB()
        for user in users:
            self.table.insert('', 'end', values = user)

    def user_select(self, event=None):
        selected_item = self.table.selection()
        if selected_item:
            item_values = self.table.item(selected_item, 'values')
            item_values = list(item_values)
            return item_values
        return None  # Trả về None nếu không có mục được chọn

    def delUser(self):
        user_values = self.user_select()
        if user_values:
            user_id = user_values[0]  # Giả sử cột đầu tiên là ID người dùng
            query1 = f"DELETE FROM DangNhap WHERE Id_NguoiDung = '{user_id}'"
            query2 = f"DELETE FROM NguoiDung WHERE Id_NguoiDung = '{user_id}'"
            self.deleteDB(query1)
            self.deleteDB(query2)
            
            # Tùy chọn: Bạn có thể tải lại bảng sau khi xóa
            self.loadTable()

    def confirm_continue(self):
        result = messagebox.askyesno("Xác nhận", "Bạn có muốn tiếp tục xóa người dùng này không?")
        if result:
            self.delUser()  # Thực thi hàm khi người dùng chọn Có
            for item in self.table.get_children():
                self.table.delete(item)
            self.loadTable()
            messagebox.showinfo("Thông báo", "Người dùng đã được xóa thành công!")
        else:
            pass  # Không làm gì khi người dùng chọn Không
        