from Course import Course
from Grade import Grade
from Student import Student
from Teacher import Teacher

def main():
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

    student1 = Student("Alice", 18, "3001")

    # Create a course
    course1 = Course("Math", "MATH101", None, [], {}, 30)

    # Enroll student in the course
    course1.enroll_student(student1)

    # Assign a grade to the student
    grade1 = Grade(student1, course1, 85, None)  # Initially setting letter grade as None

    # Calculate letter grade
    grade1.calculate_letter_grade()

    # Update the grade
    grade1.update_grade(92)  # Should change the grade and recalculate the letter grade

    # Get grade info
    print(grade1.get_grade_info())

    # Check if the grade is passing
    grade1.is_passing()

    
    # Create a student
    student1 = Student("Alice", 18, 3001)

    # Enroll in courses
    student1.enroll("Math")
    student1.enroll("Science")
    student1.enroll("Math")  # Should prevent duplicate

    # Assign grades
    student1.add_grade("Math", 90)
    student1.add_grade("Science", 85)
    student1.add_grade("English", 75)  # Should fail (not enrolled)

    # Display student info
    student1.display_info()  # Should show courses & GPA

    # Create a Teacher object
    teacher1 = Teacher("John Doe", 40, 101, "T001", ["Math", "Science"], "9 AM - 11 AM")
    
    # Assigning courses
    print(teacher1.assign_course("History"))  # Should add History
    print(teacher1.assign_course("Math"))     # Should indicate Math already exists
    
    # Removing courses
    print(teacher1.remove_course("Science"))  # Should remove Science
    print(teacher1.remove_course("English"))  # Should fail as English is not assigned
    
    # Assigning grades to students
    student1 = Student("Alice", 18, 3001, {}, [])
    student1.enroll("Math")  # Enroll Alice in Math
    print(teacher1.assign_grade(student1, "Math", 90))  # Pass course code and grade
    
    # View student's grades
    teacher1.view_student_grades(student1, "Math")  # Corrected method call
    
    # Checking student's enrollment in course
    print(teacher1.is_student_in_course(student1, "Math"))  # Should return True

if __name__ == '__main__':
    main()