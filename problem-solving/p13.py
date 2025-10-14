T=int(input())
N=[]

for i in range(1000):
    N.append( i % T )
    print(f"N[{i}] = {N[i]}")