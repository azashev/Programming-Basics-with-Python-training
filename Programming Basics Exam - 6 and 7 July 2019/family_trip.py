budget = float(input())
number_nights = int(input())
price_per_night = float(input())
percent_additional_costs = int(input())

if number_nights > 7:
    price_per_night -= price_per_night * 0.05

additional_costs = (budget * percent_additional_costs) / 100
costs_per_night = number_nights * price_per_night
total_costs = costs_per_night + additional_costs

diff = abs(budget - total_costs)

if total_costs <= budget:
    print(f"Ivanovi will be left with {diff:.2f} leva after vacation.")
else:
    print(f"{diff:.2f} leva needed.")