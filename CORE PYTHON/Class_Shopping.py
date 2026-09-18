class ShoppingCart:
    tax_percentage = 18
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.total_amount = 0
    # Instance method
    def add_product(self, price):
        if ShoppingCart.validate_price(price):
            self.total_amount += price
            print("Product added:", price)
        else:
            print("Invalid product price")
    # Class method
    @classmethod
    def change_tax(cls, new_tax):
        cls.tax_percentage = new_tax
    # Static method
    @staticmethod
    def validate_price(price):
        return price > 0
    # Instance method
    def display(self):
        print("Customer:", self.customer_name)
        print("Total Amount:", self.total_amount)
        print("Tax:", ShoppingCart.tax_percentage, "%")

cart = ShoppingCart("Shrishail")
cart.add_product(500)
cart.add_product(1000)
cart.add_product(200)
cart.display()
ShoppingCart.change_tax(20)
print("\nAfter changing tax:")
cart.display()