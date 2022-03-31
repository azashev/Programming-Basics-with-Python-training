from math import floor

points = 0
winner = ''

multiplication = False
division = False

while True:
    current_points = 0
    multiplication = False
    division = False
    word = input()
    if word == 'End of words':
        break
    for i in range(len(word)):
        if i == 0:
            if word[i] == 'a' or word[i] == 'e' or word[i] == 'i' or word[i] == 'o' or word[i] == 'u' or word[i] == 'y' or word[i] == 'A' or word[i] == 'E' or word[i] == 'I' or word[i] == 'O' or word[i] == 'U' or word[i] == 'Y':
                multiplication = True
        if not multiplication:
            division = True

        current_points += ord(word[i])
    if multiplication:
        current_points = current_points * len(word)
    elif division:
        current_points = floor(current_points / len(word))

    if current_points > points:
        points = current_points
        winner = word

print(f"The most powerful word is {winner} - {points}")