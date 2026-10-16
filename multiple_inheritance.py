class Teacher :
    def __init__(self, salary) :
        self.salary = salary

class Student :
    def __init__(self, name, gpa) :
        self.name = name
        self.gpa = gpa

class TA(Teacher, Student):
    def __init__(self, salary, name, gpa) :
        super().__init__(salary) 
        Student.__init__(self, name, gpa)

ta1 = TA(15_000, "Hemant", 9.3)

print(f"Hello! {ta1.name} your salary is Rs.{ta1.salary} and your GPA is {ta1.gpa}")