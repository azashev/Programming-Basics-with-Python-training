budget = float(input())
destination = input()
season = input()
days = int(input())

price_per_day = 0

if destination == 'Dubai':
    if season == 'Winter':
        price_per_day = 45000
    elif season == 'Summer':
        price_per_day = 40000
elif destination == 'Sofia':
    if season == 'Winter':
        price_per_day = 17000
    elif season == 'Summer':
        price_per_day = 12500
elif destination == 'London':
    if season == 'Winter':
        price_per_day = 24000
    elif season == 'Summer':
        price_per_day = 20250

total_price = days * price_per_day

if destination == 'Dubai':
    total_price -= total_price * 0.3
elif destination == 'Sofia':
    total_price += total_price * 0.25

diff = abs(budget - total_price)

if budget >= total_price:
    print(f"The budget for the movie is enough! We have {diff:.2f} leva left!")
else:
    print(f"The director needs {diff:.2f} leva more!")