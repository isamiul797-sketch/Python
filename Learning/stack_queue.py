'''books=[]

books.append("Learn c")
books.append("Learn c++")
books.append("Learn jave")
print(books)

books.pop()
print(f"Now the top book is: {books[-1]}")

books.pop()
print(f"Now the top book is: {books[-1]}")

books.pop()
if not books:
    print("No book left")'''

from collections import deque

bank=deque({"Sami","Sani","Alif"})
print(bank)

bank.popleft()
print(bank)

bank.popleft()
print(bank)
bank.popleft()
if not bank:
    print("No person left")


