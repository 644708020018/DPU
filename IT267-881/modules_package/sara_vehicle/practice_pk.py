from Cusorder import customer , order

cus = customer.Customer("jame","nontaburi")
ord = order.Order("15-06-2022", "packed")

print(f'Order of {cus.cus_name} ON {ord.date} Is {ord.status}')