

class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.assignments = {}

    def add_assignment(self, assignment_name, grade):
        self.assignments[assignment_name] = grade

    def display_grades(self):
        return f"Grades: {self.assignments}"

class Instructor:
    def __init__(self, name, course_name):
        self.name = name
        self.course_name = course_name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def assign_grade(self, student, assignment_name, grade):
        student.add_assignment(assignment_name, grade)

    def display_students_grades(self):
        for student in self.students:
            print(f"{student.name} ({student.student_id}): {student.display_grades()}")


instructor = Instructor("Mr. Smith", "Intro to Python")
student1 = Student("John", "S123")
student2 = Student("Jane", "S124")

instructor.add_student(student1)
instructor.add_student(student2)

instructor.assign_grade(student1, "Assignment 1", 85)
instructor.assign_grade(student2, "Assignment 1", 90)

instructor.display_students_grades()
