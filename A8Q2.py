phonebook = {}


def add(phonebook):
    while True:
        name = input("What is the name of the person you would like to add to the phone book? If done, enter Done.: ")
        if name == "Done":
            break
        number = input("What is the phone number of the person you would like to add to the phone book?: ")
        phonebook[name] = number
        return phonebook


def remove(phonebook):
    name = input("What is the name of the person you would like to remove from the phone book?: ")
    del phonebook[name]
    print(phonebook)


def view(phonebook):
    name = input("Which contact are you trying to view?: ")
    phonebook.get(name)


ask = input("To Add enter Add. To Remove enter Remove. To view enter View: ")
if ask == "Add":
    add(phonebook)
if ask == "Remove":
    remove(phonebook)
if ask == "View":
    view(phonebook)

