class Teacher:
    def __init__(self, first_name, last_name, students):
        self.first_name = first_name
        self.last_name = last_name
        self.number_of_students = students

    def show_information(self):
        print(f'Full name: {self.first_name} {self.last_name}\n'
              f'Number of students: {self.number_of_students}')


class Mathematics(Teacher):
    def __init__(self, number, *args, **kwargs):
        self.favorite_number = number
        super().__init__(*args, **kwargs)

    def show_information(self):
        print(f'Full name: {self.first_name} {self.last_name}\n'
              f'Number of students: {self.number_of_students}\n'
              f'Favorite number: {self.favorite_number}')


teacher = Teacher('John', 'Gomez', 30)
teacher.show_information()

print('------------------------')

mathematics = Mathematics(first_name='Tom', last_name='Smith', students=35, number=10)
mathematics.show_information()
