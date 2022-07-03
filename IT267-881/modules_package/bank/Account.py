class Account:
    def __init__(self):
        self.acc_type = ''
        self.acc_no = ''
        self.balance = 0

    def open_account(self, acc_name, acc_type, acc_no, acc_balance=100):
        self.acc_name = acc_name
        self.acc_type = acc_type
        self.acc_no = acc_no
        self.acc_balance = acc_balance

    def desplay_balance(self):
        return f'{self.acc_name} a account balance {self.acc_balance} baht '

