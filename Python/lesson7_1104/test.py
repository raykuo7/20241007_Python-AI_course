from tkinter import ttk
import tkinter as tk
from ttkthemes import ThemedTk
from tkinter.messagebox import showinfo

import sqlite3

import requests

def get_sitename(county:str)->list[str]:
   
    conn = sqlite3.connect("AQI.db")

    with conn:
        cursor = conn.cursor()
        sql = '''
            SELECT DISTINCT sitename 
            FROM records
            WHERE county =?
        '''
        cursor.execute(sql,(county, ))
        
        # sitenames = []
        # for i in cursor.fetchall():
        #     sitenames.append(i[0])

        return [i[0] for i in cursor.fetchall()]

def get_selected_data(sitename)->list[list]:
    # url = 'https://data.moenv.gov.tw/api/v2/aqx_p_488?api_key=e8dd42e6-9b8b-43f8-991e-b3dee723a52d&limit=1000&sort=datacreationdate%20desc&format=JSON'
    # try:
    #     response = requests.get(url)
    #     response.raise_for_status()
    #     data = response.json()
    # except Exception as e:
    #     print('e')
    # else:
    #     outer_list = []
        
    #     for i in data['records']:
    #         inner_list = []
    #         if i['sitename'] == sitename:
    #             inner_list.append(i['datacreationdate'])
    #             inner_list.append(i['county'])
    #             inner_list.append(i['aqi'])
    #             inner_list.append(i['pm2.5'])
    #             inner_list.append(i['status'])
    #             inner_list.append(i['latitude'])
    #             inner_list.append(i['longitude'])
    #             outer_list.append(inner_list)

    conn = sqlite3.connect("AQI.db")

    with conn:
        cursor = conn.cursor()
        sql = '''
            SELECT date,county,aqi,pm25,status,lat,lon
            from records 
            WHERE sitename = ?
            ORDER BY date ASC
        '''
        cursor.execute( sql,(sitename ,))
        sitenames = []

        for i in cursor.fetchall():
            sitenames.append(i)

        print(sitenames)
    return sitenames


def get_county()->list[str]:
    '''
    docString
    parameter:
    return:
        傳出所有的城市名稱
    '''
    conn = sqlite3.connect("AQI.db")
    with conn:
        # Create a cursor object to execute SQL commands
        cursor = conn.cursor()
        # SQL query to select unique sitenames from records table
        sql = '''
        SELECT DISTINCT county
        FROM records
        '''
        # Execute the SQL query
        cursor.execute(sql)
        # Get all results and extract first item from each row into a list
        counties = [items[0] for items in cursor.fetchall()]
    
    # Return the list of unique sitenames
    return counties
 
    
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
            #==============SelectedFrame===============
        selectedFrame= ttk.Frame(self,padding=[10,10,10,10])

        counties = get_county()


        
        # sitenames.insert(0,'請選擇站點')
        
        self.selected_county = tk.StringVar()     ## 一定要加self
        
        sitenames_cb = ttk.Combobox(selectedFrame, textvariable= self.selected_county,state='readonly')
        sitenames_cb.configure(values=counties)
        sitenames_cb.set('請選擇conty')
        sitenames_cb.bind('<<ComboboxSelected>>', self.county_selected)   # link with event(use "bind")  diffferent from link with commend(use "commend")
         # anchor = 'n' 可使其靠上
        sitenames_cb.pack(anchor='n',pady=10) 
        # listbox choses site

        self.li = []
        self.var = tk.Variable(value=self.li)
        listbox = tk.Listbox(
            selectedFrame,
            listvariable=self.var,
            height=6,
            selectmode=tk.EXTENDED
        )
        listbox.pack()
        selectedFrame.pack(side='left',expand=True,fill='y',padx=(20,0))
            #==============End SelectedFrame=============== 
    
        

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



        self.tree.pack(side='right')


        bottomFrame.pack(expand=True,fill='x',padx=20,pady=(0,20),ipadx=10,ipady=10)
        #==============end bottomFrame===============
    
    
    def county_selected(self, event):
        selected = self.selected_county.get()
        a = get_sitename(selected)
        self.var.set(a)
        print(selected)
    
    def sitename_selected(self , event):        # link with event
        print( self.selected_site.get(),'selected')

        # 清除 Treeview 中的舊資料
        for item in self.tree.get_children():
            self.tree.delete(item)


        selected_data = get_selected_data(self.selected_site.get())
        for i in selected_data:
            self.tree.insert('', "end", values=i)


def main():
    window = Window(theme="arc")
    window.mainloop()

if __name__ == '__main__':
    main()
    