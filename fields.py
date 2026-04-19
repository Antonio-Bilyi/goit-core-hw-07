from datetime import datetime

class Field:

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):

    def __init__(self, value):
        super().__init__(value)

class Phone(Field):

    def __init__(self, value):
        if value.isdigit() and len(value) == 10:
            super().__init__(value)
        
        else:
            raise ValueError('Invalid phone number')

class Birthday(Field):

    def __init__(self, value):
        try:
            datetime.strptime(value, '%d.%m.%Y')
            super().__init__(value)

        except ValueError:
            raise ValueError('Invalid date format. Use DD.MM.YYYY')