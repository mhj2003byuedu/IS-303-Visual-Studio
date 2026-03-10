# Mo Jansson

class Student:
    def __init__(self):
        self.netid = ""
        self.first_name = ""
        self.last_name = ""
        self.courses = []

# Create course class
# Attributes are number and name
# Create the constructor too

class Course:
    def __init__(self, sCourseNum, sCourseName):
        self.number = sCourseNum
        self.name = sCourseName

oStud = Student()

lstStudents = []
bContinue = True

while bContinue == True:
    sInput = input("How many students do you want to enter? ")

    if sInput.isdigit():
        iCourseCnt = int(sInput)
        bContinue = False
    else:
        print("Enter a number")

for iCount in range (0, iCourseCnt):
    oStud = Student()
    oStud.netid = input("Enter netid: ")
    oStud.first_name = input("Enter first name: ")
    oStud.last_name = input("Enter last name: ")
    lstStudents.append(oStud)

for oStudent in lstStudents:
    print(oStudent.netid, oStudent.first_name, oStudent.last_name)