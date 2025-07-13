"""This module contains class definitions for an employee management system."""

class Employee:
    """Represents an employee with name and salary."""

    def __init__(self, name, salary):
        """Initialize name and salary."""
        self.name = name
        self.salary = salary

    def give_raise(self, amount):
        """Adds a raise to the employee's salary."""
        self.salary += amount

    def display_info(self):
        """Displays the employee's information."""
        print(f"Name: {self.name}")
        print(f"Salary: ${self.salary}")
