eggs_size = input()
eggs_color = input()
batches = int(input())

profit = 0

if eggs_size == 'Large':
    if eggs_color == 'Red':
        profit = batches * 16
    elif eggs_color == 'Green':
        profit = batches * 12
    elif eggs_color == 'Yellow':
        profit = batches * 9
elif eggs_size == 'Medium':
    if eggs_color == 'Red':
        profit = batches * 13
    elif eggs_color == 'Green':
        profit = batches * 9
    elif eggs_color == 'Yellow':
        profit = batches * 7
elif eggs_size == 'Small':
    if eggs_color == 'Red':
        profit = batches * 9
    elif eggs_color == 'Green':
        profit = batches * 8
    elif eggs_color == 'Yellow':
        profit = batches * 5

costs = profit * 0.35
total_profit = profit - costs

print(f"{total_profit:.2f} leva.")