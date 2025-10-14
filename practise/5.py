X=int(input())

while True:
    Z=int(input())
    if Z>X:
        break

total=0
count=0
current=X

while total <= Z:
    total+=current
    count+=1
    current+=1

print(count)
