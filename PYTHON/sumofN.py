N = int(input("enter a limit : "))
sum = 0
i = 1
while i <= N:
    sum = sum + i
    i = i + 1

print(sum)

#Break and Cintinue

i = 1

while i <= 100:
    print(i)
    i = i + 1
    if i == 20:
        break
print("Hey")
