"""
001 - Python Method Types: Instance, Class, and Static Methods
=============================================================

In Python classes, there are three main types of methods:
1. Regular instance methods
2. Class methods (using @classmethod decorator)
3. Static methods (using @staticmethod decorator)

Let's understand each one with simple examples.
"""

# First, let's create a simple class to demonstrate the differences
class Car:
    # Class variable - shared by all instances
    total_cars = 0
    
    def __init__(self, make, model, initial_speed=0):
        # Instance variables - unique to each instance
        self.make = make
        self.model = model
        self.speed = initial_speed
        # Increment the class variable
        Car.total_cars += 1
    
    # Regular instance method
    # - First parameter is 'self' (the instance)
    # - Can access/modify instance attributes (self.speed)
    def accelerate(self, amount):
        """Regular instance method that modifies instance state"""
        self.speed += amount
        return f"{self.make} {self.model} is now going {self.speed} mph"
    
    # Class method
    # - Decorated with @classmethod
    # - First parameter is 'cls' (the class itself)
    # - Can access/modify class attributes (cls.total_cars)
    @classmethod
    def get_total_cars(cls):
        """Class method that accesses class state"""
        return f"Total cars created: {cls.total_cars}"  
    
    # Another class method - often used as an alternative constructor
    @classmethod
    def create_sedan(cls, make):
        """Class method used as a factory to create specific car types"""
        return cls(make, "Sedan")
    
    # Static method
    # - Decorated with @staticmethod
    # - No automatic first parameter
    # - Cannot directly access class or instance attributes
    @staticmethod
    def is_valid_speed(speed):
        """Static method for utility function related to cars but not dependent on state"""
        return 0 <= speed <= 200

# Demonstration code
if __name__ == "__main__":
    print("=== DEMONSTRATION OF PYTHON METHOD TYPES ===\n")
    
    # 1. Regular instance methods
    print("=== Regular Instance Methods ===")
    my_car = Car("Toyota", "Corolla")
    print(f"Created a {my_car.make} {my_car.model}")
    print(my_car.accelerate(30))  # Using instance method
    print(my_car.accelerate(20))  # Using instance method again
    print(f"Current speed: {my_car.speed} mph")
    print()
    
    # 2. Class methods
    print("=== Class Methods ===")
    # Class methods can be called on the class itself
    print(Car.get_total_cars())  # Called on the class
    
    # Creating a car using the alternative constructor (class method)
    sedan = Car.create_sedan("Honda")
    print(f"Created a {sedan.make} {sedan.model}")
    print(Car.get_total_cars())  # Now we have 2 cars
    
    # Class methods can also be called on instances (but this is less common)
    print(my_car.get_total_cars())  # Same result as Car.get_total_cars()
    print()
    
    # 3. Static methods
    print("=== Static Methods ===")
    # Static methods can be called on the class
    print(f"Is 50 mph a valid speed? {Car.is_valid_speed(50)}")
    print(f"Is 250 mph a valid speed? {Car.is_valid_speed(250)}")
    
    # Static methods can also be called on instances
    print(f"Is 30 mph a valid speed? {my_car.is_valid_speed(30)}")
    print()
    
    # Key differences summary
    print("=== KEY DIFFERENCES ===")
    print("1. Regular methods: Need an instance, have access to instance data via 'self'")
    print("2. Class methods: Can be called on class or instance, have access to class data via 'cls'")
    print("3. Static methods: Can be called on class or instance, have no access to instance or class data")
