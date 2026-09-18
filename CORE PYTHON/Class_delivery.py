class Restaurant:
    platform_name = "FoodExpress"

    def __init__(self, restaurant_name, location, rating):
        self.restaurant_name = restaurant_name
        self.location = location
        self.rating = rating

    # Instance method
    def display(self):
        print("Restaurant:", self.restaurant_name)
        print("Location:", self.location)
        print("Rating:", self.rating)
        print("Platform:", Restaurant.platform_name)

    # Class method
    @classmethod
    def change_platform(cls, new_platform):
        cls.platform_name = new_platform

    # Static method
    @staticmethod
    def calculate_delivery_charge(distance):
        if distance <= 5:
            return 30
        else:
            return 30 + (distance - 5) * 10

r1 = Restaurant("Udupi Restaurant", "Hubli", 4.5)
r1.display()
print("Delivery Charge:",
      Restaurant.calculate_delivery_charge(8))

Restaurant.change_platform("QuickFood")

print("\nAfter changing platform:")

r1.display()