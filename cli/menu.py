# cli/menu.py
# This module handles the main menu and user interactions.

import sys
from models.user_database import UserDatabase
from models.inventory import Inventory
from models.sales_tracker import SalesTracker
from models.user import Cashier, Manager
from utils.helpers import validate_positive_number, validate_non_negative_number

# Global instances (Encapsulation: Objects store their own state)
user_db = UserDatabase()
inventory = Inventory()
sales_tracker = SalesTracker()

def show_main_menu():
    """
    Displays the main menu and processes user input.
    """
    while True:
        print("\n===== VIDEO GAME STORE CASHIER SYSTEM =====")
        print("1. Log in as a Cashier")
        print("2. Log in as a Manager")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ").strip()
        
        if choice == "1":
            user = login("cashier")
        elif choice == "2":
            user = login("manager")
        elif choice == "3":
            print("\nExiting the program. Goodbye!")
            sys.exit()
        else:
            print("\nInvalid choice. Please enter a number between 1 and 3.")
            continue
        
        """ Direct user to the correct menu """
        if isinstance(user, Cashier):
            show_cashier_menu(user)
        elif isinstance(user, Manager):
            show_manager_menu(user)

def login(user_role):
    """
    Handles user authentication and ensures correct role selection.
    """
    print(f"\n=== {user_role.capitalize()} Login ===")
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()
    
    user = user_db.authenticate(username, password)
    
    if user:
        if user.get_role().lower() != user_role:
            print("❌ Incorrect role selection. Please log in as the correct user type.")
            return None
        print("\n✅ Login successful!")
        return user
    return None

def show_cashier_menu(user):
    """
    Displays the cashier menu.
    """
    while True:
        print(f"\n===== CASHIER MENU ({user.username}) =====")
        print("1. Record a Sale")
        print("2. Update Inventory")
        print("3. View Stock")
        print("4. Search for a Product")
        print("5. View My Sales History")
        print("6. Log Out")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            record_sale(user)
        elif choice == "2":
            update_inventory()
        elif choice == "3":
            inventory.view_inventory()
        elif choice == "4":
            search_product()
        elif choice == "5":
            sales_tracker.view_sales_history(user.username)
        elif choice == "6":
            print("\nLogging out...")
            return
        else:
            print("\nInvalid choice.")

def show_manager_menu(user):
    """
    Displays the manager menu with additional functionalities.
    """
    while True:
        print(f"\n===== MANAGER MENU ({user.username}) =====")
        print("1. Record a Sale")
        print("2. Update Inventory")
        print("3. View Stock")
        print("4. Search for a Product")
        print("5. View All Sales History")
        print("6. View Total Revenue")
        print("7. Add New Cashier")
        print("8. Delete Cashier")
        print("9. View All Cashiers")
        print("10. Add a New Product")
        print("11. Delete a Product")
        print("12. Log Out")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            record_sale(user)
        elif choice == "2":
            update_inventory()
        elif choice == "3":
            inventory.view_inventory()
        elif choice == "4":
            search_product()
        elif choice == "5":
            sales_tracker.view_sales_history()
        elif choice == "6":
            print(f"\nTotal Revenue: ${sales_tracker.get_total_revenue():.2f}")
        elif choice == "7":
            add_cashier()
        elif choice == "8":
            delete_cashier()
        elif choice == "9":
            user_db.view_cashiers()
        elif choice == "10":
            add_product()
        elif choice == "11":
            delete_product()
        elif choice == "12":
            print("\nLogging out...")
            return
        else:
            print("\nInvalid choice.")

def record_sale(user):
    """
    Handles recording a sale, ensuring stock availability.
    """
    product_name = input("Enter product name: ")

    if product_name not in inventory.products:
        print("❌ Product not found in inventory.")
        return

    product = inventory.products[product_name]

    while True:
        try:
            quantity = int(input("Enter quantity to sell: "))
            quantity = validate_positive_number(quantity, "Quantity")
            break
        except ValueError as e:
            print(e)

    sales_tracker.record_sale(product, quantity, user.username)

def update_inventory():
    """
    Allows cashiers and managers to update stock levels.
    """
    name = input("Enter product name: ")
    if name not in inventory.products:
        print("❌ Product not found.")
        return

    while True:
        try:
            new_stock = int(input("Enter new stock level: "))
            new_stock = validate_non_negative_number(new_stock, "Stock")
            break
        except ValueError as e:
            print(e)

    inventory.update_stock(name, new_stock)

def search_product():
    """
    Allows searching for a product by name.
    """
    name = input("Enter product name to search: ")
    inventory.search_product(name)

def add_cashier():
    """
    Allows managers to add a new cashier.
    """
    username = input("Enter new cashier username: ").strip()
    password = input("Enter new cashier password: ").strip()

    user_db.add_cashier(username, password)

def delete_cashier():
    """
    Allows managers to delete a cashier.
    """
    username = input("Enter cashier username to delete: ").strip()
    user_db.delete_cashier(username)

def add_product():
    """
    Handles adding a new product to the inventory.
    """
    name = input("Enter product name: ")
    category = input("Enter category (Game/Console/Accessory): ")

    # Ensure valid price input
    while True:
        try:
            price = float(input("Enter price: "))
            price = validate_positive_number(price, "Price")
            break
        except ValueError as e:
            print(e)

    # Ensure valid stock input
    while True:
        try:
            stock = int(input("Enter initial stock: "))
            stock = validate_non_negative_number(stock, "Stock")
            break
        except ValueError as e:
            print(e)

    inventory.add_product(name, category, price, stock)

def delete_product():
    """
    Handles deleting a product from the inventory.
    """
    name = input("Enter product name to delete: ")
    inventory.delete_product(name)
