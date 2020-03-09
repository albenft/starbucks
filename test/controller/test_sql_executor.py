import unittest
import credentials
import datetime
from controller.sql_executor import SqlExecutor

class TestSqlExecutor(unittest.TestCase):
    def test_construction(self):
        self.assertIsNotNone(SqlExecutor(credentials.DB_HOST, credentials.DB_USERNAME, credentials.DB_PASSWORD, credentials.DB_DATABASE))
    
    def test_connection(self):
        executor = SqlExecutor(credentials.DB_HOST, credentials.DB_USERNAME, credentials.DB_PASSWORD, credentials.DB_DATABASE)
        self.assertIsNotNone(executor.open_connection())
    
    def test_fetch_one(self):
        actual_value = (1, 'Alben', 'Tumanggor', 'alben@tumanggor.mail', '6281234567890', 1, 1, datetime.datetime(2020, 3, 9, 22, 26, 13), datetime.datetime(2020, 3, 9, 22, 26, 13))

        executor = SqlExecutor(credentials.DB_HOST, credentials.DB_USERNAME, credentials.DB_PASSWORD, credentials.DB_DATABASE)
        query = 'SELECT * FROM barista WHERE id=1'

        self.assertEqual(executor.fetch_one(query), actual_value)
    
    def test_insertion(self):
        table = 'barista'
        columns = ('id','firstname','lastname','email','phone','level')
        values = (2, 'John', 'Doe', 'john@doe.mail', '770883658', 2)

        executor = SqlExecutor(credentials.DB_HOST, credentials.DB_USERNAME, credentials.DB_PASSWORD, credentials.DB_DATABASE)
        executor.insert(table, columns, values)

        query = 'SELECT * FROM barista WHERE id=2'
        self.assertIsNotNone(executor.fetch_one(query))

if __name__ == '__main__':
    unittest.main()