class MobilePhone:

    # Class variable
    warranty_period = 1

    # Constructor
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    # Instance method
    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Price:", self.price)
        print("Warranty:", MobilePhone.warranty_period, "year")

    # Class method
    @classmethod
    def change_warranty(cls, new_period):
        cls.warranty_period = new_period

    # Static method
    @staticmethod
    def validate_price(price):
        return price > 0

# Creating object
m1 = MobilePhone("Samsung", "Galaxy S25", 80000)
m1.display()
print("Valid Price:", MobilePhone.validate_price(80000))
MobilePhone.change_warranty(2)
print("\nAfter changing warranty period:")
m1.display()