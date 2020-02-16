# import datetime
#
# today = datetime.datetime.now()
#
# print(today)
# print(str(today))
# print(repr(today))
# print('--------')
#
# new_date = datetime.datetime(2020, 1, 9, 22, 29, 6, 178299)
# print(new_date)
#

class Car:
    def __init__(self, color, model):
        self.color = color
        self.model = model

    def __str__(self):
        return f'This is a {self.color} {self.model}'

    # def __repr__(self):
    #     return f'{self.__class__.__name__}({self.color!r}, {self.model!r})'


bmw_1 = Car('white', 'BMW')
print(f'bmw_1: str() - {str(bmw_1)}')
print(f'bmw_1: repr() - {repr(bmw_1)}')
print('--------')

bmw_2 = Car('white', 'BMW')
print(f'bmw_2: str() - {bmw_2}')
print(f'bmw_2: repr() - {repr(bmw_2)}')