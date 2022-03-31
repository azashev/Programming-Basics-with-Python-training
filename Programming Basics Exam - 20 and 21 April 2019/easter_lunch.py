easter_cakes = int(input())
eggshells = int(input())
cookies_kg = int(input())

price_easter_cakes = easter_cakes * 3.20
eggs = eggshells * 12
price_eggshells = eggshells * 4.35
price_cookies = cookies_kg * 5.40
price_paint_for_eggs = eggs * 0.15

total_price = price_easter_cakes + price_eggshells + price_cookies + price_paint_for_eggs

print(f"{total_price:.2f}")