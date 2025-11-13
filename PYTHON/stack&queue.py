#Stack - last in first out

books = []
books.append("learn C")
books.append("learn C++")
books.append("learn Java")

print(books)

books.pop()
print(books)

books.pop()
print(books)

books.pop()
if not books :
    print("No Book Is Left")

#Queue - first in first out

from collections import deque

bank = deque(["Anik","Sanu","Mamu"])
print(bank)

bank.popleft()
print(bank)

bank.popleft()
print(bank)

bank.popleft()
if not bank:
    print("No Person Is Left")