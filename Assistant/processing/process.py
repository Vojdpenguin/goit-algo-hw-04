def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_phone(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
    return "Contact changed"

def show_num(args, contacts):
    name, = args
    if name in contacts:
        return f"Contact: {name} {contacts[name]}"
    else:
        return f"Contact not found"

