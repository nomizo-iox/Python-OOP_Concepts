class Employee:
    
    raise_amt = 1.04
    num_of_emps = 0
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    @property
    def fullname(self):
        return '{} {}@email'.format(self.first, self.last)

    @property
    def email(self):
        return '{}.{}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


        # Getters & Setters

# Instantiating a class
emp_1 = Employee('Corey', 'Schafer', 5000)
emp_2 = Employee('Test', 'User', 60000)

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

emp_1.first = 'Jim'
print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

print(emp_1.fullname)