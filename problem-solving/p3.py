students=[]

for _ in range(int(input())):
    name=input()
    score=float(input())
    students.append([name,score])

grade=[score for name,score in students]
sco_low=sorted(set(grade))[1]

names=[name for name,score in students if score== sco_low]
for name in sorted(names):
    print(name) 
