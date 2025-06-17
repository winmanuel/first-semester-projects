students = []

def add_student():
    """
    TODO: Prompt the user to enter student name, age, and grade.
    Append the student as a dictionary to the students list.
    """
    name = input('please what is your name')
    age = int(input('How old are you'))
    grade = int(input('what is your grade'))
    students.append({"name": name, "age": age, "grade": grade})


def view_students():
    """
    TODO: Loop through the students list and print each student's info.
    """
    for student in students:
        print("Name :", student['name'])
        print("Age :", student['age'])
        print("Grade :", student['grade'])
        print()


def get_average_grade():
    """
    TODO: Return the average grade of all students.
    """
    for student in students:
        total = 0
    for student in students:
        total += student['grade']

    if len(students) > 0:
        avg = total / len(students)
        print("Average grade :", avg)
    else:
        print("No students available.")
