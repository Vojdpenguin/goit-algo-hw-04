from .decorator import input_error

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_phone(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
    return "Contact changed"

@input_error
def show_num(args, contacts):
    name, = args
    if name in contacts:
        return f"Contact: {name} {contacts[name]}"

