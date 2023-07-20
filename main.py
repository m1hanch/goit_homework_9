#функція для очищення номеру від не цифрових знаків
def sanitize_phone_number(phone):
    new_phone = (
        phone.strip()
            .removeprefix("+")
            .replace("(", "")
            .replace(")", "")
            .replace("-", "")
            .replace(" ", "")
    )
    return new_phone
def phone_validation(phone:str) -> bool:
    if sanitize_phone_number(phone).isdigit() and (len(phone) == 10 or len(phone) == 12):
        return True
    else:
        return False

#функія для обрробки помилок
def input_error(handler):
    def inner(command, phone_book):
        try:
            return handler(command, phone_book)
        except KeyError:
            return 'Contact with such name does not exist'
        except ValueError:
            return 'Please enter the name of desired contact'
        except IndexError:
            return 'Please enter valid name and phone'
    return inner

@input_error
def handler(command: str, phone_book: dict):
    command = command.lower().split()
    #умова для hello
    if command[0] == 'hello':
        return "How can I help you?"

    #умова для show all
    elif ' '.join(command)=='show all':
        return '\n'.join(name.capitalize()+' '+number for name, number in phone_book.items())

    #умова для виходу з програми
    elif command[0] in ('good bye', 'close', 'exit'):
        return 'Good bye!'

    # умова для add та change. Також перевірка правильного порядку введення
    elif command[0] in ('add', 'change') and command[1].isalpha() and phone_validation(command[2]):
        phone_book.update({command[1]: sanitize_phone_number(command[2])})
        # Визначення правильної ввідповіді
        if command[0] == 'add':
            return f'{command[1].capitalize()} added!'
        else:
            return f'{command[1].capitalize()} changed!'

    # виклик помилки в разі неправильного формату команди
    elif command[0] in ('add', 'change') and not (command[1].isalpha() and phone_validation(command[2])):
        raise IndexError
    elif command[0] == 'phone' and (len(command) == 1 or not command[1].isalpha()):
        raise ValueError
    elif command[0] == 'phone' and command[1].isalpha():
        return f'{command[1]}\'s phone number: {phone_book[command[1]]}'

    #В усіх інших випадках повертаємо 'Unknown command'
    else:
        return 'Unknown command'

def main():
    phone_book = {}
    while True:
        command = input('> ')
        result = handler(command, phone_book)
        if result == 'Good bye!':
            print(result)
            break
        print(result)

if __name__ == '__main__':
    main()
