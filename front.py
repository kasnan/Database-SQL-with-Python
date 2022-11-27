import tkinter
import pyodbc

conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:/Users/kasna/Documents/workspace/py/PYgui/db1.accdb;')
cursor = conn.cursor()
cursor.execute('select * from 고객')

for row in cursor.fetchall():
    print (row)

window=tkinter.Tk()
window.mainloop()