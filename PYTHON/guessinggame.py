from random import randint

for x in range(1,6):
    guessnumber = int(input("Ente Guess Number Between 1 to 5:"))
    randomnumber = randint(1,5)

    if guessnumber == randomnumber:
        print("You Have Won")
    else:
        print("You Have Lost")
        print("Random Number Was:",randomnumber)
