from fields import Phone, Name, Birthday

class Record:

    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None
    
    def add_phone(self, phone):
        self.phones.append(Phone(phone))
    
    def find_phone(self, phone):
        for el in self.phones:
            if el.value == phone:
                return el
        
        return None
    
    def remove_phone(self, phone):
        element = self.find_phone(phone)

        if element:
            self.phones.remove(element)
        
        else:
            raise ValueError('Phone not found!')
    
    def edit_phone(self, old_number, new_number):
        element = self.find_phone(old_number)

        if not element:
            raise ValueError('Phone not found!')
        
        else:
            
            self.remove_phone(old_number)
            self.add_phone(new_number)
    
    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)       
        
    def __str__(self):
        return f'Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}'