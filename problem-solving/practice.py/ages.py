total=0
count=0

while True:
    ages=int(input())
    if ages<0:
        break
    total+=ages
    count+=1

average=total/count
print(f"{average:.2f}")