contacts = []

def display_name ():
    print("\n -- Contact Book --")
    print("1. Add Contact")
    print("2. View all Contacts")
    print("3. Search Contact")
    print("4. Exit")

names_set = set()

def add_contact():
    name = input("Please enter the Name:").strip().title()
    if name in names_set:
        print("Similar name already exist")
        return
    
    phone_number = input("Enter Phone number here:").strip()
    contact= {
        "name": name,
        "phone_number":phone_number
                }
    contacts.append(contact)
    names_set.add(name)
    print(f"{name} has been added successfully")

def view_contacts():
    if not contacts:
        print("No Contacts found")
        return
    print("\n --- All Contacts ---")
    for idx, contact in enumerate(contacts, start=1):
        print(f"{idx}. {contact['name']} - {contact['phone_number']}")

def search_contact():
    search_name = input("Enter a name to search :").strip().title()
    found = False
    for contact in contacts:
        if contact['name'] == search_name:
            print(f"Found : {contact['name']} - {contact['phone_number'] }")
            found = True
            break
    if not found:
        print(f"Contact with name {search_name} not found in list")


def exit_contact():
    print("Good bye and see you later")

while True:
    display_name()
    choice = input("Choose an option (1-4):")

    if choice == "1":
        add_contact()
    elif choice=="2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        exit_contact()
        break
    else:
        print("Invalid choice, Please try again")



