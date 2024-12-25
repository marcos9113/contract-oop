# bst.py - Contains the BST (Binary Search Tree) implementation and contact management logic.

from contact import Contact

class Node:
    def __init__(self, contact):
        """
        Node in the BST to hold a Contact object and its left and right children.
        """
        self.contact = contact
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        """
        Initialize the BST with an empty root.
        """
        self.root = None

    def insert(self, contact):
        """
        Insert a contact into the BST.
        If the root is None, make the contact the root. 
        Otherwise, recursively insert into the correct position based on name.
        """
        if not self.root:
            self.root = Node(contact)
        else:
            self._insert(self.root, contact)

    def _insert(self, current, contact):
        """
        Helper method to recursively insert a contact into the BST.
        """
        if contact.name < current.contact.name:
            if current.left:
                self._insert(current.left, contact)
            else:
                current.left = Node(contact)
        else:
            if current.right:
                self._insert(current.right, contact)
            else:
                current.right = Node(contact)

    def search(self, name):
        """
        Search for a contact by name in the BST.
        """
        return self._search(self.root, name)

    def _search(self, current, name):
        """
        Helper method to recursively search for a contact by name.
        """
        if not current:
            return None
        if name == current.contact.name:
            return current.contact
        elif name < current.contact.name:
            return self._search(current.left, name)
        else:
            return self._search(current.right, name)

    def update(self, name, phone=None, email=None):
        """
        Update an existing contact's phone and/or email.
        """
        contact = self.search(name)
        if contact:
            contact.update_contact(phone, email)
            print(f"\nUpdated: {contact}\n")
        else:
            print("Contact not found.")

    def delete(self, name):
        """
        Delete a contact from the BST by name.
        """
        self.root = self._delete(self.root, name)

    def _delete(self, current, name):
        """
        Helper method to recursively delete a contact.
        """
        if not current:
            return current
        if name < current.contact.name:
            current.left = self._delete(current.left, name)
        elif name > current.contact.name:
            current.right = self._delete(current.right, name)
        else:
            if not current.left:
                return current.right
            elif not current.right:
                return current.left
            temp = self._min_value_node(current.right)
            current.contact = temp.contact
            current.right = self._delete(current.right, temp.contact.name)
        return current

    def _min_value_node(self, node):
        """
        Find the node with the smallest value (used for deletion).
        """
        current = node
        while current.left:
            current = current.left
        return current

    def display(self):
        """
        Display all contacts in alphabetical order.
        """
        print("\n--- Contact List ---")
        self._display(self.root)
        print("\n")

    def _display(self, current):
        """
        Helper method to recursively display contacts.
        """
        if current:
            self._display(current.left)
            print(current.contact)
            self._display(current.right)
