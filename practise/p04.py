X=int(input())
Y=int(input())

start=min(X,Y)
end=max(X,Y)

for i in range(start+1,end):
    if i % 5 == 2 or i % 5 == 3:
        print(i)