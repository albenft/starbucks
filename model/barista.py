import re
import model.pattern_template as pat

class Barista():
    def __init__(self, firstname, lastname, email, phone, level):

        # validating data type
        if not isinstance(firstname, str):
            raise TypeError('Wrong Type in firstname')
        if not isinstance(lastname, str):
            raise TypeError('Wrong Type in lastname')
        if not isinstance(email, str):
            raise TypeError('Wrong Type in email')
        if not isinstance(phone, str):
            raise TypeError('Wrong Type in phone')
        if not isinstance(level, int):
            raise TypeError('Wrong Type in level')

        # validating value
        if re.match(pat.FIRSTNAME_REGEX, firstname):
            self.firstname = firstname
        else:
            raise ValueError('firstname should only contains letter')

        if re.match(pat.LASTNAME_REGEX, lastname):
            self.lastname = lastname
        else:
            raise ValueError('lastname should only contains letter')

        if re.match(pat.EMAIL_REGEX, email):
            self.email = email
        else:
            raise ValueError('email does not follow desired format')

        if re.match(pat.PHONE_REGEX, phone):
            self.phone = phone
        else:
            raise ValueError('phone should only contains number')

        if level > 0:
            self.level = level
        else:
            raise ValueError('level should be in positive value')