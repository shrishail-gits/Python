class Car:

    # Class variable
    country = "India"

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
        print("Country:", Car.country)

    # Class method
    @classmethod
    def change_country(cls, new_country):
        cls.country = new_country

    # Static method
    @staticmethod
    def validate_price(price):
        return price > 0

c1 = Car("Toyota", "Fortuner", 4000000)
c1.display()
print("Valid Price:", Car.validate_price(4000000))
Car.change_country("Japan")
print("\nAfter changing country:")
c1.display()