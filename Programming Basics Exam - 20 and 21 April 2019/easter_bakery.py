price_flour_per_kg = float(input())
flour_kg = float(input())
sugar_kg = float(input())
eggshells = int(input())
packages_yeast = int(input())

price_sugar_per_kg = price_flour_per_kg - (price_flour_per_kg * 0.25)
price_per_eggshell = price_flour_per_kg + (price_flour_per_kg * 0.1)
price_per_package_yeast = price_sugar_per_kg - (price_sugar_per_kg * 0.8)


price_flour = flour_kg * price_flour_per_kg
price_sugar = sugar_kg * price_sugar_per_kg
price_eggshells = eggshells * price_per_eggshell
price_yeast = packages_yeast * price_per_package_yeast

total_price = price_flour + price_sugar + price_eggshells + price_yeast

print(f"{total_price:.2f}")