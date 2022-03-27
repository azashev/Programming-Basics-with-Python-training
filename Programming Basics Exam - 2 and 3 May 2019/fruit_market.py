price_strawberries = float(input())
amount_bananas = float(input())
amount_oranges = float(input())
amount_raspberries = float(input())
amount_strawberries = float(input())

price_raspberries = price_strawberries / 2
price_oranges = price_raspberries * 0.6
price_bananas = price_raspberries * 0.2

total_cost_strawberries = price_strawberries * amount_strawberries
total_cost_raspberries = price_raspberries * amount_raspberries
total_cost_oranges = price_oranges * amount_oranges
total_cost_bananas = price_bananas * amount_bananas

total_price = total_cost_strawberries + total_cost_raspberries + total_cost_oranges + total_cost_bananas

print(f"{total_price:.2f}")