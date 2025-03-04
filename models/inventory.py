# models/inventory.py
# Manages all store products using object-oriented principles.

from models.product import Product

class Inventory:
    """
    Manages the store's inventory of products.
    - Uses encapsulation to store product data securely.
    - Follows single responsibility principle by handling only inventory-related tasks.
    """
    
    def __init__(self):
        self.products = {}  # Dictionary to store products (name -> Product object)

    def add_product(self, name, category, price, stock):
        """
        Adds a new product to the inventory.
        Ensures data validity before adding.
        """
        if name in self.products:
            print("❌ Product already exists in inventory.")
            return
        
        self.products[name] = Product(name, category, price, stock)
        print(f"✅ Product '{name}' added successfully!")

    def delete_product(self, name):
        """
        Deletes a product from the inventory if it exists.
        """
        if name in self.products:
            del self.products[name]
            print(f"✅ Product '{name}' removed from inventory.")
        else:
            print("❌ Product not found.")

    def update_stock(self, name, new_stock):
        """
        Updates the stock level of a product.
        Ensures stock cannot be negative.
        """
        if name in self.products:
            if new_stock < 0:
                print("❌ Stock cannot be negative.")
                return
            
            self.products[name].update_stock(new_stock)
            print(f"✅ Stock updated: {self.products[name]}")
        else:
            print("❌ Product not found.")

    def view_inventory(self):
        """
        Displays all products in the inventory.
        """
        if not self.products:
            print("📦 Inventory is empty.")
        else:
            print("\n===== INVENTORY =====")
            for product in self.products.values():
                print(product)

    def search_product(self, name):
        """
        Searches for a product by name.
        Returns details if found.
        """
        if name in self.products:
            print(self.products[name])
        else:
            print("❌ Product not found.")