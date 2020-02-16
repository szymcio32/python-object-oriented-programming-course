class Dancer:
    def dance(self):
        print('I am a Dancer!')


class FitnessCoach:
    def coach(self):
        print(f'I am a Fitness Coach!')


class Student(Dancer, FitnessCoach):
    pass


student = Student()
student.dance()
student.coach()

print(Student.mro())
