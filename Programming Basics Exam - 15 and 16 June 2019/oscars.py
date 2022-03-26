name_actor = input()
points = float(input())
evaluators = int(input())

sum_points = 0
condition = False

for i in range(1, evaluators + 1):
    name_evaluator = input()
    points_evaluator = float(input())

    points += (len(name_evaluator) * points_evaluator) / 2

    if points > 1250.5:
        condition = True
        break

if condition:
    print(f"Congratulations, {name_actor} got a nominee for leading role with {points:.1f}!")
else:
    diff = abs(1250.5 - points)
    print(f"Sorry, {name_actor} you need {diff:.1f} more!")