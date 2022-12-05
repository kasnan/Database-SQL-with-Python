from tkinter import *
import tkinter.ttk

from database import Db_


#access database(.accdb) file and test it
db1 = Db_('db1.accdb')
Fetchresult = db1.FetchQuery("select * from customer_sign")

global columns
columns = db1.GetColumns()
print(columns)

w1 = Tk("PUSH AN ITEM")
w1.title("Control Panel")
w1.geometry("480x480")
frame_w1=Frame(w1)
frame_w1.grid(column=0,row=0)
frame_w1_2 = Frame(w1)
frame_w1_2.grid(column=1,row=0)

# global w2
# w2 = Toplevel()
# w2.title("Display of table")
# w2.geometry("400x400")
# w2.withdraw()

# global table_tog
# table_tog = 0

# def tog_pressed(evt):
#     global table_tog

#     if table_tog == 1:
#         w2.deiconify()
#         table_tog=0
#     else:
#         w2.withdraw()
#         table_tog=1
scrollbar = Scrollbar(frame_w1)
scrollbar.pack(sid="right", fill="both")


#for listbox
def onselect(evt):
    for row in tableView.get_children():
        tableView.delete(row)
    w = evt.widget
    index = int(w.curselection()[0])
    value = w.get(index)
    Fetchresult = db1.FetchQuery("select * from "+value)

    columns = db1.GetColumns()
    print(columns)
    tableView.config(column=columns,displaycolumns=columns)
    for col in range(len(columns)):
        tableView.column(columns[col],width=100,anchor="center")
        tableView.heading(columns[col],text=columns[col],anchor="center")
    for i in range(len(Fetchresult)):
            tableView.insert("","end",text="",values=Fetchresult[i],iid=i)

#for listTree
# def onselect(evt):
#     for row in tableView.get_children():
#         tableView.delete(row)
#     w = evt.widget
#     index = int(w.selection())
#     print(index)
#     value = w.get(index)
#     Fetchresult = db1.FetchQuery("select * from "+value)

#     columns = db1.GetColumns()
#     print(columns)
#     tableView.config(column=columns,displaycolumns=columns)
#     for col in range(len(columns)):
#         tableView.column(columns[col],width=100,anchor="center")
#         tableView.heading(columns[col],text=columns[col],anchor="center")
#     for i in range(len(Fetchresult)):
#             tableView.insert("","end",text="",values=Fetchresult[i],iid=i)


    # tog_pressed(evt)
global tableView
tableView = tkinter.ttk.Treeview(frame_w1_2,
            height=10,
            column=["id","customer"],
            displaycolumns=["id","customer"])
tableView.pack(side="left",fill="both")
tableView["show"]="headings"
db_list = ["customer_sign","customer_list","account","account_list",
            "withdraw","portfolio","dailygain","dailygain"]

list = Listbox(frame_w1, height=10,yscrollcommand=scrollbar.set)
for line in range(len(db_list)):
    list.insert(END, db_list[line])
    list.activate(line)
list.bind('<<ListboxSelect>>', onselect)
list.pack(side="left", fill="both")

scrollbar.config(command=list.yview)

# listtree = tkinter.ttk.Treeview(frame_w1, height=10,
#      yscrollcommand=scrollbar.set)
# for line in range(len(db_list)):
#     listtree.insert('',line,text=db_list[line])
# listtree.bind('<ButtonRelease-1>', onselect)
# listtree.pack(side="left", fill="both")

# scrollbar.config(command=listtree.yview)


#table for w2
# tableView = tkinter.ttk.Treeview(w2,
#             column=["id","customer"],
#             displaycolumns=["id","customer"])
# tableView.grid(column=0,row=0)
# tableView.column("id",width=100,anchor="center")
# tableView.heading("id",text="ID",anchor="center")
# tableView.column("customer",width=100,anchor="center")
# tableView.heading("customer",text="고객이름",anchor="center")
# tableView["show"]="headings"

w1.mainloop()