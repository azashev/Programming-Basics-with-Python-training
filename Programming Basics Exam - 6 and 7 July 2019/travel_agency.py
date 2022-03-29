city = input()
package = input()
vip = input()
days = int(input())

price_per_day = 0

if city == 'Bansko' or city == 'Borovets':
    if package == 'withEquipment':
        price_per_day += 100
        if vip == 'yes':
            price_per_day -= price_per_day * 0.1
    elif package == 'noEquipment':
        price_per_day += 80
        if vip == 'yes':
            price_per_day -= price_per_day * 0.05
elif  city == 'Varna' or city == 'Burgas':
    if package == 'withBreakfast':
        price_per_day += 130
        if vip == 'yes':
            price_per_day -= price_per_day * 0.12
    elif package == 'noBreakfast':
        price_per_day += 100
        if vip == 'yes':
            price_per_day -= price_per_day * 0.07