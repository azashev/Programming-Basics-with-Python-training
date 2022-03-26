budget = float(input())
number_serials = int(input())

needed_money = 0

for i in range(1, number_serials + 1):
    name_serial = input()
    price_serial = float(input())

    if name_serial == 'Thrones':
        price_serial -= price_serial * 0.5
    elif name_serial == 'Lucifer':
        price_serial -= price_serial * 0.4
    elif name_serial == 'Protector':
        price_serial -= price_serial * 0.3
    elif name_serial == 'TotalDrama':
        price_serial -= price_serial * 0.2
    elif name_serial == 'Area':
        price_serial -= price_serial * 0.1

    needed_money += price_serial

diff = abs(needed_money - budget)

if budget >= needed_money:
    print(f"You bought all the series and left with {diff:.2f} lv.")
else:
    print(f"You need {diff:.2f} lv. more to buy the series!")