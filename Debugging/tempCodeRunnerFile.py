total = 0
count = 0

while True:
    num = int(input("Enter number: "))
    if num < 0:
        break
    total += num
    count += 1
    
if count > 0:
    average = total / count
    print(f"Average is {average:.2f}")

else:
    print("No positive number entered")
