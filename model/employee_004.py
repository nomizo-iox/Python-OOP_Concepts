# Class Method v. Instance Method v. Regular Method

import datetime

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

    """
    Setting a method with @classmethod, allows me to create class methods
    """
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount


    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)


    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

my_date = datetime.date(2020,7,3)
print(Employee.is_workday(my_date))

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

first, last, pay = emp_str_1.split('-')
new_emp_1 = Employee(first, last, pay)
print(new_emp_1.email)
print(new_emp_1.pay)


new_emp_2 = Employee.from_string(emp_str_2)
print(new_emp_2.email)
print(new_emp_2.pay)


# Instantiating a class
emp_1 = Employee('Corey', 'Schafer', 5000)
emp_2 = Employee('Test', 'User', 60000)



# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)

# print(emp_2.raise_amount)
print(emp_2.pay)
emp_2.another_raise()
print(emp_2.pay)

# Employee.raise_amount = 1.5

"""
cls.raise_amount = amount is same as Employee.raise_amount = 1.07
"""
Employee.set_raise_amt(1.07)

# print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

# print(emp_1.__dict__)
# print(Employee.__dict__)

# It knows this because the class was instantiated twice
print(Employee.num_of_emps)