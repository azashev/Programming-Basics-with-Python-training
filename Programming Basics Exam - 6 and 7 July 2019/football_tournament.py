team = input()
matches_played_this_season = int(input())

total_points = 0
wins = 0
draws = 0
loses = 0

for i in range(1, matches_played_this_season + 1):
    result = input()
    if result == 'W':
        total_points += 3
        wins += 1
    elif result == 'D':
        total_points += 1
        draws += 1
    elif result == 'L':
        loses += 1

if matches_played_this_season < 1:
    print(f"{team} hasn't played any games during this season.")
elif matches_played_this_season > 0:
    win_rate = (wins / matches_played_this_season) * 100
    print(f"{team} has won {total_points} points during this season.")
    print("Total stats:")
    print(f"## W: {wins}")
    print(f"## D: {draws}")
    print(f"## L: {loses}")
    print(f"Win rate: {win_rate:.2f}%")