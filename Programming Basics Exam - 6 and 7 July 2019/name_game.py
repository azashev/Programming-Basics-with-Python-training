current_winner = ''
points = 0


special_points = 0
special_winner = ''
condition = False

max_result = 0

while True:
    player = input()
    if player == 'Stop':
        break
    points = 0
    for i in range(len(player)):
        number = int(input())
        if number == ord(player[i]):
            points += 10
        else:
            points += 2

    if points >= max_result:
        special_points += 1
        if special_points == 2:
            condition = True
            special_winner = player
        max_result = points
        current_winner = player

if condition:
    print(f"The winner is {special_winner} with {max_result} points!")
else:
    print(f"The winner is {current_winner} with {max_result} points!")