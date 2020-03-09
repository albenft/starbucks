import unittest
from model.barista import Barista

# Valid Value
firstname = 'John'
lastname = 'Doe'
phone = '628123456789'
email = 'john@doe.mail'
level = 1

class TestBarista(unittest.TestCase):
    def test_firstname_type(self):
        with self.assertRaises(TypeError) as m: 
            Barista(808, lastname, email, phone, level)

    def test_lastname_type(self):
        with self.assertRaises(TypeError) as m: 
            Barista(firstname, True, email, phone, level)
    
    def test_phone_type(self):
        with self.assertRaises(TypeError) as m: 
            Barista(firstname, lastname, email, [1,2,3], level)
    
    def test_email_type(self):
        with self.assertRaises(TypeError) as m: 
            Barista(firstname, lastname, 99, phone, level)

    def test_level_type(self):
        with self.assertRaises(TypeError) as m: 
            Barista(firstname, lastname, email, phone, 'junior')
    
    def test_firstname_value(self):
        with self.assertRaises(ValueError) as m:
            Barista('name01', lastname, email, phone, level)

    def test_lastname_value(self):
        with self.assertRaises(ValueError) as m:
            Barista(firstname, 'name02', email, phone, level)
    
    def test_email_value(self):
        with self.assertRaises(ValueError) as m:
            Barista(firstname, lastname, 'mailnotfollowingformat', phone, level)

    def test_phone_value(self):
        with self.assertRaises(ValueError) as m:
            Barista(firstname, lastname, email, 'stringphonenumber', level)

    def test_level_value(self):
        with self.assertRaises(ValueError) as m:
            Barista(firstname, lastname, email, phone, 0)

if __name__ == '__main__':
    unittest.main()