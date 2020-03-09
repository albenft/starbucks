import unittest
from controller.barista_controller import BaristaController
from model.barista import Barista
from controller.sql_executor import SqlExecutor
import credentials

class TestBaristaController(unittest.TestCase):
    def test_create_barista_type(self):
        with self.assertRaises(TypeError):
            BaristaController.create_barista(6)
    
    def test_create_barista(self):
        barista = Barista('Scarlett', 'Johansson', 'mail@scarlett.johansson','88746442',3)
        controller = BaristaController()
        controller.create_barista(barista)

        executor = SqlExecutor(credentials.DB_HOST, credentials.DB_USERNAME, credentials.DB_PASSWORD, credentials.DB_DATABASE)
        query = "SELECT * FROM barista WHERE firstname='Scarlett' AND lastname='Johansson' AND email='mail@scarlett.johansson' AND phone='88746442'"
        self.assertIsNotNone(executor.fetch_one(query))

if __name__ == '__main__':
    unittest.main()