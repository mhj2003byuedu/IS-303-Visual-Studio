# Dictionary containing 5 lists
student_data = {
    "names": ["Alice", "Bob", "Charlie", "Diana", "Ethan"],
    "ages": [20, 21, 19, 22, 20],
    "majors": ["Math", "Biology", "History", "Computer Science", "Physics"],
    "gpas": [3.8, 3.4, 3.6, 3.9, 3.5],
    "graduated": [False, False, False, True, False]
}

# Example: Accessing data
print(student_data["names"])        # prints the names list
print(student_data["gpas"][3])      # prints Diana's GPA