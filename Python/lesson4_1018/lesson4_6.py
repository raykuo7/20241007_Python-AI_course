from ttkthemes import ThemedTk
from tkinter import ttk

class Window(ThemedTk):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.title('使用ttk的套件')
        style = ttk.Style(self)        
        self.geometry('800x500')

        topFrame = ttk.Frame(self, height=100, width=300, borderwidth=3,relief='groove')
        topFrame.pack(padx=10,pady=50, expand=True, fill= 'x') # expend 占滿
        bottomFrame = ttk.Frame(self, borderwidth=3,relief='groove') # 裡面有東西 (放按鈕) height width 就沒用了
        bottomFrame.pack(padx=10,pady=(0,10), expand=True, fill= 'x')

        btn1 = ttk.Button(topFrame, text='Button 1', underline=-1)
        btn1.pack(side='right', expand=True, fill='x')
        btn1_1 = ttk.Button(topFrame, text='Button 1_1')
        btn1_1.pack(side='right',expand=True, fill='x')
        btn1_2 = ttk.Button(topFrame, text='Button 1_2')
        btn1_2.pack(side='left',expand=True, fill='x')
        
        btn2 = ttk.Button(bottomFrame, text='Button 2')
        btn2.pack()

def main():
    window = Window(theme="arc")
    window.mainloop()

if __name__ == '__main__':
    main()