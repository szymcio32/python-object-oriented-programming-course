class Animal:
    WHO_AM_I = 'I am a animal!'

    def __init__(self, name, color):
        self.name = name
        self.color = color

    def say_name(self):
        print(f'My name is {self.name}')


cat = Animal('Jasper', 'white')

dog = Animal('Max', 'black')


# cat.say_name()
# dog.say_name()
print(f'cat: {cat.WHO_AM_I}')
print(f'dog: {dog.WHO_AM_I}')
print(f'animal: {Animal.WHO_AM_I}')
# print(Animal.name)
print(vars(cat))
print(dir(dog))