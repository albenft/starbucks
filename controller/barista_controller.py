from controller.sql_executor import SqlExecutor
from model.barista import Barista
import credentials

class BaristaController():
    def create_barista(self, barista: Barista):
        if not isinstance(barista, Barista):
            raise TypeError
        else:
            table = 'barista'
            columns = ('firstname','lastname','email','phone','level')
            values = (barista.firstname, barista.lastname, barista.email, barista.phone, barista.level)

            executor = SqlExecutor(credentials.DB_HOST, credentials.DB_USERNAME, credentials.DB_PASSWORD, credentials.DB_DATABASE)
            executor.insert(table, columns, values)