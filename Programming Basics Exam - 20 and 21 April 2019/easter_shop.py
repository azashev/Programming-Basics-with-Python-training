eggs_total_amount = int(input())

condition = False
close = False

sold_eggs = 0

while True:
    command = input()
    if command == 'Close':
        close = True
        break
    eggs_amount = int(input())

    if command == 'Buy':
        if eggs_amount > eggs_total_amount:
            condition = True
            break
        else:
            eggs_total_amount -= eggs_amount
            sold_eggs += eggs_amount
    elif command == 'Fill':
        eggs_total_amount += eggs_amount

if close:
    print("Store is closed!")
    print(f"{sold_eggs} eggs sold.")

if condition:
    print("Not enough eggs in store!")
    print(f"You can buy only {eggs_total_amount}.")