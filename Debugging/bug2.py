#bug01
def average(numbers):
    if len(numbers)==0:
        return 0
    return sum(numbers) / len(numbers)

print(average([]))  # Expected: Should handle empty list gracefully
#bug02
def add_item(item, basket=None):
    if basket is None:
        basket=[]
    basket.append(item)
    return basket

print(add_item("apple"))  
print(add_item("banana"))  # Expected: ["banana"], but it adds to the previous list
#bug03
def countdown(n):
    while n <= 0:
        print("Blast off!")
        return
    while n > 0:
        print(n)
        n -= 1
    print("Blast off!")
   

  # Expected: Should print "Blast off!" only, but nothing happens
#bug04
text = "python is fun"
print(text.title())
#bug05
with open("data.txt", "w") as f:
    f.write("Hello, world!")


