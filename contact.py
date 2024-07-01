class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email, address):
        contact = {
            'name': name,
            'phone': phone,
            'email': email,
            'address': address
        }
        self.contacts.append(contact)
        print(f"Contact {name} added successfully!")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
            return
        for idx, contact in enumerate(self.contacts, start=1):
            print(f"{idx}. {contact['name']} - {contact['phone']}")

    def search_contact(self, search_term):
        results = [contact for contact in self.contacts if search_term.lower() in contact['name'].lower() or search_term in contact['phone']]
        if not results:
            print(f"No contacts found matching '{search_term}'.")
            return
        for contact in results:
            self.display_contact(contact)

    def update_contact(self, search_term):
        for contact in self.contacts:
            if search_term.lower() == contact['name'].lower() or search_term == contact['phone']:
                print("Contact found:")
                self.display_contact(contact)
                print("Enter new details (leave blank to keep current value):")
                name = input(f"Name ({contact['name']}): ") or contact['name']
                phone = input(f"Phone ({contact['phone']}): ") or contact['phone']
                email = input(f"Email ({contact['email']}): ") or contact['email']
                address = input(f"Address ({contact['address']}): ") or contact['address']
                contact.update({'name': name, 'phone': phone, 'email': email, 'address': address})
                print("Contact updated successfully!")
                return
        print(f"No contact found matching '{search_term}'.")

    def delete_contact(self, search_term):
        for contact in self.contacts:
            if search_term.lower() == contact['name'].lower() or search_term == contact['phone']:
                self.contacts.remove(contact)
                print(f"Contact {contact['name']} deleted successfully!")
                return
        print(f"No contact found matching '{search_term}'.")

    def display_contact(self, contact):
        print(f"Name: {contact['name']}")
        print(f"Phone: {contact['phone']}")
        print(f"Email: {contact['email']}")
        print(f"Address: {contact['address']}")

def main():
    contact_book = ContactBook()
    
    while True:
        print("\nContact Book Application")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Enter your choice (1/2/3/4/5/6): ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact_book.add_contact(name, phone, email, address)
        elif choice == '2':
            contact_book.view_contacts()
        elif choice == '3':
            search_term = input("Enter name or phone number to search: ")
            contact_book.search_contact(search_term)
        elif choice == '4':
            search_term = input("Enter name or phone number to update: ")
            contact_book.update_contact(search_term)
        elif choice == '5':
            search_term = input("Enter name or phone number to delete: ")
            contact_book.delete_contact(search_term)
        elif choice == '6':
            print("Exiting the Contact Book application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
