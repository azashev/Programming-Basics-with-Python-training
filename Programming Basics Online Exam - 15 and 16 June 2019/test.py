budget = float(input())

total_honorarium = 0

while True:
    name_of_actor = input()

    if name_of_actor == 'ACTION':
        break
    else:
        if len(name_of_actor) <= 15:
            reward = float(input())
            budget -= reward
            total_honorarium += reward
        if len(name_of_actor) > 15:
            budget -= budget * 0.2
            total_honorarium += budget * 0.2

    if budget < 0:
        break
if budget < 0:
    print(f"We need {abs(budget):.2f} leva for our actors.")
else:
    print(f"We are left with {budget:.2f} leva.")