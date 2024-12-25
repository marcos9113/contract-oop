# contact.py - Contains the Contact class to store individual contact details.

class Contact:
    def __init__(self, name, phone, email):
        """
        Initialize a new contact with a name, phone, and email.
        """
        self.name = name
        self.phone = phone
        self.email = email
    
    def update_contact(self, phone=None, email=None):
        """
        Update the phone and/or email of the contact.
        """
        if phone:
            self.phone = phone
        if email:
            self.email = email

    def __str__(self):
        """
        Return a string representation of the contact.
        """
        return f"{self.name} - {self.phone} - {self.email}"
