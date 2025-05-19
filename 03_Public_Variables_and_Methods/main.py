class Car:
    def __init__(self, brand):
        self.brand = brand  # Public variable

    def start(self):  # Public method
        print(f"{self.brand} car is starting...")

# Example usage
my_car = Car("Toyota")
print("Car Brand:", my_car.brand)
my_car.start()
