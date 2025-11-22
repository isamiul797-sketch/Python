# class phone:
#     def __init__(self):
#         print("you can call")


# class samsung(phone):
#     def __init__(self):
#         super().__init__()
#         print("you can take photo")

# s= samsung()

#A practical example of inheritance

class shape:
    def __init__(self,dim1,dim2):
        self.dim1 = dim1
        self.dim2 = dim2

    def area(self):
        print("I am the area method of shape class")

class triangle(shape):
    def area(self):
        area = 0.5 * self.dim1 * self.dim2
        print("Area of Triangle", area)

class ractangle(shape):
    def area(self):
        area = self.dim1 * self.dim2
        print("Area of Ractangle", area)

t1 = triangle(20,30)
t1.area()

r1 = ractangle(20,30)
r1.area()