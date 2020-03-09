import mysql.connector

class SqlExecutor():
    def __init__(self, host, username, password, database):
        self.host = host
        self.username = username
        self.password = password
        self.database = database
    
    def open_connection(self):
        return mysql.connector.connect(host=self.host, user=self.username, passwd=self.password, database=self.database)
    
    def fetch_one(self, query):
        connection = self.open_connection()
        cursor = connection.cursor()
        cursor.execute(query)
        result = cursor.fetchone()
        cursor.close()
        connection.close()

        return result
    
    def insert(self, table, columns, values):
        columns = "".join(column + ", " for column in columns)[:-2]
        sql = "INSERT INTO " + table + "(" + columns + ")" + " VALUES (" + "".join("%s, " for _ in range(len(values)))[:-2] + ")"
        connection = self.open_connection()
        cursor = connection.cursor()
        cursor.execute(sql, values)
        connection.commit()
        cursor.close()
        connection.close()