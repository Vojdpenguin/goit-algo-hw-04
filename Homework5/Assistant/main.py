from Comparser import parse_input
from processing import add_contact, change_phone, show_num
from json import dumps


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "all":
            print(f"Your all contacts: \n{dumps(contacts, indent=1)}")
        elif command == "change":
            print(change_phone(args, contacts))
        elif command == "show":
            print(show_num(args,contacts))

if __name__ == "__main__":
    main()

