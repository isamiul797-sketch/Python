while True:
    N = int(input())
    if N == 0:
        break
    
    matrix = [[0] * N for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            matrix[i][j] = min(i, j, N - 1 - i, N - 1 - j) + 1
    
    for row in matrix:
        print(" ".join(f"{val:3d}" for val in row))
    print()
