from decorators import input_error
from addressbook import AddressBook
from record import Record

@input_error
def add_contacts(args, book: AddressBook):
    name, phone, *_ = args
    record = book.find(name)
    message = 'Contact updated.'

    if record is None:
        record = Record(name)
        book.add_record(record)
        message = 'Contact added.'
    
    if phone:
        record.add_phone(phone)
    
    return message

@input_error
def change_contact(args, book: AddressBook):
    name, old_phone, new_phone, *_ = args
    record = book.find(name)

    if not record:
        return f'Contact {name} not found'
    
    record.edit_phone(old_phone, new_phone)

    return f'Phone for contact {name} has changed'

@input_error
def show_contact(args, book: AddressBook):
    name, *_ = args
    record = book.find(name)

    if not record:
        return f'Contact {name} not found'
    
    phones = "; ".join(p.value for p in record.phones)
    return f'Contact {name} has phone number {phones}\n'

@input_error
def all_contacts(book: AddressBook):
    return "\n".join(str(record) for record in book.data.values())