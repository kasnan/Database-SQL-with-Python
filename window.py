import tkinter
import tkinter.ttk
from database import Db_

class Window:
    col_index=0
    row_index=0

    def __init__(self, title):
        Window.window_ = tkinter.Tk()
        Window.window_.title(title)
        Window.window_.geometry("640x480+100+100")
        Window.window_.resizable=(False, False)
        Window.in_text = ""
        Window.table_tog = 0
    
    def AddDB(self, db):
        Window.db = db

    def Popwindow(self):
        Window.window_.mainloop()
        
