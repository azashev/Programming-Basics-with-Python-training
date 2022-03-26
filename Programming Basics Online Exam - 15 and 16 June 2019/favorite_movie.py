titles = 0

top_points = -9223372036854775807
top_movie = ''

while titles < 7:
    new_title = input()

    if new_title == 'STOP':
        break
    else:
        titles += 1
        current_points = 0

        for ch in new_title:
            current_points += ord(ch)
            if 122 >= ord(ch) >= 97:
                current_points -= 2 * len(new_title)
            elif 90 >= ord(ch) >= 65:
                current_points -= len(new_title)

        if current_points > top_points:
            top_points = current_points
            top_movie = new_title

if titles == 7:
    print(f"The limit is reached.")
print(f"The best movie for you is {top_movie} with {top_points} ASCII sum.")