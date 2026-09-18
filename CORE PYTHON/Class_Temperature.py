class Temperature:

    def __init__(self, celsius):
        self.celsius = celsius

    # Instance method
    def display(self):
        print("Temperature:", self.celsius, "°C")

    # Static method
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9 / 5) + 32

    # Static method
    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        return (fahrenheit - 32) * 5 / 9

# Creating object
t1 = Temperature(25)
t1.display()
print("Celsius to Fahrenheit:",
      Temperature.celsius_to_fahrenheit(25))
print("Fahrenheit to Celsius:",
      Temperature.fahrenheit_to_celsius(77))