budget_movie = float(input())
statists = int(input())
price_per_outfit = float(input())

decor = budget_movie * 0.1
price_outfits = statists * price_per_outfit

if statists > 150:
    price_outfits -= price_outfits * 0.1

total_costs = decor + price_outfits

diff = abs(budget_movie - total_costs)

if total_costs <= budget_movie:
    print("Action!")
    print(f"Wingard starts filming with {diff:.2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {diff:.2f} leva more.")