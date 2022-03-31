current_winner = ''
points = 0

#if there are multiple winners, second player included, then second player wins
special_points = 0
special_winner = ''
special_result = 0

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
        max_result = points
        current_winner = player
        if special_points == 2:
            special_winner = player
            special_result = max_result

if special_result >= max_result:
    print(f"The winner is {special_winner} with {special_result} points!")
else:
    print(f"The winner is {current_winner} with {max_result} points!")