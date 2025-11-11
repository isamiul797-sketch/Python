n = input("Enter a text of numbers : ")

list = n.split()

sum = 0
for num in list:
    sum = sum + int(num)

print(sum)

numofWords = 0
numofDigits = 0
numofLatters = 0

text = input("Enter your text : ")

for x in text:
    x = x.lower()
    if x >= 'a' and x <= 'z':
        numofLatters = numofLatters + 1

    elif x >= '0' and x <= '9':
        numofDigits = numofDigits + 1
    elif x == " ":
        numofWords = numofWords + 1

print("Number of latters:",numofLatters)
print("Number of digits:",numofDigits)
print("Number of words:",numofWords + 1)
