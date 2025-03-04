# models/user.py
# Defines the User class and its subclasses (Cashier, Manager).

class User:
    """
    Base class representing a user in the system.
    - Implements inheritance for role-specific users.
    - Encapsulates common user attributes.
    """
    
    def __init__(self, username, role):
        self.username = username  # Stores the username
        self.role = role  # Stores user role (Cashier or Manager)
    
    def get_role(self):
        """
        Returns the role of the user.
        """
        return self.role
    
    def __str__(self):
        """
        Returns a formatted string representation of the user.
        """
        return f"{self.username} ({self.role})"

class Cashier(User):
    """
    Represents a Cashier, inheriting from the User class.
    - Specialization of User with role-specific attributes in the future.
    """
    
    def __init__(self, username):
        super().__init__(username, "Cashier")  # Calls the parent class constructor

class Manager(User):
    """
    Represents a Manager, inheriting from the User class.
    - Specialization of User with extended permissions.
    """
    
    def __init__(self, username):
        super().__init__(username, "Manager")  # Calls the parent class constructor
