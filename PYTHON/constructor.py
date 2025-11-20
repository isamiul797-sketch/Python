class Student:
    roll = ""
    cgpa = ""

    def __init__(self,roll,cgpa):
        self.roll = roll
        self.cgpa = cgpa

    def display(self):
        print(f"Roll : {self.roll}, CGPA : {self.cgpa}")

        

sami = Student(101,3.89)
sami.display()

sani = Student(202,2.98)
sani.display()