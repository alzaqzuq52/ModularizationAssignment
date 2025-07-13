"""Main program to use the Employee class."""

from my_classes import Employee

def main():
    # Create an employee instance
    emp1 = Employee("Hassan", 60000)
    emp1.display_info()

    print("\nGiving a $5,000 raise...\n")
    emp1.give_raise(5000)
    emp1.display_info()

if __name__ == "__main__":
    main()
