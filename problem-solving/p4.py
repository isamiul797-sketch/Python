N=int(input())

for _ in range(N):
    X=int(input())
    soma = 0

    for i in range(1,X//2+1):
        if X % i == 0:
            soma += i

    if soma == X:
        print(f"{X} eh perfeito")

    else:
        print(f"{X} nao eh perfeito")

    