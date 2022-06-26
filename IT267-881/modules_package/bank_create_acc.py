from bank.Customer import Customer
from bank.Account import Account

paul = Customer()
paul.new_customer()

paul_acc = Account()
paul_acc.open_account(paul.name, 'Seving', '0123-4567', 500)

print (paul.customer_info())

print (paul_acc.desplay_balance())
