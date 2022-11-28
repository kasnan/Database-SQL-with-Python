import tkinter
import tkinter.ttk
from database import Db_

class Window:
    def __init__(self, title):
        Window.window_ = tkinter.Tk()
        Window.window_.title(title)
        Window.window_.geometry("640x480+100+100")
        Window.window_.resizable=(False, False)
        Window.in_text = ""
        Window.table_tog = 0
    
    def AddDB(self, db):
        Window.db = db

    def AddButton(self, title, color, font_color):
        Window.inputBtn = tkinter.Button(Window.window_,text=title,bg=color,fg=font_color,command=Window.pressed)
        Window.inputBtn.grid(column=1,row=0)

    def AddTextBox(self,width):
        Window.inputBox = tkinter.Entry(Window.window_,width=width)
        Window.inputBox.grid(column=0,row=0)

    def AddTreeView(self):
        Window.tableView = tkinter.ttk.Treeview(Window.window_,
            column=["id","customer"],
            displaycolumns=["id","customer"])
            
        Window.tableView.grid(column=0,row=1)

        Window.tableView.column("id",width=100,anchor="center")
        Window.tableView.heading("id",text="ID",anchor="center")

        Window.tableView.column("customer",width=100,anchor="center")
        Window.tableView.heading("customer",text="고객이름",anchor="center")

        Window.tableView["show"]="headings"

    def SetTreeView(Fetchresult):
        for i in range(len(Fetchresult)):
            Window.tableView.insert("","end",text="",values=Fetchresult[i],iid=i)

    def ClearTable(table):
        for row in table.get_children():
            table.delete(row)

    def pressed():
        Window.in_text = Window.inputBox.get()
        Window.inputBox.delete(0,"end")
        print(Window.in_text)
        Window.FetchResult = Window.db.FetchQuery(Window.in_text)
        Window.ClearTable(Window.tableView)
        Window.SetTreeView(Fetchresult=Window.FetchResult)



    def Return_intext():
        return Window.in_text    

    def Popwindow(self):
        Window.window_.mainloop()
        
