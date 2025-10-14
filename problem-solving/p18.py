while True:
    N = int(input())
    if N == 0:
        break
    
    for i in range(N):
        row = []
        for j in range(N):
            if i == j:
                row.append(1)
            else:
                row.append(abs(i-j)+1)
        print(" ".join(f"{num:3d}" for num in row))
    print()
