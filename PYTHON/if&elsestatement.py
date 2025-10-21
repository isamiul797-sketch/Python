marks = 56

if marks >= 33:
    print("Pass")

else:
    print("Fail")

num1 = 90
num2 = 450

if num1 < num2:
    print(num2)

else:
    print(num1)

#even/odd
num = 9

if num%2 == 0:
    print("Even")
else:
    print("Odd")

#Uses of elif

mark = 30

if mark >= 90:
    print("A*")

elif mark >= 80:
    print("A+")

elif mark >= 70:
    print("A")

elif mark >= 60:
    print("A-")

elif mark >= 50:
    print("B")

elif mark >= 40:
    print("C")

elif mark >= 33:
    print("D")

else:
    print("F")

#Inner or nested if

num1 = 899
num2 = 798
num3 = 988

if num1 > num2:
    if num1 > num3:
        print(num1)
    else :
        print(num3)
else :
    print(num2)