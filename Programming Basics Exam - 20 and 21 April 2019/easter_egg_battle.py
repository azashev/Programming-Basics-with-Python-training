eggs_first_player = int(input())
eggs_second_player = int(input())

condition = False

while True:
    command = input()
    if command == 'End':
        condition = True
        break
    if command == 'one':
        eggs_second_player -= 1
    elif command == 'two':
        eggs_first_player -= 1

    if eggs_first_player < 1 or eggs_second_player < 1:
        break


if eggs_first_player < 1:
    print(f"Player one is out of eggs. Player two has {eggs_second_player} eggs left.")
elif eggs_second_player < 1:
    print(f"Player two is out of eggs. Player one has {eggs_first_player} eggs left.")

if condition:
    print(f"Player one has {eggs_first_player} eggs left.")
    print(f"Player two has {eggs_second_player} eggs left.")
