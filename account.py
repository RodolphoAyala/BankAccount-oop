from hashlib import sha256


class BankAccount:
    def __init__(self, account_id: int, name: str, balance: float = 0, password: str = None):
        self._id = account_id
        self._name = name
        self.__balance = balance

        if password is None:
            password = self.request_password()

        self.__hash = sha256(password.encode()).hexdigest()

    def deposit(self, amount):
        amount = abs(amount)
        self.__balance += amount
        print(f'Deposit of ${amount:.2f} completed successfully.')

    def __str__(self):
        return f'''

Account = {self.id}
Owner = {self.name}
Balance = ${self.__balance:.2f}'''

    def withdraw(self, amount):
        if self.validate_password():
            if amount <= self.__balance:
                self.__balance -= amount
            else:
                print(f'Your balance is insufficient to withdraw ${amount:.2f}')
        else:
            print('Incorrect password.')

    def validate_password(self):
        from pwinput import pwinput

        password = pwinput('Enter your password: ')
        code = sha256(password.encode()).hexdigest()

        if code == self.__hash:
            return True
        else:
            return False

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        for attempts in range(3, 0, -1):
            if self.validate_password():
                self._name = new_name
                return
            else:
                print(f'Incorrect password! {attempts - 1} attempt(s) remaining.')

        print('Maximum attempts reached.')

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, new_id):
        raise PermissionError('It is not possible to change the account ID.')

    @property
    def balance(self):
        for attempts in range(3, 0, -1):
            if self.validate_password():
                return self.__balance
            else:
                print(f'Incorrect password! {attempts - 1} attempt(s) remaining.')

        return 'Maximum attempts reached.'

    def request_password(self):
        from pwinput import pwinput

        while True:
            password = pwinput('Create a password: ')

            if 5 <= len(password) <= 12:
                return password

            print('Password must contain between 5 and 12 characters.')