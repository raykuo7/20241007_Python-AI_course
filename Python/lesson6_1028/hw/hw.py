from tkinter import ttk
import tkinter as tk
from ttkthemes import ThemedTk
from tkinter.messagebox import showinfo

import sqlite3

import requests

def updated_data() -> list[list]:
    
    link = 'https://data.moenv.gov.tw/api/v2/aqx_p_488?api_key=e8dd42e6-9b8b-43f8-991e-b3dee723a52d&limit=1000&sort=datacreationdate%20desc&format=JSON'

    try:
        response = requests.get(link)
        response.raise_for_status()
        data = response.json()
    except Exception as e:
        print(e)
    
    else:
        conn = sqlite3.connect("AQI.db")
        with conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM records")
            conn.commit()  # 確保刪除操作被提交
            
            for items in data['records']:
                sitename = items['sitename']
                county = items['county']
                aqi = int(items['aqi']) if items['aqi'] != '' else 0
                status = items['status']
                pm25 = float(items['pm2.5']) if items['pm2.5'] != '' else 0.0
                date = items['datacreationdate']
                lon = float(items['longitude']) if items['longitude'] != '' else 0.0
                lat = float(items['latitude']) if items['latitude'] != '' else 0.0
                sql = '''INSERT OR IGNORE INTO records(sitename,county,aqi,status,pm25,date,lat,lon)
                        values (?,?, ?, ?,?,?,?,?);
                '''
                cursor.execute(sql,(sitename, county, aqi, status,pm25,date,lat,lon))

            conn.commit()



def get_sitename()->list[str]:

    conn = sqlite3.connect("AQI.db")

    with conn:
        cursor = conn.cursor()
        sql = '''
            SELECT DISTINCT sitename
            from records
        '''
        cursor.execute(sql)
        return [i[0] for i in cursor.fetchall()]

def get_selected_data(sitename)->list[list]:

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
        sitenames = get_sitename()
        
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



        self.tree.pack(side='right')


        bottomFrame.pack(expand=True,fill='x',padx=20,pady=(0,20),ipadx=10,ipady=10)
        #==============end bottomFrame===============
    
    def sitename_selected(self , event):        # link with event
        print( self.selected_site.get(),'selected')

        # 清除 Treeview 中的舊資料
        for item in self.tree.get_children():
            self.tree.delete(item)


        selected_data = get_selected_data(self.selected_site.get())
        for i in selected_data:
            self.tree.insert('', "end", values=i)


def main():
    updated_data()
    window = Window(theme="arc")
    window.mainloop()

if __name__ == '__main__':
    main()
    