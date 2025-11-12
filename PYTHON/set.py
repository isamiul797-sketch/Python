num1 = {1,2,3,4,5}
num2 = set([3,4,5,6])
num2.add(7)
num2.remove(6)

print(4 not in num2)
print(num1 | num2)
print(num1 & num2)
print(num1 - num2)