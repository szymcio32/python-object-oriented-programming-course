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

    @classmethod
    def from_string(cls, string):
        day, month, year = map(int, string.split('-'))
        return cls(day, month, year)

    @classmethod
    def from_file(cls, file):
        array = []
        with open(file, 'r') as text_file:
            text_data = text_file.read().splitlines()
        for date in text_data:
            custom_date_obj = cls.from_string(date)
            array.append(custom_date_obj)
        return array


date_1 = CustomDate.from_string("4-2-2000")
print(date_1)

array_of_dates = CustomDate.from_file('text_file.txt')
print(array_of_dates)