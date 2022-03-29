drink = input()
sugar = input()
number_of_drinks = int(input())

price_per_drink = 0

if drink == 'Espresso':
    if sugar == 'Without':
        price_per_drink = 0.9
    elif sugar == 'Normal':
        price_per_drink = 1
    elif sugar == 'Extra':
        price_per_drink = 1.2
if drink == 'Cappuccino':
    if sugar == 'Without':
        price_per_drink = 1
    elif sugar == 'Normal':
        price_per_drink = 1.2
    elif sugar == 'Extra':
        price_per_drink = 1.6
if drink == 'Tea':
    if sugar == 'Without':
        price_per_drink = 0.5
    elif sugar == 'Normal':
        price_per_drink = 0.6
    elif sugar == 'Extra':
        price_per_drink = 0.7

price = number_of_drinks * price_per_drink

if sugar == 'Without':
    price -= price * 0.35

if drink == 'Espresso' and number_of_drinks >= 5:
    price -= price * 0.25

if price > 15:
    price -= price * 0.2

print(f"You bought {number_of_drinks} cups of {drink} for {price:.2f} lv.")