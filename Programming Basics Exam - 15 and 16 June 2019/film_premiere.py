projection = input()
package = input()
tickets = int(input())

price = 0

if projection == 'John Wick':
    if package == 'Drink':
        price = 12 * tickets
    elif package == 'Popcorn':
        price = 15 * tickets
    elif package == 'Menu':
        price = 19 * tickets

elif projection == 'Star Wars':
    if package == 'Drink':
        price = 18 * tickets
    elif package == 'Popcorn':
        price = 25 * tickets
    elif package == 'Menu':
        price = 30 * tickets

elif projection == 'Jumanji':
    if package == 'Drink':
        price = 9 * tickets
    elif package == 'Popcorn':
        price = 11 * tickets
    elif package == 'Menu':
        price = 14 * tickets

if projection == 'Star Wars' and tickets >= 4:
    price -= price * 0.3
if projection == 'Jumanji' and tickets == 2:
    price -= price * 0.15

print(f"Your bill is {price:.2f} leva.")