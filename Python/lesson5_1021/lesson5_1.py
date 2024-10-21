import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
from tkinter.messagebox import showinfo


class Window(ThemedTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

 
        style = ttk.Style(self)
        style.configure('TopFrame.TLabel',font=('Helvetica',20))    # TLabel "T" "L" needs CAPITALIZE!!!

        topframe = ttk.Frame(self)
        ttk.Label(topframe, text="輸入個資:", style='TopFrame.TLabel').pack()
        topframe.pack(padx=20, pady=20)
        
        
        bottomframe = ttk.Frame(self,borderwidth=3, relief='groove')
        ttk.Label(bottomframe, text='USER NAME: ').grid(column=0, row=0, padx=(10,5), sticky='E')        # column 行  ; row 列
        self.username = tk.StringVar()
        # user_entery = ttk.Entry(bottomframe, )
        # user_entery.grid(column=1, row=0)
        ttk.Entry(bottomframe, textvariable=self.username).grid(column=1, row=0)


        ttk.Label(bottomframe, text='USER PASSWORD: ').grid(column=0, row=1, padx=(10,5), sticky='E')
        self.password = tk.StringVar()
        # password_entery = ttk.Entry(bottomframe)      加上stringvar 之前
        # password_entery.grid(column=1, row=1, )
        ttk.Entry(bottomframe, textvariable=self.password, show='*').grid(column=1, row=1, )  #用StringVar之後就只是外觀   
        ## +textvariable  show='*'

        bottomframe.pack(expand=True, fill='x', ipadx=10, ipady=10)

        radioFrame = ttk.Frame(bottomframe,borderwidth=3, relief='groove').grid(column=0, row=2, columnspan=2) # colmnspan = 2 橫跨兩欄
        
        size = (
            ('Small' , 'S'),
            ('Medium' , 'M'),
            ('Large' , 'L'),
            ('Extra Large' , 'XL'),
            ('Extra Extra Large', 'XXL')
        )



        cancle_btn = ttk.Button(bottomframe, text='取消',command= self.cancel_click)
        cancle_btn.grid(column=0,row=3, padx=20, pady=(30,0))

        ok_btn = ttk.Button(bottomframe, text='確認', command=self.ok_click)
        ok_btn.grid(column=1, row=3, padx=10, pady=(30,0), sticky='E')

    def cancel_click(self):
        self.username.set('')
        self.password.set('')
    
    def ok_click(self):
        username = self.username.get()
        password = self.password.get()
        showinfo(title='使用者輸入', message=f'使用者名稱:{username}\n使用者密碼:{[password]}')

def main():
    window = Window(theme = "arc")
    # window.username.set('here puts name')         set 用法
    # window.password.set('here puts password')
    window.mainloop()
    
    

if __name__ == '__main__':
    main()