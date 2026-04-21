from decorators import input_error
from addressbook import AddressBook
from record import Record

@input_error
def add_birthday(args, book: AddressBook):
    if len(args) < 2:
        raise ValueError('Give me please name and birthday')
    
    name, birthday, *_ = args
    record = book.find(name)

    record.add_birthday(birthday)
    return f'Birthday added for {name}'

@input_error
def show_birthday(args, book: AddressBook):
    name, *_ = args
    record = book.find(name)

    if record:
        if record.birthday:
            return f"{name}'s birthday is {record.birthday.value}"
        else:
          return f"'Contact {name} doesn't have a birthday set"    

@input_error
def birthdays(book: AddressBook):
    upcoming_birthdays = book.get_upcoming_birthday()

    if not upcoming_birthdays:
        return 'No upcoming birthdays'
    
    result = []
    for el in upcoming_birthdays:
        result.append(f"{el['name']}: {el['congratulation_date']}") 
    
    return "\n".join(result)