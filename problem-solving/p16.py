n=int(input())

data = list(map(int,input().split()))

if len(data) != n:
    raise ValueError(f"Expected {n} integers but got {len(data)}.")



t = tuple(data)
print(hash(t))