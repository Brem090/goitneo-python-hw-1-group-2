def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args


def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."


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
                name, phone = args
                if name not in contacts:
                    print("Contact does not exist.")
                else:
                    contacts[name] = phone
                    print("Contact updated.")
        elif command == "phone":
            if len(args) != 1:
                print("Incorrect number of arguments.")
            else:
                name = args[0]
                if name not in contacts:
                    print("Contact does not exist.")
                else:
                    print(contacts[name])
        elif command == "all":
            print("List of contacts:")
            for name, phone in contacts.items():
                print(f"{name}: {phone}")
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()