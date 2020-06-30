class Employee:
    # Same as a Constructor in Java.
    # When creating the init method in Python, it receives the first Instance as an argument automatically (self).
    # All the variables in this class are considered INSTANCE VARIABLES

    def __init__(self, first, last, pay):
        # self.first, self.last, self.pay, self.pay, self.email, are all attributes of a class.

        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


# Instantiating a class
emp_1 = Employee('Corey', 'Schafer', 5000)
emp_2 = Employee('Test', 'User', 60000)

print(emp_1.email)
print(emp_2.email)

# We could keep calling first and last name like this.
print('{} {}'.format(emp_1.first, emp_1.last))

# The 'self' keyword is needed in order to get the results of the 'emp_1' Instance.  TOP is same as BOTTOM
print(emp_1.fullname())

# The 'self' keyword is  needed in order to get the results of the 'emp_1' Instance BOTTOM is same as TOP
print(Employee.fullname(emp_1))
