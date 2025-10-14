N=int(input())

for _ in range (1,N+1):
    X,Y=map(int,input().split())

    if X % 2 ==0:
        X+=1

    total=0
    for i in range(Y):
        total+= X+2*i

    print(total)