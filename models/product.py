# models/product.py
# Defines the Product class, which represents an item in the store.

class Product:
    """
    Represents a product in the video game store.
    - Encapsulates product attributes such as name, category, price, and stock.
    - Ensures data integrity by validating inputs.
    """
    
    def __init__(self, name, category, price, stock):
        self.name = name  # Name of the product (e.g., "PlayStation 5")
        self.category = category  # Category (Game, Console, Accessory)
        self.price = self.validate_price(price)  # Ensures price is positive
        self.stock = self.validate_stock(stock)  # Ensures stock is non-negative
    
    @staticmethod
    def validate_price(price):
        """
        Ensures the price is a positive value.
        """
        return max(price, 0.01)  # Prevents non-positive prices
    
    @staticmethod
    def validate_stock(stock):
        """
        Ensures the stock is a non-negative integer.
        """
        return max(stock, 0)  # Prevents negative stock values
    
    def update_stock(self, quantity):
        """
        Updates the stock level of the product.
        """
        if quantity < 0:
            print("❌ Stock cannot be negative.")
            return
        self.stock = quantity
        print(f"✅ Stock updated: {self}")
    
    def __str__(self):
        """
        Returns a formatted string representation of the product.
        """
        return f"{self.name} | {self.category} | ${self.price:.2f} | Stock: {self.stock}"
