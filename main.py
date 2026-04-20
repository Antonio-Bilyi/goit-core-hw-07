from input_parser import parse_input
from addressbook import AddressBook
from contact_command_handler import add_contacts, change_contact, show_contact, all_contacts
from birthday_command_handler import add_birthday, show_birthday, birthdays

def main():

    book = AddressBook()
    print('Welcome to the assistant bot!')

    while True:
        
        user_input = input('Enter a command: ')
        command, *args = parse_input(user_input)

        if command in ['close', 'exit']:
            print('Good bye!')
            break

        elif command == 'hello':
            print('How can i help you ?')
        
        elif command == 'add':
            print(add_contacts(args, book))

        elif command == 'change':
            print(change_contact(args, book))

        elif command == 'phone':
            print(show_contact(args, book))

        elif command == 'all':
            print(all_contacts(book))

        elif command == 'add-birthday':
            print(add_birthday(args, book))

        elif command == 'show-birthday':
            print(show_birthday(args, book))

        elif command == 'birthdays':
            print(birthdays(book))

        else:
            print('Invalid command')

if __name__ == '__main__':
    main()