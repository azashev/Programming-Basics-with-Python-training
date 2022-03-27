budget = float(input())
needed_gas = float(input())
day_of_the_week = input()

gas_costs = needed_gas * 2.10
guide_costs = 100
total_costs = gas_costs + guide_costs

if day_of_the_week == 'Saturday':
    total_costs -= total_costs * 0.1
else:
    total_costs -= total_costs * 0.2

diff = abs(budget - total_costs)

if budget >= total_costs:
    print(f"Safari time! Money left: {diff:.2f} lv. ")
else:
    print(f"Not enough money! Money needed: {diff:.2f} lv.")