import functools

HELP = """
    Commands:
    - hello: Greeting.
    - add <name> <phone>:Add new contact.
    - phone <name>: Get contact.
    - change <name> <phone>: Change the phone number of a contact.
    - all: All contacts.
    - help: All commands.
    - close/exit: Close the assistant.
    """

def input_error(func):
    def inner(*args, **kwargs):
        func_name = func.__name__
        try:
            return func(*args, **kwargs)
        except ValueError:
            match func_name:
                    case "add_contact":
                        return "Enter the argument for the command"
                    case "change_contact":
                        return "Enter the argument for the command"
                    case "get_phone":
                        return "Enter the argument for the command"
                    case _:
                        return "Invalid input."
            return "Give me name and phone please."
        except IndexError:
                return f"IndexError in '{func_name}'"
        except KeyError:
            return f"KeyError in '{func_name}' Contact {args[0]} not found."

    return inner

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def hello():
    return "How can I help you?"

@input_error
def close():
    return "Good bye!"

@input_error
def help():
    return HELP

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    return f"Contact {name} not found."

@input_error
def get_phone(args, contacts):
    name, *args = args
    phone = contacts.get(name)
    if phone:
        return phone
    return f"Contact {name} not found."

@input_error
def get_all_contacts(contacts):
    if len(contacts) == 0:
        return "No contacts found."
    res = ""
    for k, v in contacts.items():
        res+=f"{k}: {v}\n"

    return res

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        match command:
            case "close" | "exit":
                print(close())
                break
            case "hello":
                print(hello())
            case "add":
                print(add_contact(args, contacts))
            case "change":
                print(change_contact(args, contacts))
            case "phone":
                print(get_phone(args, contacts))
            case "all":
                print(get_all_contacts(contacts))
            case "help":
                print(help())

if __name__ == "__main__":
    main()