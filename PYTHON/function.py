def add (x,y):
    sum = x * y
    print(sum)

def addition(x,y,z):
    sum = x + y + z
    print(sum)

def sub (a,b):
    sub = a - b
    print(sub)

def message():
    print("No Message is Available")

add(20,80)
sub(190,40)
addition(21,70,90)
message()

#Returning value from function

def sqr(a,b):
    result = a * b
    return result

result = sqr(20,10)
print("Result Is = ",result)

def sqr(a,b):
    result = a * b
    return result

result = sqr(20,10)
print("Result Is = ",result)

def large(a,b):
    if a > b :
        return a
    else :
        return b


print("Large Number Is = ",large(20,100))