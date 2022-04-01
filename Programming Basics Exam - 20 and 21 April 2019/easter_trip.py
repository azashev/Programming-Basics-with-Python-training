destination = input()
dates = input()
nights_number = int(input())

costs = 0

if destination == 'France':
    if dates == '21-23':
        costs = nights_number * 30
    elif dates == '24-27':
        costs = nights_number * 35
    elif dates == '28-31':
        costs = nights_number * 40
elif destination == 'Italy':
    if dates == '21-23':
        costs = nights_number * 28
    elif dates == '24-27':
        costs = nights_number * 32
    elif dates == '28-31':
        costs = nights_number * 39
elif destination == 'Germany':
    if dates == '21-23':
        costs = nights_number * 32
    elif dates == '24-27':
        costs = nights_number * 37
    elif dates == '28-31':
        costs = nights_number * 43

print(f"Easter trip to {destination} : {costs:.2f} leva.")
