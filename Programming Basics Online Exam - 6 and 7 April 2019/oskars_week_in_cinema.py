name_movie = input()
type_hall = input()
purchased_tickets = int(input())

total_profit = 0

if name_movie == 'A Star Is Born':
    if type_hall == 'normal':
        total_profit = purchased_tickets * 7.5
    elif type_hall == 'luxury':
        total_profit = purchased_tickets * 10.5
    elif type_hall == 'ultra luxury':
        total_profit = purchased_tickets * 13.5
elif name_movie == 'Bohemian Rhapsody':
    if type_hall == 'normal':
        total_profit = purchased_tickets * 7.35
    elif type_hall == 'luxury':
        total_profit = purchased_tickets * 9.45
    elif type_hall == 'ultra luxury':
        total_profit = purchased_tickets * 12.75
elif name_movie == 'Green Book':
    if type_hall == 'normal':
        total_profit = purchased_tickets * 8.15
    elif type_hall == 'luxury':
        total_profit = purchased_tickets * 10.25
    elif type_hall == 'ultra luxury':
        total_profit = purchased_tickets * 13.25
elif name_movie == 'The Favourite':
    if type_hall == 'normal':
        total_profit = purchased_tickets * 8.75
    elif type_hall == 'luxury':
        total_profit = purchased_tickets * 11.55
    elif type_hall == 'ultra luxury':
        total_profit = purchased_tickets * 13.95

print(f"{name_movie} -> {total_profit:.2f} lv.")