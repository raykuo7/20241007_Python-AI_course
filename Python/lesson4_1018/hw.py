from ttkthemes import ThemedTk
from tkinter import ttk
from ttkthemes import ThemedTk
from tkinter import ttk

class Window(ThemedTk):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.title('使用ttk的套件')
        style = ttk.Style(self)        
        topFrame = ttk.Frame(self,borderwidth=1,relief='groove')
        btn1 = ttk.Button(topFrame,text="按鈕1")
        btn1.pack(side='left',expand=True,fill='x',padx=10)
        btn2 = ttk.Button(topFrame,text="按鈕2")
        btn2.pack(side='left',expand=True,fill='x')
        btn3 = ttk.Button(topFrame,text="按鈕3")
        btn3.pack(side='left',expand=True,fill='x',padx=10)
        topFrame.pack(padx=10,pady=(10,0),ipadx=10,ipady=10,expand=True,fill='x')

        bottomFrame = ttk.Frame(self,borderwidth=1,relief='groove')
        bottomFrame.pack(padx=10,pady=10,expand=True,fill='x')

        f1 = ttk.Frame(bottomFrame,borderwidth=3,height=500,relief='groove')
        f2 = ttk.Frame(bottomFrame,borderwidth=3,height=500,relief='groove')
        f3 = ttk.Frame(bottomFrame,borderwidth=3,height=500,relief='groove')
        f1.pack(side='left', expand=True,fill='x')
        f2.pack(side='left', expand=True,fill='x')
        f3.pack(side='left', expand=True,fill='x')
        
        btna1 = ttk.Button(f1,text="按鈕1")
        btna1.pack(expand=True,fill='both',)
        btna2 = ttk.Button(f1,text="按鈕2")
        btna2.pack(expand=True,fill='both',)
        btna3 = ttk.Button(f1,text="按鈕3")
        btna3.pack(expand=True,fill='both',)

        btnb1 = ttk.Button(f2,text="按鈕1")
        btnb1.pack(expand=True,fill='both',)
        btnb2 = ttk.Button(f2,text="按鈕2")
        btnb2.pack(expand=True,fill='both',)
        btnb3 = ttk.Button(f2,text="按鈕3")
        btnb3.pack(expand=True,fill='both',)


        btnc1 = ttk.Button(f3,text="按鈕1")
        btnc1.pack(expand=True,fill='both',)
        btnc2 = ttk.Button(f3,text="按鈕2")
        btnc2.pack(expand=True,fill='both',)
        btnc3 = ttk.Button(f3,text="按鈕3")
        btnc3.pack(expand=True,fill='both',)


def main():
    window = Window(theme="arc")
    window.mainloop()

if __name__ == '__main__':
    main()