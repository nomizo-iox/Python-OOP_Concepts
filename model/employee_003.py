class Employee:

    raise_amount = 1.04
    num_of_emps = 0
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        # This is a counter to keep count of the number of employees
        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * 1.04)

    def another_raise(self):
        self.pay = int(self.pay * self.raise_amount)


# Instantiating a class
emp_1 = Employee('Corey', 'Schafer', 5000)
emp_2 = Employee('Test', 'User', 60000)

# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)

print(emp_2.raise_amount)
print(emp_2.pay)
emp_2.another_raise()
print(emp_2.pay)

# Employee.raise_amount = 1.5

# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

# print(emp_1.__dict__)
# print(Employee.__dict__)

# It knows this because the class was instantiated twice
print(Employee.num_of_emps)

