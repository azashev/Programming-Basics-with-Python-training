from math import ceil

guests = int(input())
budget = float(input())

price_per_easter_brade = 4
price_per_egg = 0.45

needed_easter_breads = ceil(guests / 3)
needed_eggs = guests * 2

price_easter_bread = needed_easter_breads * price_per_easter_brade
price_eggs = needed_eggs * price_per_egg

total_costs = price_easter_bread + price_eggs
diff = abs(budget - total_costs)

if total_costs <= budget:
    print(f"Lyubo bought {needed_easter_breads} Easter bread and {needed_eggs} eggs.")
    print(f"He has {diff:.2f} lv. left.")
else:
    print("Lyubo doesn't have enough money.")
    print(f"He needs {diff:.2f} lv. more.")