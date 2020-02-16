class Duck:

    def quack(self):
        print('I am a Duck!')

    def fly(self):
        print('Duck can fly')


class Human:

    def quack(self):
        print('I am a Human!')

    def fly(self):
        print("Human can't fly")


duck = Duck()
human = Human()

# for obj in [duck, human]:
#     if hasattr(obj, 'quack'):
#         obj.quack()
#     if hasattr(obj, 'fly'):
#         obj.fly()

for obj in [duck, human]:
    try:
        obj.quack()
        obj.fly()
        obj.eat()
    except AttributeError as exc:
        print(f'Attribute error: {exc}')
