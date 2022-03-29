number_of_days = int(input())
hours_per_day = int(input())

cost_per_day = 0
total_cost = 0

for d in range(1, number_of_days + 1):
    cost_per_day = 0
    for h in range(1, hours_per_day + 1):
        if d % 2 == 0 and h % 2 != 0:
            cost_per_day += 2.5
            total_cost += 2.5
        elif d % 2 != 0 and h % 2 == 0:
            cost_per_day += 1.25
            total_cost += 1.25
        else:
            cost_per_day += 1
            total_cost += 1

    print(f"Day: {d} - {cost_per_day:.2f} leva")

print(f"Total: {total_cost:.2f} leva")