rent = int(input())

statuettes = rent - (rent * 0.3)
catering = statuettes - (statuettes * 0.15)
sound = catering / 2

total_costs = rent + statuettes + catering + sound

print(f"{total_costs:.2f}")