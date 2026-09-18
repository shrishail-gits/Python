class Student:
    total_students=0
    def __init__(self,name,roll_no,marks):
        self.name=name
        self.roll_no=roll_no
        self.marks=marks
        Student.total_students +=1
    def display(self):
        print("Name:",self.name)
        print("Roll No:",self.roll_no)
        print("Marks:",self.marks)

    @staticmethod
    def validate_marks(marks):
        return 0 <= marks <=100

    @classmethod
    def show_total_students(cls):
        print("Total Students:",cls.total_students)

s1=Student("Shrishail",101,85)
s2=Student("Rahul",102,90)

s1.display()
print()
s2.display()
print()
Student.show_total_students()
print("valid marks:",Student.validate_marks(85))