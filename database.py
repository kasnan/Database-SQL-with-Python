import pyodbc

class Db_:
    
    def __init__(self,filename):
        #path_laptop='C:/Users/kasna/Documents/vsworkspace/Pyworkspace/pyodbc-database-with-graphic/'
        path_desktop='C:/Users/kasna/Documents/workspace/py/pyodbc-database-with-graphic/'
        Db_.conn=pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ='+path_desktop+filename+';')
        Db_.cursor = Db_.conn.cursor()
    
    def testquery(self):
        Db_.cursor.execute('select * from 고객')
        for row in Db_.cursor.fetchall():
            print(row)
    
    def ExecQuery(self, query):
        Db_.cursor.execute(query)
        for row in Db_.cursor.fetchall():
            print(row)

    def FetchQuery(self, query):
        Db_.cursor.execute(query)
        return Db_.cursor.fetchall()


