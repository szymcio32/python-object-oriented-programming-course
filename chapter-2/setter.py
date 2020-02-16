class BankAccount:
    def __init__(self, first_name, last_name, initial_balance):
        self.first_name = first_name
        self.last_name = last_name
        self._balance = initial_balance

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if not isinstance(value, int):
            raise TypeError('The value should be integer')
        elif value < 0:
            raise ValueError('Negative amount is not allowed')
        self._balance = value


account_1 = BankAccount('Kate', 'Smith', 100)
account_1.balance = 250
print(f'Balance: {account_1.balance}')