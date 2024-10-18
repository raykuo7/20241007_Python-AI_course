import tkinter as tk
from tkinter import ttk

class Window(tk.Tk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title('TTK window')
        self.geometry('500x400')
        message = ttk.Label(self, text='lalala(lable)') # -->為區域變數
        # self.message --> 為設定attribute
        message.pack()

def main():
    rt = Window()

    rt.mainloop()

if __name__ == '__main__':
    main()