class Dog():
    """A simple attempt to code a dog"""
    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(self.name.title() + " is now sitting")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(self.name.title() + " is now rolling over")


# my_dog = Dog('willie', 6)


# print("My dogs name is {}. My dog is {} years old".format(my_dog.name.title(), my_dog.age))
# print(my_dog.roll_over())

# Try It Yourself page 166

class Restaurant():
    """makes a res"""
    def __init__(self, restaurant_name, cuisine_type):
        """adding name and food type"""
        self.name = restaurant_name
        self.type = cuisine_type

    def describe_restaurant(self):
        """state the name and the type of food served"""
        print("{} serves the best {} in the tri state area.".format(self.name.title(), self.type))

    def open_restaurant(self):
        """open message"""
        print("{} is open for the day".format(self.name.title()))

# my_res = Restaurant("Lucky house", 'Chinese')

# print(my_res.describe_restaurant())
# print(my_res.open_restaurant())

# stopped at Working with Classes and Instances on page 167


class Car():
    """A simple attempt to to rep a car"""

    def __init__(self, make, model, year):
        """int attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name_one(self):
        """"reteuns a formmated script of the car"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """Print the millage"""
        print("This car has {} miles on it.".format(self.odometer_reading))
        # print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self):
        """update the mialage"""


my_first = Car("Pontiac", 'Grand AM', 2001)


print(my_first.get_descriptive_name())
my_first.read_odometer()
