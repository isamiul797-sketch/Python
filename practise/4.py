input=list(map(int,input().split()))

A=input[0]
N=None

for num in input[1:]:
    if num > 0:
        N= num
        break

if N:
    total=0
    for i in range(A ,N+A):
        total+=i
    print(total)