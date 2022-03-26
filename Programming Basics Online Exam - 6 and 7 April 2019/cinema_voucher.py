voucher_value = int(input())

budget = voucher_value
costs = 0

tickets = 0
other_products = 0

while True:
    product = input()

    if product == 'End':
        break

    if len(product) > 8:
        current_cost = (ord(product[0]) + ord(product[1]))
        if current_cost > budget:
            break
        else:
            tickets += 1
            budget -= current_cost
    else:
        current_cost = ord(product[0])
        if current_cost > budget:
            break
        else:
            other_products += 1
            budget -= current_cost

print(f"{tickets}")
print(f"{other_products}")