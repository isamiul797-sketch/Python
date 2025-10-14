N=int(input())

f1=0
f2=1

for i in range(N):
    if i == 0:
        print(f1,end="")
    elif i == 1:
        print(f" {f2}", end="")
    else:
        next_fib=f1+f2
        print(f" {next_fib}", end="")
        f1,f2=f2,next_fib
    
print()