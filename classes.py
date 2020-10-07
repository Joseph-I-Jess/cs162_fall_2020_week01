"""Demonstrates the basics of classes in Python."""

"""
    ToDo:
        write more tests
        include file IO
        fix git repositories
"""


class Person:
    """Defines a Person."""

    def __init__(self):
        """Initialize a Person object."""

        self.name: str = "Joseph"
        self.age: int = 34
        self.is_alive: int = True

    def double_age(self):
        """Return double the value of this person's age.."""
        return self.age * 2

    def birthday(self):
        """Increase this peron's age by 1."""
        self.age += 1

    def birthdays(self, num_birthdays: int):
        """Increase this peron's age by num_birthdays."""
        self.age += num_birthdays

        return self.age

    def print_yo_self(self):
        """Print this person in a human readable format."""
        print(f"name: {self.name}, age: {self.age}, is_alive: {self.is_alive}")


joseph = Person()
# print(f"joseph.name: {joseph.name}")
# print(f"joseph.age: {joseph.age}")
# print(f"joseph.is_alive: {joseph.is_alive}")
joseph.print_yo_self()
print(joseph.double_age())

num_birthdays_output = joseph.birthdays(10)
print(f"num_birthdays_output: {num_birthdays_output}")
joseph.print_yo_self()
