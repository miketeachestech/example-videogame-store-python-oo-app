# models/sale.py
# Defines the Sale class, which represents a sales transaction.

from datetime import datetime

class Sale:
    """
    Represents a sales transaction in the store.
    - Stores details of each sale including product, quantity, and total price.
    - Uses encapsulation to protect transaction data.
    """
    
    def __init__(self, product_name, quantity, total_price, cashier_name):
        self.product_name = product_name  # Name of the product sold
        self.quantity = self.validate_quantity(quantity)  # Ensures quantity is positive
        self.total_price = self.validate_price(total_price)  # Ensures total price is valid
        self.cashier_name = cashier_name  # Cashier handling the sale
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Timestamp of sale
    
    @staticmethod # because it does not depend on instance attributes.
    def validate_quantity(quantity):
        """
        Ensures the quantity sold is a positive integer.
        """
        if quantity <= 0:
            raise ValueError("❌ Quantity must be greater than zero.")
        return quantity
    
    @staticmethod # because it performs validation without accessing instance attributes.
    def validate_price(price):
        """
        Ensures the total price is a positive value.
        """
        if price <= 0:
            raise ValueError("❌ Total price must be greater than zero.")
        return price
    
    def __str__(self):
        """
        Returns a formatted string representation of the sale.
        """
        return f"{self.timestamp} | {self.cashier_name} sold {self.quantity}x {self.product_name} | Total: ${self.total_price:.2f}"