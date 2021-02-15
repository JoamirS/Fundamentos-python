class CheckingAccount:
    def __init__(self, code):
        self.code = code
        self.balance = 0
        self.account_holder_name = ''

    def cash_deposit(self, value):
        self.balance += value

    def __str__(self):
        return "[Nome: {2} Código: {0} Saldo: {1} ]".format(self.code, self.balance, self.account_holder_name)

    def deposit_all_accounts(accounts):
        for account in accounts:
            account.cash_deposit(100)

    def add_account_name(self, nome_account):
        self.account_holder_name = nome_account


joamir_account = CheckingAccount(15)
joamir_account.add_account_name("Joamir")
print(joamir_account)

danny_account = CheckingAccount(1)
danny_account.add_account_name("Danny")
print(danny_account)

joamir_account.cash_deposit(1000)
print(joamir_account)
