class Employee:
    
    raise_amt = 1.04
    num_of_emps = 0
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    # Special Methods or Dunder Methods

    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

# Instantiating a class
emp_1 = Employee('Corey', 'Schafer', 5000)
emp_2 = Employee('Test', 'User', 60000)

print(emp_1)
print(emp_1 + emp_2)


