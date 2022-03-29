from math import ceil

wall_height = int(input())
wall_width = int(input())
percentage_not_painted = int(input())

surface = (wall_height * wall_width) * 4
surface_to_paint = ceil(surface - ((surface * percentage_not_painted) / 100))

painted_surface = 0
paint = 0

tired = False
done = False

while True:
    l_paint = input()
    if l_paint == 'Tired!':
        tired = True
        break

    painted_surface += int(l_paint)
    paint += int(l_paint)
    if painted_surface >= surface_to_paint:
        done = True
        break

if tired:
    m_left = surface_to_paint - painted_surface
    print(f"{m_left} quadratic m left.")
elif paint > surface_to_paint:
    paint_left = paint - surface_to_paint
    print(f"All walls are painted and you have {paint_left} l paint left!")
elif paint == surface_to_paint:
    print(f"All walls are painted! Great job, Pesho!")