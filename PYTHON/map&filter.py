#map

def sqr(x):
    return x*x

num = [1,2,3,4,5]

result2 = list(filter(lambda x:x%2 == 0,num))
result1 = list(map(sqr,num))
print(result2)
print(result1)

#filter

