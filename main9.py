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
                print(add_contact(name, phone))
            except:
                print("Enter name and phone")

        elif command.startswith("change"):
            try:
                name, phone = command.split()[1:]
                print(change_phone(name, phone))
            except:
                print("Enter name and phone")

        elif command.startswith("phone"):
            try:
                name = command.split()[1]
                print(show_phone(name))
            except:
                print("Enter name")

        elif command == "show all":
            print(show_all())

        elif command in ["good bye", "close", "exit"]:
            print("Good bye!")
            break

        else:
            print("Unknown command")


main()
