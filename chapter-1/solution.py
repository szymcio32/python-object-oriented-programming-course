"""
Create an Employee class with following attributes and methods:

- constructor, which will create an instance of Employee class based on provided arguments:
    first name, last name, email address and monthly salary

- get_annual_salary method, which will calculate and return employee annual salary

- show_employee_information method, which will show employee information in such syntax:
    Employee: <full name>
    Email address: <email>
    Annual salary: <annual salary>

- an attribute, which will store the number of created objects of an Employee class
"""


class Employee:
    NUMBER_OF_EMPLOYEES = 0

    def __init__(self, first_name, last_name, email, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.monthly_salary = salary
        Employee.NUMBER_OF_EMPLOYEES += 1

    def get_annual_salary(self):
        return self.monthly_salary * 12

    def show_employee_information(self):
        full_name = f'{self.first_name} {self.last_name}'
        print(f'Employee: {full_name}\n'
              f'Email address: {self.email}\n'
              f'Annual salary: {self.get_annual_salary()}')


employee_1 = Employee('John', 'Smith', 'johnsmith@gmail.com', 3000)
employee_2 = Employee('Kate', 'Taylor', 'katetaylot@gmail.com', 3500)

employee_1.show_employee_information()
print('--------------------')
employee_2.show_employee_information()
print(f'Number of employees: {Employee.NUMBER_OF_EMPLOYEES}')
