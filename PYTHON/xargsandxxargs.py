#xargs

def add(*numbers):
    sum = 0
    for num in numbers:
        sum = sum + num
    print(sum)
    
add(12,89)
add(12,89,90)
add(12,89,90,78)

#xxargs

def student(**details):
    print(details['cgpa'])

student(id=101,name="sami",cgpa=3.12)