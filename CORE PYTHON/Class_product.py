class Product:

    discount = 10

    def __init__(self, product_name, price):
        self.product_name = product_name
        self.price = price

    # Instance method
    def final_price(self):
        discount_amount = self.price * Product.discount / 100
        return self.price - discount_amount

    # Class method
    @classmethod
    def change_discount(cls, new_discount):
        cls.discount = new_discount

    # Static method
    @staticmethod
    def validate_price(price):
        return price > 0

p1 = Product("Laptop", 50000)

print("Product:", p1.product_name)
print("Original Price:", p1.price)
print("Final Price:", p1.final_price())

print("Valid Price:", Product.validate_price(50000))

Product.change_discount(20)

print("New Discount:", Product.discount)
print("New Final Price:", p1.final_price())