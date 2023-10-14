def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args


def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."


def change_contact(args, contacts):
    name, phone = args
    if name not in contacts:
        return "Contact does not exist."
    else:
        contacts[name] = phone
        return "Contact updated."


def get_phone(args, contacts):
    name = args[0]
    if name not in contacts:
        return "Contact does not exist."
    else:
        return contacts[name]


def get_all_contacts(contacts):
    print("List of contacts:")
    for name, phone in contacts.items():
        print(f"{name}: {phone}")


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        if command in ["close", "exit"]:
            print("Goodbye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            if len(args) != 2:
                print("Incorrect number of arguments.")
            else:
                print(add_contact(args, contacts))
        elif command == "change":
            if len(args) != 2:
                print("Incorrect number of arguments.")
            else:
                print(change_contact(args, contacts))
        elif command == "phone":
            if len(args) != 1:
                print("Incorrect number of arguments.")
            else:
                print(get_phone(args, contacts))
        elif command == "all":
            print(get_all_contacts(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()