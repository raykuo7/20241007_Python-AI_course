from ttkthemes import ThemedTk
from tkinter import ttk


class Window(ThemedTk):                 
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.title('使用ttk的套件')
        style = ttk.Style(self)        

        topFrame = ttk.Frame(self,borderwidth=1,relief='groove',)
        self.btn1 = ttk.Button(topFrame,text="按鈕1", command=self.userclick1) # commend 為按鈕控制
        self.btn1.pack(side='left',expand=True,fill='x',padx=10)
      
        btn2 = ttk.Button(topFrame,text="按鈕2", command=self.userclick2)
        btn2.bind('<ButtonRelease>', self.btn2_click )
        btn2.pack(side='left',expand=True,fill='x')

        
        btn3 = ttk.Button(topFrame,text="按鈕3", command=self.userclick3)
        btn3.pack(side='left',expand=True,fill='x',padx=10)
        topFrame.pack(padx=10,pady=(10,0),ipadx=10,ipady=10,expand=True,fill='x')

        bottomFrame = ttk.Frame(self,borderwidth=1,height=2000,relief='groove')
        bottomFrame.pack(padx=10,pady=10,expand=True,fill='x')

        f1 = ttk.Frame(bottomFrame,borderwidth=3,relief='groove')
        f2 = ttk.Frame(bottomFrame,borderwidth=3,relief='groove')
        f3 = ttk.Frame(bottomFrame,borderwidth=3,relief='groove')
        f1.pack(side='left', padx=10, expand=True,fill='both')
        f2.pack(side='left', padx=10, expand=True,fill='both')
        f3.pack(side='left', padx=10, expand=True,fill='both')
        
        
        btna1 = ttk.Button(f1,text="按鈕1")             # link
        btna1.bind('<ButtonRelease>', self.btna1_click )

        btna1.pack(fill='x', padx=10, pady=(5, 5), ipady=50)
        btna2 = ttk.Button(f1,text="按鈕2")
        btna2.pack(fill='x', padx=10, pady=(5, 5), ipady=25)
        btna3 = ttk.Button(f1,text="按鈕3")
        btna3.pack(fill='x', padx=10, pady=(5, 5), ipady=25)


        btnb1 = ttk.Button(f2,text="按鈕1")
        btnb1.pack(fill='x', padx=10, pady=(5, 5), ipady=40)
        btnb2 = ttk.Button(f2,text="按鈕2")
        btnb2.pack(fill='x', padx=10, pady=(5, 5), ipady=20)
        btnb3 = ttk.Button(f2,text="按鈕3")
        btnb3.pack(fill='x', padx=10, pady=(5, 5), ipady=40)


        btnc1 = ttk.Button(f3,text="按鈕1")
        btnc1.pack(fill='x', padx=10, pady=(5, 5), ipady=100/3)
        btnc2 = ttk.Button(f3,text="按鈕2")
        btnc2.pack(fill='x', padx=10, pady=(5, 5), ipady=100/3)
        btnc3 = ttk.Button(f3,text="按鈕3")
        btnc3.pack(fill='x', padx=10, pady=(5, 5), ipady=100/3)

    def userclick1(self):
        print('hi but1')
        self.btn1.configure(text='pressed!')
    def userclick2(self):
        print('hi but2')
    def userclick3(self):
        print('hi but3')

    def btna1_click(self, event):       # link with event
        print('btna1_click')
        print(event)
        print(event.widget.configure(text='pressed!'))  
    
    def btn2_click(self, event):
        print('btn2_click')
    

def main():
    window = Window(theme="arc")
    window.mainloop()

if __name__ == '__main__':
    main()