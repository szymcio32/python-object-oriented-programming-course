from datetime import datetime


class CustomDate:
    def __init__(self, day, month, year):
        self.date_validation(day, month, year)

        self.day = day
        self.month = month
        self.year = year

    def __repr__(self):
        # day = self.day
        # month = self.month
        # if self.day < 10:
        #     day = f'0{day}'
        # if self.month < 10:
        #     month = f'0{month}'
        # return f'{day}-{month}-{self.year}'
        date = datetime(self.year, self.month, self.day)
        return date.strftime('%d-%m-%Y')

    @staticmethod
    def date_validation(day, month, year):
        try:
            datetime(year, month, day)
        except ValueError:
            raise ValueError('Not a valid date!')


date_1 = CustomDate(10, 8, 2000)
date_2 = CustomDate(8, 8, 2000)
date_3 = CustomDate(10, 11, 2000)
print(date_1)
print(date_2)
print(date_3)
# date_2 = CustomDate(50, 8, 2000)    # ValueError: Not a valid date!