import pyodbc

class Db_:
    
    def __init__(self,filename):

        Db_.conn=pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:/Users/kasna/Documents/workspace/py/PYgui/'+filename+';')
        Db_.cursor = Db_.conn.cursor()
    
    def testquery(self):
        Db_.cursor.execute('select * from 고객')
        for row in Db_.cursor.fetchall():
            print(row)


