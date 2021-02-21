class SalaryAccount:
    def __init__(self, code):
        self._code = code
        self._balance = 0

    def __eq__(self, other):
        if type(other) != SalaryAccount:
            return False

        return self._code == other._code and self._balance == other._balance

    def deposit(self, value):
        self._balance += value

    def __str__(self):
        return "[> Código: {} Saldo: {} <]".format(self._code, self._balance)


account_one = SalaryAccount(10)
account_two = SalaryAccount(10)
print(account_one)
print(account_two)

object_comparator = account_one == account_two
print(object_comparator)
