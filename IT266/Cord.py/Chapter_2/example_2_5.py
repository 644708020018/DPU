number_of_days = int(input("Enter number of days "))

number_of_years = int(number_of_days / 365)

number_of_weeks = int(number_of_days % 365 / 7)

remaining_number_of_days = int(number_of_days % 365 % 7)

print(f"Years = {number_of_years}, Weeks = {number_of_weeks}, Days = {remaining_number_of_days}")
