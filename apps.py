from model.barista import Barista
from controller.barista_controller import BaristaController
from datetime import datetime
import names
import numpy as np

def manual_insertion(firstname: str, lastname: str, email: str, phone: str, level: int, bulk=False):
    start = datetime.now()
    barista = Barista(firstname, lastname, email, phone, level)
    controller = BaristaController()
    controller.create_barista(barista)
    end = datetime.now()
    duration = (end - start).seconds
    
    if not bulk:
        print('Barista ' + str(barista) + ' inserted in ' + str(duration) + ' s | Name: ' + barista.firstname + ' ' + barista.lastname + '.')

def bulk_insertion(size=100):
    start = datetime.now()
    controller = BaristaController()

    for _ in range(size):
        firstname = names.get_first_name()
        lastname = names.get_last_name()
        email = firstname.lower() + '@' + lastname.lower() + '.mail'
        phone = str(np.random.randint(low=10000, high=10000000))
        level = np.random.randint(low=1, high=5)

        manual_insertion(firstname, lastname, email, phone, level, bulk=True)
    
    end = datetime.now()
    duration = (end - start).seconds
    print(str(size) + ' Baristas inserted in ' + str(duration) + ' s.')

if __name__ == "__main__":

    insertion_method = input('Insertion method [1: bulk, 0: manual] (leave blank for bulk): ')
    if insertion_method != '':
        insertion_method = int(insertion_method)

        if insertion_method == 0:
            firstname = input('Input firstname of Barista: ')
            while not firstname:
                print('Firstname is required!')
                firstname = input('Input firstname of Barista: ')
            
            lastname = input('Input lastname of Barista: ')
            while not lastname:
                print('Last is required!')
                lastname = input('Input lastname of Barista: ')
            
            email = input('Input email of Barista: ')
            while not email:
                print('Email is required!')
                email = input('Input email of Barista: ')
            
            phone = input('Input phone of Barista: ')
            while not phone:
                print('Phone is required!')
                phone = input('Input phone of Barista: ')
            
            level = input('Input experience level of Barista: ')
            while not level:
                print('Experience level is required!')
                level = input('Input experience level of Barista: ')
            
            manual_insertion(firstname, lastname, email, phone, int(level))
        
        elif insertion_method == 1:
            entries = input('Input number of entries to bulk insert (leave blank for 100): ')
            if entries != '':
                bulk_insertion(size=int(entries))
            else:
                bulk_insertion()
        
        else:
            print('Unknown command!')
    
    else:
        entries = input('Input number of entries to bulk insert (leave blank for 100): ')
        if entries != '':
            bulk_insertion(size=int(entries))
        else:
            bulk_insertion()