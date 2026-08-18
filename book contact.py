contacts = []

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }

    contacts.append(contact)
    print("Contact added successfully!")


def view_contacts():
    if len(contacts) == 0:
        print("No contacts found.")
    else:
        print("\n--- Contact List ---")
        for i, contact in enumerate(contacts, start=1):
            print(f"{i}. Name: {contact['name']}")
            print(f"   Phone: {contact['phone']}")
            print(f"   Email: {contact['email']}")


def search_contact():
    name = input("Enter name to search: ").lower()

    found = False
    for contact in contacts:
        if contact["name"].lower() == name:
            print("\nContact Found:")
            print("Name:", contact["name"])
            print("Phone:", contact["phone"])
            print("Email:", contact["email"])
            found = True

    if not found:
        print("Contact not found.")


def delete_contact():
    name = input("Enter name to delete: ").lower()

    for contact in contacts:
        if contact["name"].lower() == name:
            contacts.remove(contact)
            print("Contact deleted successfully!")
            return

    print("Contact not found.")


while True:
    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        print("Thank you for using Contact Book!")
        break
    else:
        print("Invalid choice! Please try again.")