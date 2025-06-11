class Person:
    def __init__(self, name ):
        self.name = name
    def display_info(self):
        print("Name:", self.name)
class Student(Person):
    def __init__(self, name, marks):
        super().__init__(name)
        self.__marks = marks

    def display_info(self):
        super().display_info()
        print("Marks:", self.__marks)

    def get_marks(self):
        return self.__marks

    def set_marks(self, new_marks):
        if new_marks >= 0:
            self.__marks = new_marks
s1 = Student("Alice", 85)
s1.display_info()
p1 = s1.get_marks()
print("Marks accessed through getter:", p1)
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
