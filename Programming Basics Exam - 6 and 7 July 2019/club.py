wanted_profit = float(input())

profit_for_the_day = 0

condition = False

while True:
    cocktail_name = input()
    if cocktail_name == 'Party!':
        condition = True
        break
    cocktails_to_order = int(input())
    price_for_cocktails = int(len(cocktail_name)) * cocktails_to_order
    if price_for_cocktails % 2 != 0:
        price_for_cocktails -= price_for_cocktails * 0.25
    profit_for_the_day += price_for_cocktails
    if wanted_profit <= profit_for_the_day:
        break
if condition:
    diff = wanted_profit - profit_for_the_day
    print(f"We need {diff:.2f} leva more.")
else:
    print(f"Target acquired.")
print(f"Club income - {profit_for_the_day:.2f} leva.")