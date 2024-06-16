import json

# Define the contact book
contact_book = {}

# Function to add a contact
def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contact_book[name] = {
        'phone': phone,
        'email': email,
        'address': address
    }
    print("Contact added successfully!")

# Function to view all contacts
def view_contacts():
    if contact_book:
        for name, details in contact_book.items():
            print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}, Address: {details['address']}")
    else:
        print("No contacts found.")

# Function to search for a contact
def search_contact():
    search_term = input("Enter name or phone number to search: ")
    for name, details in contact_book.items():
        if search_term in name or search_term in details['phone']:
            print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}, Address: {details['address']}")
            return
    print("Contact not found.")

# Function to update a contact
def update_contact():
    name = input("Enter the name of the contact to update: ")
    if name in contact_book:
        phone = input("Enter new phone number: ")
        email = input("Enter new email: ")
        address = input("Enter new address: ")
        contact_book[name] = {
            'phone': phone,
            'email': email,
            'address': address
        }
        print("Contact updated successfully!")
    else:
        print("Contact not found.")

# Function to delete a contact
def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    if name in contact_book:
        del contact_book[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")

# Function to save the contact book to a file
def save_contacts():
    with open('contact_book.json', 'w') as file:
        json.dump(contact_book, file)
    print("Contacts saved to file.")

# Function to load the contact book from a file
def load_contacts():
    global contact_book
    try:
        with open('contact_book.json', 'r') as file:
            contact_book = json.load(file)
        print("Contacts loaded from file.")
    except FileNotFoundError:
        print("No saved contacts found.")

# User interface
def user_interface():
    load_contacts()
    while True:
        print("\nContact Book Menu")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Save and Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            save_contacts()
            break
        else:
            print("Invalid choice. Please try again.")

# Run the user interface
if __name__ == "__main__":
    user_interface()