# Mo Jansson
# Working with OOP

class Student :
    student_id = 0
    first_name = " "
    last_name = " "
    age = 0
    gpa = 0.0
    
    def __init__ (self, fName, lName) :
        self.first_name = fName
        self.last_name = lName
        self.gpa = 0.0

    def get_fullname(self) :
        return (self.last_name + ", " + self.first_name)

    def load_gpa (self, fGPA) :
        if (fGPA > 4.0):
            fGPA = 4.0
        elif (fGPA < 0.0):
            fGPA = 0.0
        self.gpa = fGPA

#Creates an object of type student
oStudent = Student(first_name, last_name, age)

oStudent.first_name = input("Enter the student's first name: ")
oStudent.last_name = input("Enter the student's last name: ")
oStudent.age = int(input("Enter the student's age: "))

oStudent.load_gpa(4.5)

print(oStudent.get_fullname())

