guests = int(input())
price_per_guest = float(input())
budget = float(input())

if 10 <= guests <= 15:
    price_per_guest -= price_per_guest * 0.15
elif 15 < guests <= 20:
    price_per_guest -= price_per_guest * 0.2
elif guests > 20:
    price_per_guest -= price_per_guest * 0.25

price_cake = budget * 0.1
price_guests = price_per_guest * guests

total_price = price_cake + price_guests

diff = abs(budget - total_price)

if total_price <= budget:
    print(f"It is party time! {diff:.2f} leva left.")
else:
    print(f"No party! {diff:.2f} leva needed.")