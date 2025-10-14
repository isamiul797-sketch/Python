C=int(input())

T=input()

M=[]

for i in range(12):
    row=[]
    for j in range(12):
        num=float(input())
        row.append(num)
    M.append(row)

total = 0
for i in range(12):
    total += M[i][C]

if T == 'S':
    print(f"{total:.1f}")
elif T == 'M':
    print(f"{total/12:.1f}")
