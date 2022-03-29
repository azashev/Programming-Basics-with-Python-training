from math import ceil

people = int(input())
entrance = float(input())
price_per_chair = float(input())
price_per_umbrella = float(input())

price_entrance = people * entrance
price_umbrellas = ceil(people / 2) * price_per_umbrella
people_for_chair = ceil((people * 75) / 100)
price_for_chairs = people_for_chair * price_per_chair

total_price = price_entrance + price_for_chairs + price_umbrellas

print(f"{total_price:.2f} lv.")
