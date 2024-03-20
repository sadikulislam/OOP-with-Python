import re


class Employee:
    raise_amt = 1.04

    def __init__(self, first, last, id, salary):
        self.first = first
        self.last = last
        self.id = id
        self.salary = salary
        self.email = first + '.' + last + '@gmail.com'

    def fullname(self):
        return f'{self.first} {self.last}'

    def is_valid_email(self):
        pattern = r"^[a-zA-Z0-9.]+@gmail.com$"
        if re.match(pattern, self.email):
            print("Your email is correct")
        else:
            print("Your email is invalid")

    def apply_raise(self):
        return int(self.salary * self.raise_amt)

    def display_info(self):
        print(f"Name: {self.fullname()}\nID: {self.id}\nSalary: {self.apply_raise()}\nEmail: {self.email}")


emp1 = Employee('John', 'Smith', 100, 50000)
print(emp1.is_valid_email())
print(emp1.display_info())