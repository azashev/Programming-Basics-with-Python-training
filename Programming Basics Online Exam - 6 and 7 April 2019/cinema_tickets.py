
condition = False

student_tickets = 0
standard_tickets = 0
kid_tickets = 0

total_tickets_movies = 0

while True:
    total_tickets = 0
    name_movie = input()
    if name_movie == 'Finish':
        condition = True
        break

    free_seats = int(input())

    while total_tickets < free_seats:
        type_ticket = input()
        if type_ticket == 'End':
            break
        total_tickets += 1
        total_tickets_movies += 1

        if type_ticket == 'student':
            student_tickets += 1
        elif type_ticket == 'standard':
            standard_tickets += 1
        elif type_ticket == 'kid':
            kid_tickets += 1

    percentage_hall = (total_tickets * 100) / free_seats
    print(f"{name_movie} - {percentage_hall:.2f}% full.")

if condition:
    student_tickets_percentage = (student_tickets * 100) / total_tickets_movies
    standard_tickets_percentage = (standard_tickets * 100) / total_tickets_movies
    kid_tickets_percentage = (kid_tickets * 100) / total_tickets_movies
    print(f"Total tickets: {total_tickets_movies}")
    print(f"{student_tickets_percentage:.2f}% student tickets.")
    print(f"{standard_tickets_percentage:.2f}% standard tickets.")
    print(f"{kid_tickets_percentage:.2f}% kids tickets.")
