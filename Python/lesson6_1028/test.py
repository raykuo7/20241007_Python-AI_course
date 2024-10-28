from tkinter import *
from tkinter import ttk
#Create an instance of Tkinter frame or window
win= Tk()
#Set the geometry of tkinter frame
win.geometry("750x250")
#Create a Combobox
combobox= ttk.Combobox(win,state= "readonly")
combobox['values']=('C++','Java','Python')
combobox.current(2)
combobox.pack(pady=30, ipadx=20)
win.mainloop()