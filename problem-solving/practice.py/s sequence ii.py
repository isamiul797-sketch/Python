s = 0
numerator = 1
denominator = 1

for i in range (20):
    numerator = 2 * i + 1
    denominator = 2 ** i
    s+=numerator/denominator

print(f"{s:.2f}")