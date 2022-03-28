term_of_contract = input()
type_of_contract = input()
added_internet = input()
months_to_pay = int(input())

costs = 0

if term_of_contract == 'one':
    if type_of_contract == 'Small':
        costs = 9.98
    elif type_of_contract == 'Middle':
        costs = 18.99
    elif type_of_contract == 'Large':
        costs = 25.98
    elif type_of_contract == 'ExtraLarge':
        costs = 35.99
elif term_of_contract == 'two':
    if type_of_contract == 'Small':
        costs = 8.58
    elif type_of_contract == 'Middle':
        costs = 17.09
    elif type_of_contract == 'Large':
        costs = 23.59
    elif type_of_contract == 'ExtraLarge':
        costs = 31.79

if added_internet == 'yes':
    if costs <= 10:
        costs += 5.50
    elif 30 >= costs > 10:
        costs += 4.35
    elif costs > 30:
        costs += 3.85

total_cost = costs * months_to_pay

if term_of_contract == 'two':
    total_cost -= (total_cost * 3.75) / 100

print(f"{total_cost:.2f} lv.")