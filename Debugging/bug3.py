S = 0
Numerator = 1
Denominator = 1

while Numerator <= 39:
    S += Numerator / Denominator
    Numerator += 2
    Denominator *= 2

print(f"Sum = {S}")
print(f"Formatted output: {S:.2f}")
