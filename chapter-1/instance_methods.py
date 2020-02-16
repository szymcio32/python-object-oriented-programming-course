class Animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def who_am_i(self):
        print('I am a animal!')

    def say_name(self):
        print(f'My name is {self.name}')


cat = Animal('Jasper', 'white')

dog = Animal('Max', 'black')


# cat.who_am_i()
# dog.who_am_i()
cat.say_name()
cat.say_name()

