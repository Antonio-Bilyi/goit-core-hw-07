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
        old_element = self.find_phone(old_number)

        if not old_element:
            raise ValueError('Phone not found!')
        
        else:
            new_element = Phone(new_number)

            index = self.phones.index(old_element)
            self.phones[index] = new_element
            
            
    
    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)       
        
    def __str__(self):
        message = f'Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}'

        if self.birthday:
            message += f', birthday: {self.birthday.value}'
        
        return message