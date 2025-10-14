n=int(input())

for _ in range(n):
    x, y=map(int,input().split())

    if y== 0:
        print("divisao impossivel")

    else:
        result=x/y
        print(f"{result:.1f}")