from tkinter import *
import tkinter.ttk

from database import Db_

global columns
global tableView
global tv1
global db_list

#tableViewer of database (for tag "lower")
def onselect(event):
    for row in tableView.get_children():
        tableView.delete(row)
    
    selected_iid = tv1.focus()
    item_index = tv1.item(selected_iid)
    value = item_index.get('values')[0]
    
    Fetchresult = db1.FetchQuery("select * from "+value)
    columns = db1.GetColumns()

    tableView.config(column=columns,displaycolumns=columns)
    for col in range(len(columns)):
        tableView.column(columns[col],width=100,anchor="center")
        tableView.heading(columns[col],text=columns[col],anchor="center")
    for i in range(len(Fetchresult)):
            tableView.insert("","end",text="",values=list(Fetchresult[i]),iid=i)

def inputQuery():
    cmd_input = textbox.get()
    print(cmd_input)
    if(cmd_input == "clear"):
        for row in tableView.get_children():
            tableView.delete(row)
        for row in tableView2.get_children():
            tableView2.delete(row)
        textbox.delete(0,"end")
        return
    for row in tableView2.get_children():
        tableView2.delete(row)
    
    
    Fetchresult = db1.FetchQuery(cmd_input)
    columns = db1.GetColumns()

    tableView2.config(column=columns,displaycolumns=columns)
    for col in range(len(columns)):
        tableView2.column(columns[col],width=100,anchor="center")
        tableView2.heading(columns[col],text=columns[col],anchor="center")
    for i in range(len(Fetchresult)):
            tableView2.insert("","end",text="",values=list(Fetchresult[i]),iid=i)

    textbox.delete(0,"end")


#access database(.accdb) file and test it
db1 = Db_('db1.accdb')

w1 = Tk("PUSH AN ITEM")
w1.title("Control Panel")
w1.geometry("480x480")
frame_w1=Frame(w1)
frame_w1.grid(column=0,row=0)
frame_w1_2 = Frame(w1)
frame_w1_2.grid(column=1,row=0)
frame_w2=Frame(w1)
frame_w2.grid(column=0,row=1)
frame_w2_2 = Frame(w1)
frame_w2_2.grid(column=1,row=1)
frame_w3=Frame(w1)
frame_w3.grid(column=0,row=2)
frame_w3_2=Frame(w1)
frame_w3_2.grid(column=1,row=2)

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
    tv1.insert(upper_tree,"end",text=text,values=text,tag="lower")

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

tv1.tag_bind("lower","<Double-1>",onselect)
# tv1.bind("<Double-1>",onselect)
tv1.pack(side="left", fill="both")
scrollbar.config(command=tv1.yview)

textbox = Entry(frame_w2,width=20)
textbox.pack(sid="left",fill="both")

textbox_but = Button(frame_w2,text="cmd Enter",command=inputQuery)
textbox_but.pack(sid="right",fill="both")

tableView2 = tkinter.ttk.Treeview(frame_w2_2,
            height=10,
            column=["id","customer"],
            displaycolumns=["id","customer"])
tableView2.pack(side="left",fill="both")
tableView2["show"]="headings"


w1.mainloop()