class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
    def introduce(self):
        print("I am", self.name)
student1 = Student("Perumal", 101)
student2 = Student("Kavitha", 102)
student1.introduce()
student2.introduce()