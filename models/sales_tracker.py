# models/sales_tracker.py
# Manages all sales transactions in the store.

from models.sale import Sale

class SalesTracker:
    """
    Manages sales records.
    - Uses encapsulation to store and manage sales history.
    - Ensures proper validation before recording sales.
    """
    
    def __init__(self):
        self.sales_history = []  # List to store all sale transactions
    
    def record_sale(self, product, quantity, cashier_name):
        """
        Records a new sale transaction.
        :param product: Product object being sold.
        :param quantity: Quantity of the product being sold.
        :param cashier_name: Name of the cashier processing the sale.
        """
        if product.stock < quantity:
            print("\n❌ Not enough stock to complete this sale.")
            return None
        
        total_price = product.price * quantity
        product.stock -= quantity  # Deduct from inventory
        
        try:
            sale = Sale(product.name, quantity, total_price, cashier_name)
            self.sales_history.append(sale)
            print(f"\n✅ Sale recorded: {quantity}x {product.name} for ${total_price:.2f}")
            return sale
        except ValueError as e:
            print(f"\n❌ Sale could not be recorded: {e}")
            return None
    
    def view_sales_history(self, cashier_name=None):
        """
        Displays sales history.
        :param cashier_name: If provided, filters sales by the given cashier.
        """
        if not self.sales_history:
            print("\n📜 No sales recorded yet.")
            return
        
        print("\n===== SALES HISTORY =====")
        for sale in self.sales_history:
            if cashier_name is None or sale.cashier_name == cashier_name:
                print(sale)
    
    def get_total_revenue(self):
        """
        Returns the total revenue from all sales.
        """
        return sum(sale.total_price for sale in self.sales_history)
