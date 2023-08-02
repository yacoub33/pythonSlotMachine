def deposit(self):
    while True:
        amount = input('What would you like to deposit? ')
        if amount.isdigit():
            amount = int(amount)