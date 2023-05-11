contacts = {}

def input_error(func):
    def wrapper(*args):
        try:
            return func(*args)
        except KeyError:
            return "Contact not found"
        except ValueError:
            return "Enter name and phone"
        except IndexError:
            return "Enter name and phone"
    return wrapper

@input_error
def add_contact(name, phone):
    contacts[name] = phone
    return "Contact added"

@input_error
def change_phone(name, phone):
    contacts[name] = phone
    return "Phone number changed"

@input_error
def show_phone(name):
    return contacts[name]

def show_all():
    if contacts:
        return "\n".join("{}: {}".format(name, phone) for name, phone in contacts.items())
    else:
        return "No contacts found"

def main():
    print("Hello!)")

    while True:
        command = input().lower()

        if command == "hello":
            print("How can I help you?")

        elif command.startswith("add"):
            try:
                name, phone = command.split()[1:]
                result = add_contact(name, phone)
            except:
                result = "Enter name and phone"
            print(result)

        elif command.startswith("change"):
            try:
                name, phone = command.split()[1:]
                result = change_phone(name, phone)
            except:
                result = "Enter name and phone"
            print(result)

        elif command.startswith("phone"):
            try:
                name = command.split()[1]
                result = show_phone(name)
            except:
                result = "Enter name"
            print(result)

        elif command == "show all":
            result = show_all()
            print(result)

        elif command in ["good bye", "close", "exit"]:
            print("Good bye!")
            break

        else:
            print("Unknown command")


main()

