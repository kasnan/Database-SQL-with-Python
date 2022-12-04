from tkinter import *
import tkinter.ttk

from database import Db_

global columns
global tableView
global tv1
global db_list

def onselect(event):
    print("callback")
    for row in tableView.get_children():
        tableView.delete(row)
    
    selected_iid = tv1.focus()
    item_index = tv1.item(selected_iid)
    value = item_index.get('values')[0]
    print(value)
    
    Fetchresult = db1.FetchQuery("select * from "+value)
    columns = db1.GetColumns()
    print(columns)

    tableView.config(column=columns,displaycolumns=columns)
    for col in range(len(columns)):
        tableView.column(columns[col],width=100,anchor="center")
        tableView.heading(columns[col],text=columns[col],anchor="center")
    for i in range(len(Fetchresult)):
            tableView.insert("","end",text="",values=Fetchresult[i],iid=i)


#access database(.accdb) file and test it
db1 = Db_('db1.accdb')
Fetchresult = db1.FetchQuery("select * from customer_sign")

#test getcolumns
columns = db1.GetColumns()
print(columns)

w1 = Tk("PUSH AN ITEM")
w1.title("Control Panel")
w1.geometry("480x480")
frame_w1=Frame(w1)
frame_w1.grid(column=0,row=0)
frame_w1_2 = Frame(w1)
frame_w1_2.grid(column=1,row=0)

scrollbar = Scrollbar(frame_w1)
scrollbar.pack(sid="right", fill="both")


tableView = tkinter.ttk.Treeview(frame_w1_2,
            height=10,
            column=["id","customer"],
            displaycolumns=["id","customer"])
tableView.pack(side="left",fill="both")
tableView["show"]="headings"
db_list = ["customer_sign","customer_list","account","account_list",
            "withdraw","portfolio","dailygain","dailygain"]


def addlowerMenu(upper_tree, text):
    tv1.insert(upper_tree,"end",text=text,values=text,tag=upper_tree+"_"+text)

tv1 = tkinter.ttk.Treeview(frame_w1, height=10, yscrollcommand=scrollbar.set)

info_tree = tv1.insert("","end",text="메뉴",values="메뉴",iid="menu")

customer_tree = tv1.insert(info_tree,"end",text="고객",values="고객",iid="customer")
addlowerMenu(customer_tree,"customer_sign")
addlowerMenu(customer_tree,"customer_list")

acc_tree = tv1.insert(info_tree,"end",text="account",values="account",iid="account")
addlowerMenu(acc_tree,"account")
addlowerMenu(acc_tree,"account_list")

addlowerMenu(info_tree,"withdraw")

port_tree = tv1.insert(info_tree,"end",text="조회",values="조회",iid="portfolio")
addlowerMenu(port_tree,"portfolio")

addlowerMenu(info_tree,"dailygain")


# for line in range(len(db_list)):
#     tv1.insert(info_tree,"end",text=db_list[line],values=db_list[line],tag="tag1")
#tv1.tag_bind("tag1","<<TreeviewSelect>>", callback=onselect)
tv1.bind("<Double-1>",onselect)
tv1.pack(side="left", fill="both")
scrollbar.config(command=tv1.yview)

# list = Listbox(frame_w1, height=10,yscrollcommand=scrollbar.set)
# for line in range(len(db_list)):
#     list.insert(END, db_list[line])
#     list.activate(line)
# list.bind('<<ListboxSelect>>', onselect)
# list.pack(side="left", fill="both")
# scrollbar.config(command=list.yview)


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