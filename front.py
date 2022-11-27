import tkinter

from window import Window
from database import Db_


#access database(.accdb) file
db1 = Db_('db1.accdb')

#create window object
w1 = Window("Main Window")
w2 = Window("customer list")


#property for w2
w2.AddTextBox(15)
w2.AddButton("확인","blue","white")
w2.AddDB(db1)
w2.AddTreeView()

w2.Popwindow()







