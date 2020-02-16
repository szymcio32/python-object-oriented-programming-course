class Teacher:
    def __init__(self, first_name, last_name, students):
        self.first_name = first_name
        self.last_name = last_name
        self.number_of_students = students

    def show_information(self):
        print(f'Full name: {self.first_name} {self.last_name}\n'
              f'Number of students: {self.number_of_students}')


class Mathematics(Teacher):
    FAVORITE_NUMBER = 10


teacher = Teacher('John', 'Gomez', 30)
print(f'First name: {teacher.first_name}')
teacher.show_information()

print('------------------------')

mathematics = Mathematics('Tom', 'Smith', 35)
print(f'First name: {mathematics.first_name}')
mathematics.show_information()
print(f'Favorite number: {mathematics.FAVORITE_NUMBER}')
