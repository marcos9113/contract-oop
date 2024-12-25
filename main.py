from bst import BST
from contact import Contact

# Function to execute a command on the BST
def execute_command(bst, command):
    parts = command.split()
    action = parts[0]

    if action == "INSERT":
        name, phone, email = parts[1], parts[2], parts[3]
        bst.insert(Contact(name, phone, email))
        print(f"Added contact: {name}")
    
    elif action == "SEARCH":
        name = parts[1]
        contact = bst.search(name)
        if contact:
            print(f"Found: {contact}")
        else:
            print("Contact not found.")
    
    elif action == "UPDATE":
        name, phone, email = parts[1], parts[2], parts[3]
        bst.update(name, phone, email)
    
    elif action == "DELETE":
        name = parts[1]
        bst.delete(name)
        print(f"Deleted contact: {name}")
    
    else:
        print(f"Invalid command: {command}")

# Function to process commands from a file
def process_input_file(filename):
    bst = BST()
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if line and not line.startswith("---"):  # Skip empty lines and section headers
                execute_command(bst, line)

# Menu for interactive usage
def interactive_menu():
    bst = BST()
    while True:
        print("\n--- Contact Management System ---")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Display All Contacts")
        print("6. Process Commands from File")
        print("7. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            name = input("Enter Name: ")
            phone = input("Enter Phone: ")
            email = input("Enter Email: ")
            if name:
                bst.insert(Contact(name, phone, email))
                print("\nContact Added Successfully!\n")
            else:
                print("\nName cannot be empty!\n")

        elif choice == "2":
            name = input("Enter Name to Search: ")
            contact = bst.search(name)
            if contact:
                print(f"\nFound: {contact}\n")
            else:
                print("\nContact not found.\n")
        
        elif choice == "3":
            name = input("Enter Name to Update: ")
            phone = input("Enter New Phone (Leave blank to keep current): ")
            email = input("Enter New Email (Leave blank to keep current): ")
            bst.update(name, phone if phone else None, email if email else None)
        
        elif choice == "4":
            name = input("Enter Name to Delete: ")
            bst.delete(name)
            print(f"\n{name} deleted successfully (if found).\n")
        
        elif choice == "5":
            bst.display()
        
        elif choice == "6":
            filename = input("Enter the filename to process commands from: ")
            process_input_file(filename)
        
        elif choice == "7":
            print("\nExiting... Goodbye!\n")
            break
        
        else:
            print("\nInvalid choice. Please try again.\n")

if __name__ == "__main__":
    # Ask user if they want to use the menu system or process a file
    choice = input("Do you want to (1) Use Interactive Menu or (2) Process Commands from a File? Enter 1 or 2: ")
    if choice == "1":
        interactive_menu()
    elif choice == "2":
        filename = input("Enter the filename to process commands from: ")
        process_input_file(filename)
    else:
        print("Invalid choice. Exiting...")
