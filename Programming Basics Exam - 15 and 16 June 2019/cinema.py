hall_capacity = int(input())

current_people = 0

command = False
hall_is_full = False
profit = 0

while True:
    new_people = input()

    if new_people == 'Movie time!':
        command = True
        break

    if int(new_people) + current_people > hall_capacity:
        hall_is_full = True
        break
    else:
        current_people += int(new_people)
        profit += int(new_people) * 5
        if int(new_people) % 3 == 0:
            profit -= 5

diff = abs(hall_capacity - current_people)

if command:
    print(f"There are {diff} seats left in the cinema.")
elif hall_is_full:
    print(f"The cinema is full.")

print(f"Cinema income - {profit} lv.")