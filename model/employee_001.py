class Employee:
    pass

# Instance variable contain data that is unique to each Instance

# This is how Instantiation of a class is being done in Python
emp_1 = Employee()
emp_2 = Employee()


print(emp_1)
print(emp_2)

emp_1.first = 'Corey'
emp_1.last = 'Schafer'
emp_1.email = 'Corey.Schafer@Company.com'
emp_1.pay = 50000

emp_2.first = 'Test'
emp_2.last = 'User'
emp_2.email = 'Test.User@Company.com'
emp_2.pay = 60000

print(emp_1.email)
print(emp_2.email)