amount=10000
int=3.5
years=7

future_value=amount*((1+(0.01*int))**years)

#print(f"{future_value:.2f}")
print(round(future_value, 2))