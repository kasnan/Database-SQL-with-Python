from tkinter import *
import tkinter.ttk

from database import Db_

import datetime

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

def subWindow(button):
    print("service for",button)
    w_tmp = Tk("PUSH AN ITEM")
    w_tmp.title(str(button))
    w_tmp.geometry("320x240")
    globals()["w_"+button](w_tmp,button)

def getBalance(textbox, frame,balance_txt,manual_text) :
    name = textbox.get()
    print(name)

    id = str(db1.FetchQuery(f"select id from customer_sign where customer_name like '{name}';")[0][0])
    balance = db1.FetchQuery(f"select balance from account_list where id = {id};")[0][0]
    w_money = db1.FetchQuery(f"select amount from withdraw where id = {id};")
    for i in range(len(w_money)):
        balance -= w_money[i][0]

    balance = str(balance)
    balance_txt.config(text="총 가치 : "+balance+"원")
    manual_text.config(text=name)


def w_customer_list(window, button):

    f1 = Frame(window)
    f1.grid(column=0,row=0,columnspan=2)
    f2 = Frame(window)
    f2.grid(column=0,row=1,columnspan=2)
    f3 = Frame(window)
    f3.grid(column=0,row=2)
    f3_2 = Frame(window)
    f3_2.grid(column=1,row=2)
    manual_text = Label(f1, text="이름을 입력하세요", width=20, height=1, fg="black", relief="solid")
    manual_text.pack(side="top",fill="both")
    
    textbox = Entry(f2,width=20)
    textbox.pack(sid="left",fill="both")
    textbox_but = Button(f2,text="입력",command=lambda: getBalance(textbox,f3,balance_txt,manual_text))
    textbox_but.pack(sid="right",fill="both")

    balance = "NULL"
    balance_txt = Label(f3, text="총 가치 : "+balance+"원", width=20, height=1, fg="black")
    balance_txt.pack(side="left",fill="both")

    try_withdraw = Label(f3_2, text="출금하시겠습니까?", width=20, height=1, fg="black")
    try_withdraw.pack(side="top",fill="both")
    
    try_withdraw_but = Button(f3_2,text="withdraw")
    try_withdraw_but.config(command=lambda m=try_withdraw_but.cget('text'): subWindow(m))
    
    
    try_withdraw_but.pack(sid="bottom",fill="both")

    window.mainloop()

def withdrawMoney(textbox,textbox2,proc):
    name = textbox.get()
    print(name)

    id = db1.FetchQuery(f"select id from customer_sign where customer_name like '{name}';")[0][0]
    balance = db1.FetchQuery(f"select balance from account_list where id = {id};")[0][0]

    w_money = db1.FetchQuery(f"select amount from withdraw where id = {id};")
    for i in range(len(w_money)):
        balance -= w_money[i][0]

    money = int(textbox2.get())
    print(money)
    #id, amount, w_date
    date = datetime.date.today().strftime("%Y-%m-%d") 
    if money <= balance:
        db1.ExecQuery(f"insert into withdraw(id, amount,w_date) values ({id}, {money}, '{date}')")
        db1.save()
        proc.pack(side="bottom",fill="both")

    else:
        print("error!")


def w_withdraw(window, button):
    f1 = Frame(window)
    f1.grid(column=0,row=0,columnspan=2)
    f2 = Frame(window)
    f2.grid(column=0,row=1,columnspan=2)
    f3 = Frame(window)
    f3.grid(column=0,row=2,columnspan=2)
    manual_text = Label(f1, text="이름과 출금액을 입력하세요", width=30, height=1, fg="black", relief="solid")
    manual_text.pack(side="top",fill="both")

    textbox = Entry(f2,width=10)
    textbox.pack(sid="left",fill="both")

    proc_text = Label(f3, text="작업이 완료되었습니다!", width=30, height=1, fg="black")
    

    textbox2 = Entry(f2,width=7)
    textbox2.pack(sid="left",fill="both")
    textbox_but2 = Button(f2,text="입력",command=lambda: withdrawMoney(textbox,textbox2,proc_text))
    textbox_but2.pack(sid="right",fill="both")


#access database(.accdb) file
db1 = Db_('db1.accdb')

db_list = ["customer_sign","customer_list","account","account_list",
            "withdraw","portfolio","dailygain","dailygain_tot"]

w1 = Tk("PUSH AN ITEM")
w1.title("Control Panel")
w1.geometry("640x480")
w1.resizable(False,False)

frame_w1=Frame(w1)
frame_w1.grid(column=0,row=0)
frame_w1_2 = Frame(w1)
frame_w1_2.grid(column=1,row=0)
frame_w2=Frame(w1)
frame_w2.grid(column=0,row=1)
frame_w2_2 = Frame(w1)
frame_w2_2.grid(column=1,row=1)
frame_w3=Frame(w1)
frame_w3.grid(column=0,row=2,columnspan=2)


scrollbar = Scrollbar(frame_w1)
scrollbar.pack(sid="right", fill="both")

tableView = tkinter.ttk.Treeview(frame_w1_2,
            height=10,
            column=["id","customer"],
            displaycolumns=["id","customer"])
tableView.pack(side="left",fill="both")
tableView["show"]="headings"

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
addlowerMenu(info_tree,"dailygain_tot")

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

Button_box = []
for i in range(len(db_list)):
    Button_box.append(Button(frame_w3,text=db_list[i],command=lambda m=db_list[i]: subWindow(m)))
for i in range(len(db_list)):
    Button_box[i].pack(sid="left",fill="both")


w1.mainloop()