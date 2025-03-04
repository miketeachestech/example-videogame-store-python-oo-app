# models/user_database.py
# Manages user accounts, allowing managers to add, delete, and view cashiers.

from models.user import Cashier, Manager

class UserDatabase:
    """
    Manages all users in the system.
    - Uses encapsulation to store user data securely.
    - Implements authentication and user management operations.
    """
    
    def __init__(self):
        # Dictionary to store users (username -> User object)
        self.users = {
            "manager1": Manager("manager1"),  # Predefined manager
            "cashier1": Cashier("cashier1")   # Predefined cashier
        }
        # Dictionary to store passwords (for simple authentication)
        self.passwords = {
            "manager1": "admin123",
            "cashier1": "pass123"
        }
    
    def add_cashier(self, username, password):
        """
        Adds a new cashier to the database.
        Ensures the username is unique.
        """
        if username in self.users:
            print("❌ User already exists.")
        else:
            self.users[username] = Cashier(username)
            self.passwords[username] = password
            print(f"✅ Cashier '{username}' added successfully!")
    
    def delete_cashier(self, username):
        """
        Deletes a cashier from the database.
        Ensures that managers cannot be deleted.
        """
        if username in self.users and isinstance(self.users[username], Cashier):
            del self.users[username]
            del self.passwords[username]
            print(f"✅ Cashier '{username}' removed successfully!")
        else:
            print("❌ Cashier not found or cannot delete a manager.")
    
    def view_cashiers(self):
        """
        Displays all registered cashiers.
        """
        print("\n===== REGISTERED CASHIERS =====")
        for username, user in self.users.items():
            if isinstance(user, Cashier):
                print(f"- {username}")
        print("================================")
    
    def authenticate(self, username, password):
        """
        Checks if a user exists and verifies the password.
        """
        if username in self.users and self.passwords.get(username) == password:
            return self.users[username]
        print("❌ Incorrect username or password.")
        return None