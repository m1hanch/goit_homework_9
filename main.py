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

command = input('> ').lower()
phone_book = {}
if command=='hello':
    print("How can I help you?")
command = input('> ').lower()
command = command.split()
if (command[0] == 'add' or command[0]=='change') and command[1].isalpha() and sanitize_phone_number(command[2]).isdigit():
    phone_book.update({command[1]:sanitize_phone_number(command[2])})
elif command[0] == 'phone' and command[1].isalpha():
    if command[1][-1] == 's':
        print(f'{command[1]}\' phone number: {phone_book[command[1]]}')
    else:
        print(f'{command[1]}\'s phone number: {phone_book[command[1]]}')


