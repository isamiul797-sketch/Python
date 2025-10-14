'''To open the file, use the built-in open() function.

The open() function returns a file object, which has a read() method for reading the content of the file:'''

f = open("demofile.txt" "w")
print(f.read())

#If the file is located in a different location, you will have to specify the file path, like this:

f = open("D:\\myfiles\welcome.txt")
print(f.read())

#Using the with statement
with open("demofile.txt") as f:
  print(f.read())

'''Close Files
It is a good practice to always close the file when you are done with it.

If you are not using the with statement, you must write a close statement in order to close the file:'''
f = open("demofile.txt")
print(f.readline())
f.close()

'''Read Only Parts of the File
By default the read() method returns the whole text, but you can also specify how many characters you want to return'''
with open("demofile.txt") as f:
  print(f.read(5))

'''Read Lines
You can return one line by using the readline() method:'''
with open("demofile.txt") as f:
  print(f.readline())