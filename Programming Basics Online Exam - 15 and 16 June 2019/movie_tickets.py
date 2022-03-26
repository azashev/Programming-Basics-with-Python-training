a1 = int(input())
a2 = int(input())
n = int(input())

ascii_a1 = chr(a1)
ascii_a2 = chr(a2)

symbol_one = ''

for s1 in range(a1, a2 - 1):
    symbol_one = chr(s1)
    for s2 in range(1, n - 1):
        for s3 in range(1, round(n / 2 - 1)):
            s4 = ord(symbol_one)
            if s1 % 2 != 0 and (s2 + s3 + s4) % 2 != 0:
                print(f"{symbol_one}-{s2}{s3}{s4}")
                continue
