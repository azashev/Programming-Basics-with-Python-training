budget = float(input())

products_amount = 0
price = 0
condition = False
nem = False

counter = 0
diff = 0

while True:
    name_of_product = input()
    if name_of_product == 'Stop':
        condition = True
        break
    price_of_product = float(input())

    counter += 1

    if counter == 3:
        price_of_product = price_of_product / 2
        counter = 0

    diff = abs(price_of_product - budget)

    if price_of_product > budget:
        nem = True
        break
    budget -= price_of_product
    price += price_of_product
    products_amount += 1

if condition:
    print(f"You bought {products_amount} products for {price:.2f} leva.")
if nem:
    print("You don't have enough money!")
    print(f"You need {diff:.2f} leva!")