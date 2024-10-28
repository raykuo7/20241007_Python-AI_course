import datasource

from tkinter import ttk
import tkinter as tk
from ttkthemes import ThemedTk
from tkinter.messagebox import showinfo

class Window(ThemedTk):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title('登入')
        #==============style===============
        style = ttk.Style(self)
        style.configure('TopFrame.TLabel',font=('Helvetica',20))
        #============end style===============
        
        #==============top Frame===============

        topFrame = ttk.Frame(self)
        ttk.Label(topFrame,text='空氣品質指標(AQI)(歷史資料)',style='TopFrame.TLabel').pack()
        topFrame.pack(padx=20,pady=20)
        
        #==============end topFrame===============

        #==============bottomFrame===============
        bottomFrame = ttk.Frame(self)
        sitenames = datasource.get_sitename()
        
        # sitenames.insert(0,'請選擇站點')
        
        self.selected_site = tk.StringVar()     ## 一定要加self
        sitenames_cb = ttk.Combobox(bottomFrame, textvariable= self.selected_site,state='readonly')
        sitenames_cb.configure(values=sitenames)
        sitenames_cb.set('請選擇站點')
        sitenames_cb.bind('<<ComboboxSelected>>', self.sitename_selected)   # link with event(use "bind")  diffferent from link with commend(use "commend")
        sitenames_cb.pack(side='left',anchor='n')   # anchor = 'n' 可使其靠上
        
        # define columns
        columns = ('date', 'county', 'aqi' , 'pm25' ,'status', 'lat' , 'lon' )  # 有五欄

        self.tree = ttk.Treeview(bottomFrame, columns=columns, show='headings')

        # define headings
        self.tree.heading('date', text='date')
        self.tree.heading('county', text='county')
        self.tree.heading('aqi', text='AQI')
        self.tree.heading('pm25', text='PM2.5')
        self.tree.heading('status' , text='Status')
        self.tree.heading('lat', text='Lat')
        self.tree.heading('lon', text='Lon')

        self.tree.column('date', width=120 )
        self.tree.column('county' , width=120  )
        self.tree.column('aqi', width=120 )
        self.tree.column('pm25', width=120 )
        self.tree.column('status', width=120 )
        self.tree.column('lat', width=120 )
        self.tree.column('lon', width=120 )

        # lst = self.getall()
        # for i in lst:
        #     tree.insert("" , "end", values=tuple(i))
    

            # generate sample data
        # contacts = []
        # for n in range(1, 100):
        #     contacts.append((f'first {n}', f'last {n}', f'email{n}@example.com'))

        # # add data to the treeview
        # for contact in contacts:
        #     tree.insert('', tk.END, values=contact)
        

        self.tree.pack(side='right')


        bottomFrame.pack(expand=True,fill='x',padx=20,pady=(0,20),ipadx=10,ipady=10)
        #==============end bottomFrame===============
    
    def sitename_selected(self , event):        # link with event
        print( self.selected_site.get(),'selected')
        selected_data = datasource.get_selected_data(self.selected_site.get())
        for i in selected_data:
            self.tree.insert('', "end", values=i)

    def getall(self):
        lst = datasource.get_all()
        return lst

def main():
    window = Window(theme="arc")
    window.mainloop()

if __name__ == '__main__':
    main()
        

def main():
    window = Window(theme="arc")
    window.mainloop()

if __name__ == '__main__':
    main()