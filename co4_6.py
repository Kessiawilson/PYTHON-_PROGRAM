class Student:
    def __init__(self, name,age):
        self.name = name
        self.age = age
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
class Sem1(Student):
    def __init__(self,name,age,mark):
        super().__init__(name,age)
        self.mark = mark 

    def display(self):
        print("Name:", self.name)
        print("age:", self.age)
        print("mark:", self.mark)
class Result(Sem1):
    def __init__(self,name,age,mark,grade):
        super().__init__(name,mark,age) 
        self.grade = grade


    def display(self): 
        print("Name:", self.name)
        print("age:", self.age)
        print("mark:", self.mark)
        print("grade:", self.grade)


k=Result("Kessia",25,95,"A+")
k.display()
