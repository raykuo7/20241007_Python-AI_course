import tkinter as tk
from PIL import Image, ImageTk

class Window(tk.Tk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.title('blablabla')

        self.geometry('600x400')
        self.resizable(False,True)

        ico = Image.open('D:/GitHub/20241007_Python-AI_course/Python/lesson4_1018/cat.png')
        photo = ImageTk.PhotoImage(ico)
        self.wm_iconphoto(False, photo)

        message =  tk.Label(self, text='lalala')
        message.pack()


def main():
    root = Window()
  


    root.mainloop()

if __name__ == '__main__':
    main()