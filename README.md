# Contact Management System

## Overview
The **Contact Management System** is an application designed to store, manage, and manipulate contact information. The system provides a set of functionalities for managing contacts using a **Binary Search Tree (BST)** to ensure efficient operations for inserting, searching, updating, and deleting contacts. Additionally, the application allows batch processing of commands through a file, making it useful for managing contacts automatically.

The program supports two modes of operation:

1. **Interactive Mode**: A menu-driven approach where users can interact with the system in real-time to perform actions such as adding, searching, and updating contacts.
2. **Batch Mode**: A way to process a predefined list of commands stored in a text file to execute the contact management operations in a sequence.

This project demonstrates the use of **Object-Oriented Programming (OOP)** principles such as classes, inheritance, and encapsulation, with an emphasis on implementing a **Binary Search Tree (BST)** for contact management.

## Features
The system is designed to handle basic operations for managing contacts efficiently. The features include:

### 1. **Insert Contact**
- Allows the user to add a new contact to the system with a name, phone number, and email address.
- Contacts are inserted in a sorted order, ensuring that they can be retrieved quickly via search operations.

### 2. **Search Contact**
- Allows the user to search for a contact by name.
- Uses the **Binary Search Tree (BST)** to quickly locate contacts, ensuring fast search operations even as the list of contacts grows.

### 3. **Update Contact**
- Allows the user to update the phone number and/or email address of an existing contact.
- Updates are done in-place, and the updated contact will remain in the BST while retaining the order.

### 4. **Delete Contact**
- Allows the user to delete a contact by name.
- If the contact has two children, the BST will handle the deletion by replacing the deleted contact with its in-order successor.

### 5. **Display Contacts**
- Displays all the contacts currently stored in the system in sorted order (lexicographical order).
- This operation uses an **in-order traversal** of the BST to display contacts in ascending order of their names.

### 6. **Batch Processing from File**
- Allows the user to provide a file containing a series of commands to perform the contact management operations automatically.
- This feature is particularly useful for importing or processing large sets of data quickly.

### 7. **Interactive Command Line Interface**
- A user-friendly menu-driven interface that allows users to interact with the system through a series of prompts.
- The menu provides the following options:
  - Add, search, update, and delete contacts.
  - Display all contacts in sorted order.
  - Process commands from a file.
  - Exit the program.

## Technologies Used
The system is built using Python and follows Object-Oriented Programming principles. The key technologies and concepts used are:

- **Python**: The core programming language for implementing the system.
- **Binary Search Tree (BST)**: A fundamental data structure used for efficient storage, searching, and deletion of contacts.
- **File I/O**: Allows processing commands from external text files for batch operations.

## How It Works

### Core Classes
The system is structured into several core classes to manage the contacts and implement the BST data structure. Below are the key components of the system:

1. **Contact Class**:
   - Represents an individual contact with attributes like name, phone number, and email.
   - Provides methods to update contact information.

2. **Node Class**:
   - Represents a node in the Binary Search Tree. Each node holds a contact and has pointers to its left and right child nodes.

3. **BST Class**:
   - Implements the Binary Search Tree, providing methods for inserting, searching, updating, deleting, and displaying contacts.
   - Each operation ensures that the BST property (left child < parent < right child) is maintained.

4. **Menu System (Main Program)**:
   - Provides an interactive command-line interface for users to interact with the system.
   - Supports user input to select operations like inserting, searching, updating, and deleting contacts.
   - Supports file input for batch processing of commands.

### Insertion of Contacts
When a new contact is inserted, the program places the contact in the correct position in the BST based on the contact's name. The BST ensures that the contacts are always stored in lexicographical order (alphabetically sorted by name). The insertion process follows this algorithm:
- If the BST is empty, the new contact becomes the root.
- Otherwise, the new contact is inserted recursively into the left or right subtree based on its comparison to the current node.

### Searching for Contacts
To search for a contact, the system performs a binary search on the tree, comparing the target name with the current node's name. This allows for an efficient search process with a time complexity of **O(log n)** in a balanced BST.

### Updating Contacts
If a contact is found, the phone number and/or email can be updated. The updated contact remains in the same position in the BST, maintaining the order. If no contact is found, an appropriate message is displayed.

### Deleting Contacts
When a contact is deleted, the system maintains the BST properties by ensuring the correct reorganization of the tree. If the contact has:
- **No children**: It is simply removed.
- **One child**: The node is removed, and the single child takes its place.
- **Two children**: The node is removed, and the in-order successor (the smallest contact in the right subtree) replaces the deleted node.

### Batch Processing (File Input)
The system can read a file with commands (e.g., `examples.txt`) and process each line sequentially. The commands include operations like **INSERT**, **SEARCH**, **UPDATE**, and **DELETE**. Each command is executed in the order it appears in the file.

### Explanation of Files

- **main.py**: The main program that provides both an interactive menu for users to interact with the system and a way to process commands from a file.
- **bst.py**: Defines the **Binary Search Tree** (BST) class that handles insertion, searching, updating, deletion, and traversal of contacts.
- **contact.py**: Contains the **Contact** class that represents an individual contact with attributes like name, phone number, and email.
- **examples.txt**: A sample text file that contains a series of commands (e.g., `INSERT`, `SEARCH`, `UPDATE`, `DELETE`) for batch processing. This file is used to automatically perform contact management operations.
- **README.md**: The documentation file (this file), which provides details about the project and how to use it.

## How to Run the Program

### Step 1: Clone the Repository
Clone the repository to your local machine:
```bash
git clone https://github.com/yourusername/contact-management-system.git
cd contact-management-system
python main.py
.
.
.
.
.
Credit: ChatGPT
