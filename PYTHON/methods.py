class Student:
    roll = ""
    cgpa = ""

    def set_value(self,roll,cgpa):
        self.roll = roll
        self.cgpa = cgpa

    def display(self):
        print(f"Roll : {self.roll}, CGPA : {self.cgpa}")

        

sami = Student()
sami.set_value(101,3.89)
sami.display()

sani = Student()
sani.set_value(202,2.98)
sani.display()