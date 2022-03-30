games_sold = int(input())

total_hearthstone = 0
total_fortnite = 0
total_overwatch = 0
total_others = 0

for i in range(1, games_sold + 1):
    game = input()
    if game == 'Hearthstone':
        total_hearthstone += 1
    elif game == 'Fornite':
        total_fortnite += 1
    elif game == 'Overwatch':
        total_overwatch += 1
    else:
        total_others += 1

percentage_hearthstone = (total_hearthstone / games_sold) * 100
percentage_fortnite = (total_fortnite / games_sold) * 100
percentage_overwatch = (total_overwatch / games_sold) * 100
percentage_others = (total_others / games_sold) * 100

print(f"Hearthstone - {percentage_hearthstone:.2f}%")
print(f"Fornite - {percentage_fortnite:.2f}%")
print(f"Overwatch - {percentage_overwatch:.2f}%")
print(f"Others - {percentage_others:.2f}%")