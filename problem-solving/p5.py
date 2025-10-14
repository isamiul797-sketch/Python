import math

N=int(input())

for _ in range(N):
    X=int(input())
    eh_primo=True

    if X < 2:
        eh_primo=False

    else:
        for i in range(2,int(math.sqrt(X))+1):
            if X % i == 0:
                eh_primo = False
                break

    if eh_primo:
        print(f"{X} eh primo")
    else:
        print(f"{X} nao eh primo")