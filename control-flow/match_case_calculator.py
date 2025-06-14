my_car = Car("Toyota", "Camry", 2020)
print(my_car.get_descriptive_name())  # Output: 2020 Toyota Camry

my_car.read_odometer()  # Output: This car has 0 miles on it.
my_car.update_odometer(100)  # Update odometer reading
my_car.read_odometer()  # Output: This car has 100 miles on it.

my_car.increment_odometer(50)  # Increment odometer reading
my_car.read_odometer()  # Output: This car has 150 miles on it.