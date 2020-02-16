class BankAccount:
    def __init__(self, first_name, last_name, initial_balance):
        self.first_name = first_name
        self.last_name = last_name
        self.balance = initial_balance

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'


account_1 = BankAccount('Kate', 'Smith', 100)
print(f'Last name value: {account_1.last_name}')
print(f'Full name: {account_1.full_name}')

account_1.last_name = 'Taylor'
print(f'New last name value: {account_1.last_name}')
print(f'Full name after change: {account_1.full_name}')

# account_1.full_name = 'Jenny Jones'