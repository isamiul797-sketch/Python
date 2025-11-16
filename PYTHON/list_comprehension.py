num = [1,2,3,4,5]
num2 = [1,2,3,4,5,6]

result = [x*x for x in num]
print(result)

result2 = [x for x in num2 if x%2 != 0]
print(result2)