#Name:Pravalika Rao Chitneni
#CompletionDate:24/11/2023 06.00AM


#Here we have created Student Class,Constructor and toString methods are used.
#Constructor used for the object initialisation and address is allocated to that object,so that during runtime code execution flow will be executed
#Here Class Student will take three params as name,major,college and by using toSting method are printing the local variables
#
#
#Now we are creating another class Graduate class which will inherit the Student class data
#Graduate class will takes another 5 parameter and it will do same execution
#  Graduate Class will takes student as param's and this is the way to decleration of the Inheritance
# Class ChildrenClass:-GraduateStudent
# Class ParentClass:-Student
# ChildrenClass(ParentClass):
# super().__init__(name, major, college) is the way to call the Parent Constructor from the Children.

class Student:
    def __init__(self, name, major,college):
        self.name = name
        self.college = college
        self.major = major

    def __str__(self):
        return f"{self.name} is a/an {self.major} student at {self.college}"


class GraduateStudent(Student):
    def __init__(self, name,major,college, project, scholarship):
        super().__init__(name, major, college)
        self.project = project
        self.scholarship = scholarship

    def __str__(self):
        return super().__str__() + f",working on project {self.project},receiving ${self.scholarship} as scholarship"


# Example usage:
student1 = Student("Steve", "English Student", "NEC")
print(student1)

grad_student1 = GraduateStudent("Mery", "CS graduate", "Harvard", "Project AI",3500)
print(grad_student1)

student2 = Student("Alicia", "Mechanical Engineering", "MIT")
print(student2)

grad_student2 = GraduateStudent("John", "Mechanical Engineering", "Yale", "Dream Anlysis",7800)
print(grad_student2)
