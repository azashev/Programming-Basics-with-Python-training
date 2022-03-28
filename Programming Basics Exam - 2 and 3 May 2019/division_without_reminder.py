numbers = int(input())

divided_by_2_wr = 0
divided_by_3_wr = 0
divided_by_4_wr = 0
total_numbers = 0

for i in range(1, numbers + 1):
    current_number = int(input())
    if current_number % 2 == 0:
        divided_by_2_wr += 1
    elif current_number % 3 == 0:
        divided_by_3_wr += 1
    elif current_number % 4 == 0:
        divided_by_4_wr += 1

percent_divided_by_2 = (divided_by_2_wr / numbers) * 100
percent_divided_by_3 = (divided_by_3_wr / numbers) * 100
percent_divided_by_4 = (divided_by_4_wr / numbers) * 100

print(f"{percent_divided_by_2:.2f}%")
print(f"{percent_divided_by_3:.2f}%")
print(f"{percent_divided_by_4:.2f}%")