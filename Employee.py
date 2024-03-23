import re


class Employee:
    raise_amt = 1.04

    def __init__(self, first, last, id, salary):
        self.first = first
        self.last = last
        self.id = id
        self.salary = salary

    @property
    def email(self):
        return f"{self.first}.{self.last}@email.com"

    @property
    def fullname(self):
        return f'{self.first} {self.last}'

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Delete the name')
        self.first = None
        self.last = None

    def is_valid_email(self):
        pattern = r"^[a-zA-Z0-9.]+@gmail.com$"
        if re.match(pattern, self.email):
            print("Your email is correct")
        else:
            print("Your email is invalid")

    def apply_raise(self):
        self.salary = int(self.salary * self.raise_amt)

    def display_info(self):
        print(f"Name: {self.fullname}\nID: {self.id}\nSalary: {self.apply_raise()}\nEmail: {self.email}")


class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, id, salary, prog_lang):
        super().__init__(first, last, id, salary)
        self.prog_lang = prog_lang


class Manager(Employee):
    def __init__(self, first, last, id, salary, employees=None):
        super().__init__(first, last, id, salary)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_employees(self):
        for emp in self.employees:
            print('-->', emp.fullname())


dev_1 = Developer('Jack', 'Nash', 100, 30000, 'Python')
dev_2 = Developer('John', 'Smith', 102, 50000, 'Java')

mgr_1 = Manager('Max', 'Joe', 303, 90000, [dev_1])

emp1 = Employee('Jack', 'Nash', 100, 30000)

dev_2.display_info()
dev_1.apply_raise()
