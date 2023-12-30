class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone, email, address):
        self.contacts[name] = {'phone': phone, 'email': email, 'address': address}
        print(f"Contact {name} added successfully!")

    def view_contacts(self):
        if not self.contacts:
            print("Contact book is empty.")
        else:
            print("\n=== Contact List ===")
            for name, details in self.contacts.items():
                print(f"Name: {name}")
                print(f"Phone: {details['phone']}")
                print(f"Email: {details['email']}")
                print(f"Address: {details['address']}")
                print("----------------------")

    def search_contact(self, keyword):
        results = {}
        for name, details in self.contacts.items():
            if keyword.lower() in name.lower() or keyword in details['phone']:
                results[name] = details
        return results

    def update_contact(self, name, new_phone, new_email, new_address):
        if name in self.contacts:
            self.contacts[name]['phone'] = new_phone
            self.contacts[name]['email'] = new_email
            self.contacts[name]['address'] = new_address
            print(f"Contact {name} updated successfully!")
        else:
            print(f"Contact {name} not found.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact {name} deleted successfully!")
        else:
            print(f"Contact {name} not found.")


def main():
    contact_book = ContactBook()

    while True:
        print("\n=== Contact Book Menu ===")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            name = input("Enter the name: ")
            phone = input("Enter the phone number: ")
            email = input("Enter the email address: ")
            address = input("Enter the address: ")
            contact_book.add_contact(name, phone, email, address)

        elif choice == '2':
            contact_book.view_contacts()

        elif choice == '3':
            keyword = input("Enter name or phone number to search: ")
            results = contact_book.search_contact(keyword)
            if results:
                print("\n=== Search Results ===")
                for name, details in results.items():
                    print(f"Name: {name}")
                    print(f"Phone: {details['phone']}")
                    print(f"Email: {details['email']}")
                    print(f"Address: {details['address']}")
                    print("----------------------")
            else:
                print("No contacts found.")

        elif choice == '4':
            name = input("Enter the name of the contact to update: ")
            new_phone = input("Enter the new phone number: ")
            new_email = input("Enter the new email address: ")
            new_address = input("Enter the new address: ")
            contact_book.update_contact(name, new_phone, new_email, new_address)

        elif choice == '5':
            name = input("Enter the name of the contact to delete: ")
            contact_book.delete_contact(name)

        elif choice == '6':
            print("Exiting Contact Book. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()
