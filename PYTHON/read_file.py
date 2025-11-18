file = open("PYTHON/student.txt","r+")

text = file.read()
print(text)

size = len(text)
print(size)

file.seek(0)       # RESET FILE POINTER

text2 = file.readlines()[1]
print(text2)

file.close()