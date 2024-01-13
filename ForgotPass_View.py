from tkinter import *
import tkinter as tk

class ForgetPassView(tk.Tk):
    def __init__(self):
        super().__init__()
        self.iconbitmap('./image/Icon_Book_Library.ico')
        self.title("Library Management System")
        self.geometry("1000x500+400+300")
        self.configure(bg = "#FFFFFF")

        self.canvas = Canvas(self, bg = "#FFFFFF", height = 500, width = 1000, bd = 0, highlightthickness = 0, relief = "ridge")
        self.canvas.place(x = 0, y = 0)
        self.canvas.create_text(250.0, 50.0, anchor = "nw", text = "FORGOT PASSWORD", fill = "#9377EE", font = ("RobotoRoman Bold", 40 * -1))

        entry_image = PhotoImage(file = './image/entry_login.png')

        self.canvas.create_text(99.0, 123.0, anchor = "nw", text = "User name:", fill = "#555454", font = ("RobotoRoman Bold", 16 * -1))
        self.entry_bg_1 = self.canvas.create_image(253.0, 167.0, image = entry_image)
        self.entry_1 = Entry(bd = 0, bg = "#E3E3E3", fg = "#000716", highlightthickness = 0, font = ("RobotoRoman Bold", 16 * -1))
        self.entry_1.place(x = 101.0, y = 147.0, width = 304.0, height = 38.0)

        self.canvas.create_text(99.0, 200.0, anchor = "nw", text = "Phone:", fill = "#555454", font = ("RobotoRoman Bold", 16 * -1))
        self.entry_bg_2 = self.canvas.create_image(253.0, 244.0, image = entry_image)
        self.entry_2 = Entry(bd = 0, bg = "#E3E3E3", fg = "#000716", highlightthickness = 0, font = ("RobotoRoman Bold", 16 * -1), show = '●')
        self.entry_2.place(x = 101.0, y = 224.0, width = 304.0, height = 38.0)

        button_image_1 = PhotoImage(file = './image/button_otp1.png')
        self.button_1 = Button(image = button_image_1, borderwidth = 0, highlightthickness = 0, command = lambda: print("button_1 clicked"), relief = "flat")
        self.button_1.place( x = 430.0, y = 230.0, width = 65.0, height = 32.0)


        entry_otp = PhotoImage(file = './image/otp.png')
        self.entry_otp = self.canvas.create_image(111.0, 320.0, image = entry_otp)
        self.entry = Entry(bd = 0, bg = "#E3E3E3", fg = "#000716", highlightthickness = 0, font = ("RobotoRoman Bold", 16 * -1))
        self.entry.place(x = 111.0, y = 301.0, width = 30.0, height = 38.0)
        self.entry.bind("<Key>", self.reset)

        # self.canvas.create_text(119.0, 394.0, anchor = "nw", text = "Don't have an account", fill = "#555454", font = ("RobotoRoman Regular", 16 * -1))
        # button_image_2 = PhotoImage(file = './image/button_register.png')
        # self.button_2 = Button(image = button_image_2, borderwidth = 0, highlightthickness = 0, command = lambda: print("button_2 clicked"), relief = "flat")
        # self.button_2.place(x = 284.0, y = 391.0, width = 103.0, height = 26.0)


        # image_image_1 = PhotoImage(file = './image/Library_Forgot.png')
        # self.image_1 = self.canvas.create_image(713.0, 261.0, image = image_image_1)
        self.resizable(False, False)
        self.mainloop()

    def reset(self):
        self.entry.delete(1, END)
        
    
    # def nextRegister(self):
    #     self.destroy()
    #     Register_View.RegisterView()

if __name__ == "__main__":

    register = ForgetPassView()
    register.mainloop()