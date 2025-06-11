class Student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks

    def display_info(self):
        print("Name:", self.name)
        print("Marks:", self.__marks)

    def get_marks(self):
        return self.__marks

    def set_marks(self, new_marks):
        if new_marks >= 0:
            self.__marks = new_marks

s1 = Student("Alice", 85)
s1.display_info()

p1 = s1.get_marks()
s1.set_marks(90)
s1.display_info()
s2 = Student("Bob", 75)
s2.display_info()
s2.set_marks(80)
s2.display_info()
s3 = Student("Charlie", 95)
s3.display_info()

s3.set_marks(100)
s3.display_info()
s4 = Student("David", 65)
s4.display_info()
s4.set_marks(70)

s4.display_info()
s5 = Student("Eve", 55)
s5.display_info()
s5.set_marks(60)
s5.display_info()
s6 = Student("Frank", 45)

s6.display_info()
s6.set_marks(50)
s6.display_info()
print("All students have been created and their information displayed.")
