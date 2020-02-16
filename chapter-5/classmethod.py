class Employee:
    EMPLOYEES_GRADES = {
        'A': '2500',
        'B': '3000',
        'C': '3500',
        'D': '4000'
    }

    def __init__(self, first_name, last_name, grade):
        self.first_name = first_name
        self.last_name = last_name

        if grade not in Employee.EMPLOYEES_GRADES:
            raise KeyError(f"Wrong employee grade. Available grades: {list(Employee.EMPLOYEES_GRADES)}")
        self.salary = Employee.EMPLOYEES_GRADES[grade]

    def show_employee_information(self):
        print('Employee information:')
        print(f"\tName: {self.first_name} {self.last_name}\n\tSalary: {self.salary}")

    @classmethod
    def show_grades(cls):
        print('Employees grades:')
        # Employee.EMPLOYEES_GRADES.items() == cls.EMPLOYEES_GRADES.items()
        for grade, salary in cls.EMPLOYEES_GRADES.items():
            print(f'\t {grade}: {salary}')

    @classmethod
    def add_grade(cls, grade, salary):
        # Employee.EMPLOYEES_GRADES[grade] == cls.EMPLOYEES_GRADES[grade]
        cls.EMPLOYEES_GRADES[grade] = salary


employee_1 = Employee('John', 'Smith', 'A')
# employee_1.show_employee_information()
# employee_1.show_grades()
# Employee.show_grades()
# Employee.show_employee_information()  -> TypeError

employee_1.add_grade('E', 4500)
Employee.add_grade('F', 5000)
Employee.show_grades()