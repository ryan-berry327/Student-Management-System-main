from Student import Student
from Teacher import Teacher

class Course:
    def __init__(self, course_name, course_code,teacher,students,grades,max_students):
        self.course_name = course_name
        self.course_code = course_code
        self.teacher = teacher
        self.students = students if students is not None else []
        self.grades = grades if grades is not None else {}  
        self.max_students = max_students
    
    # Takes a techer object and assigns to the course
    def assign_teacher(self,teacher):
        if not isinstance(teacher, Teacher):
            raise TypeError("Only Teacher objects can be assigned.")
        if self.teacher is None or self.teacher != teacher:
            self.teacher = teacher
            return True
        else:
            print(f"The teacher {teacher.name} is already assigned to this course {self.course_name}")
            return False


    # Adds a student object to the list of enrolled students
    def enroll_student(self, student):
        if len(self.students) < self.max_students: # if there is still room in the class
            self.students.append(student)
            self.grades[student] = 0  # initialise students grades to 0
            return True
        else:
            print(f"Course {self.course_name} is full!")
            return False

    def remove_student(self,student):
        if student in self.students:
            self.students.remove(student)
            if student in self.grades: # ensures the student has grades before popping
                self.grades.pop(student) # dictionary so use pop

    def assign_grade(self, student, grade):
        if student in self.students: # if the student is enrolled the class add their grade
            if isinstance(grade,(int,float)) and 0 <= grade <= 100:
                self.grades[student] = grade # Store a single grade per student
            else:
                print("Invalid grade! Grades must be a number between 0 and 100.")
        else:
            print(f"{student.name} is not enrolled in {self.course_name}")

    def calculate_average_grade(self):
        valid_grades = [grade for grade in self.grades.values() if grade > 0]  # Ignore 0s
        
        if not valid_grades:  # If no valid grades, return 0
            return 0
        
        return sum(valid_grades) / len(valid_grades)

    def list_students(self):
        print(f"Enrolled Students:")
        for i, student in enumerate(self.students, start = 1):
            print(f"{i}. {student.name.title()}") # looping through self.students so when using student variable do not need self

    def course_summary(self):
        teacher_name = self.teacher.name if self.teacher else "No teacher assigned"
        return (f"The course {self.course_name} (Code: {self.course_code}) is taught by {teacher_name}. "
                f"Number of students enrolled: {len(self.students)}. "
                f"Average course grade: {self.calculate_average_grade():.2f}")

if __name__ == "__main__":
    # Create a teacher
    teacher1 = Teacher(
        name="Dr. Smith",
        age=31,
        id_number="T001",          # Example ID
        teacher_id="TS001",        # Example Teacher ID
        courses_taught=["Calculus 101", "Algebra 101"],  # Example courses
        office_hours="9 AM - 12 PM"  # Example office hours
    )

    # Create students
    student1 = Student("Alice", 16, "12345")
    student2 = Student("Bob", 17,"12346")
    student3 = Student("Charlie",22, "12347")

    # Create a course
    course = Course(course_name="Calculus 101", course_code="MATH101", teacher=teacher1, students=[], grades={}, max_students=3)

    # Test assigning a teacher
    print(course.assign_teacher(teacher1))  # Should print the teacher assignment message

    # Test enrolling students
    print(course.enroll_student(student1))  # Should return True and add student1 to the course
    print(course.enroll_student(student2))  # Should return True and add student2 to the course
    print(course.enroll_student(student3))  # Should return True and add student3 to the course
    print(course.enroll_student(student1))  # Should return False since student1 is already enrolled

    # Test assigning grades
    course.assign_grade(student1, 90)  # Assigning a valid grade
    course.assign_grade(student2, 85)  # Assigning a valid grade
    course.assign_grade(student3, 88)  # Assigning a valid grade
    course.assign_grade(student1, -5)  # Should print an error since the grade is invalid

    # Test removing a student
    course.remove_student(student2)  # Should remove student2 and their grade
    print(course.list_students())  # Should list student1 and student3 only

    # Test calculating the average grade
    print(f"Average Grade: {course.calculate_average_grade()}")  # Should print the average of the remaining students' grades

    # Test course summary
    print(course.course_summary())  # Should print a summary with teacher name, number of students, and average grade
