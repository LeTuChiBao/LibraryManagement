import pyodbc

class MSSQLConnection:
    def __init__ (self, driver = 'SQL Server',server = 'MSI\SQLEXPRESS',database = 'QLThuVien',username = '',password = ''):
        self.driver = driver
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        self.connection = None

    def connect(self):
        try:
            self.connection = pyodbc.connect(f'DRIVER={self.driver};SERVER={self.server};DATABASE={self.database};UID={self.username};PWD={self.password}')
            #print('Connection successful!')
        except Exception as E:
            print('Error in connection: ',E)

    def query(self,sql):
        cursor = self.connection.cursor()
        cursor.execute(sql)
        return cursor.fetchall()

    def update(self,sql):
        cursor = self.connection.cursor()
        cursor.execute("SET DATEFORMAT DMY")
        cursor.execute(sql)
        self.connection.commit()

    def insert(self, sql):
        cursor = self.connection.cursor()
        cursor.execute("SET DATEFORMAT DMY")
        cursor.execute(sql)
        self.connection.commit()

    def delete(self, sql):
        cursor = self.connection.cursor()
        cursor.execute(sql)
        self.connection.commit()

    def close(self):
        if self.connection:
            self.connection.close()
            # print('Connection closed!')
