import os.path

print(os.path.isfile('p01.py'))
print(os.path.exists('p02.py'))



my_file = open('main.py')

try:
    my_file.close()
    print("File found")

except FileNotFoundError:
    print("File not found!")