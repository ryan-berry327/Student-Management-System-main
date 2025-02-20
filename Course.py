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
