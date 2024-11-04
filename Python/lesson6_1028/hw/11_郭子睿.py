from tkinter import ttk
import tkinter as tk
from ttkthemes import ThemedTk
from tkinter.messagebox import showinfo

import sqlite3

import requests

def get_sitename()->list[str]:
    url = 'https://data.moenv.gov.tw/api/v2/aqx_p_488?api_key=e8dd42e6-9b8b-43f8-991e-b3dee723a52d&limit=1000&sort=datacreationdate%20desc&format=JSON'
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
    except Exception as e:
        print('e')
    else:
        sitenames = set()
        for items in data['records']:
            sitenames.add(items['sitename'])

        sitenames = list(sitenames)
        return sitenames

def get_selected_data(sitename)->list[list]:
    url = 'https://data.moenv.gov.tw/api/v2/aqx_p_488?api_key=e8dd42e6-9b8b-43f8-991e-b3dee723a52d&limit=1000&sort=datacreationdate%20desc&format=JSON'
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
    except Exception as e:
        print('e')
    else:
        outer_list = []
        
        for i in data['records']:
            inner_list = []
            if i['sitename'] == sitename:
                inner_list.append(i['datacreationdate'])
                inner_list.append(i['county'])
                inner_list.append(i['aqi'])
                inner_list.append(i['pm2.5'])
                inner_list.append(i['status'])
                inner_list.append(i['latitude'])
                inner_list.append(i['longitude'])
                outer_list.append(inner_list)

        
        return outer_list
    
    
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
        selected_data = get_selected_data(self.selected_site.get())
        for i in selected_data:
            self.tree.insert('', "end", values=i)


def main():
    window = Window(theme="arc")
    window.mainloop()

if __name__ == '__main__':
    main()
        


#=================================================#

sql = '''
CREATE TABLE IF NOT EXISTS records (
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	sitename TEXT NOT NULL,
	county TEXT,
	aqi INTEGER,
	status TEXT,
	pm25 NUMERIC,
	date TEXT,
	lat NUMERIC,
	lon NUMERIC
);
'''

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect("AQI.db")

# Create a cursor object
cursor = conn.cursor()

# Create a table
cursor.execute(sql)

# Commit changes and close the connection
conn.commit()
cursor.close()
conn.close()