# Mo Jansson
# Chapter 16 and lists
# Enter variables

sStudentID = input("Enter Student ID: ")
sFirstName = input("Enter First Name: ").upper()
sLastName = input("Enter Last Name: ").upper()
fGPA = float(input("Enter Student's GPA (to 2 decimal places): "))
round(fGPA, 2)

# print(f'{sStudentID} {sFirstName} {sLastName} {fGPA}')

listStudent = []
# listStudent.append(sStudentID)
# listStudent.append(sFirstName)
# listStudent.append(sLastName)
# listStudent.append(fGPA)
listStudent.append([sStudentID, sFirstName, sLastName, fGPA])

sStudentID = input("Enter Student ID: ")
sFirstName = input("Enter First Name: ").upper()
sLastName = input("Enter Last Name: ").upper()
fGPA = float(input("Enter Student's GPA (to 2 decimal places): "))
round(fGPA, 2)

listStudent.append([sStudentID, sFirstName, sLastName, fGPA])

print(listStudent[0][1])
print(listStudent[1][2])

listStudent.pop()