import tkinter as tk
# from ttkthemes import ThemedTk as tk
from tkinter import ttk
from PIL import Image, ImageTk

class Window(tk.Tk):
# class Window(tk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title('TTK window')
        self.geometry('800x400')
        
        ico = Image.open('D:/GitHub/20241007_Python-AI_course/Python/lesson4_1018/cat.png')
        photo = ImageTk.PhotoImage(ico)
        self.wm_iconphoto(False, photo)
        resized_ico = ico.resize((50, 50))
        self.photo = photo

        style = ttk.Style(self) # 用ttk.style(self) 傳出style
        style.configure('TLabel', font =('Helvetica', 15))      #修改現有的
        style.configure('Title.TLabel', font =('Helvetica', 30))    #自訂的style (Title.TLabel)
        style.configure('Main.TButton', font = ('Arial', 22))

        message = ttk.Label(self, text='lalala(lable_defult)') # -->為區域變數
        message1 = ttk.Label(self, text="hahaha(自訂style'Title.TLabel')", style='Title.TLabel', background='purple', foreground='lightblue')
        message2 = tk.Label(self, text="mumumumu", bg='yellow', font=('Helvetica', 30), fg= 'blue')
        
        # self.message --> 為設定attribute
        message.pack()
        message1.pack()
        message2.pack()

        btn1 = ttk.Button(self, text="button 1 ", style="Main.TButton" )
        btn1.pack(ipadx=22, ipady=42)
        btn2 = tk.Button(self, text="button 1 ", image=self.photo, compound='left', font=('Arial', 22))
        btn2.pack(ipadx=22, ipady=42)

def main():
    rt = Window()

    rt.mainloop()

if __name__ == '__main__':
    main()