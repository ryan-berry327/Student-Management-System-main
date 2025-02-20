from Person import Person
from Student import Student

class Teacher(Person):
    def __init__(self,name, age,id_number,teacher_id,courses_taught,office_hours):
        super().__init__(name,age,id_number)
        self.teacher_id = teacher_id
        self.courses_taught = courses_taught
        self.office_hours = office_hours

    def assign_course(self,course):
        if course not in self.courses_taught:
            self.courses_taught.append(course)
            print(f"{course} has been added to {self.name}'s classes taught")
            return True
        else:
            print(f"{course} has been added to {self.name}'s classes taught")
            return False

    def remove_course(self, course):
        if course in self.courses_taught:
            self.courses_taught.remove(course)
            print(f"{course} has been removed from {self.name}'s classes taught")
            return True
        else:
            print(f"The course {course} does not exist in {self.name}'s taught courses")
            return False

    def assign_grade(self, student, course_code, grade):
        if course_code in self.courses_taught:  # Ensure teacher teaches the course
            if course_code in student.courses:  # Ensure student is enrolled in the course
                if 0 <= grade <= 100:  # Validate the grade
                    # Call add_grade method from Student class to set the grade
                    student.add_grade(course_code, grade)
                    print(f"{student.name} has been assigned a grade of {grade} in {course_code}.")
                    return True
                else:
                    print("Invalid grade. Must be between 0 and 100.")
                    return False
            else:
                print(f"{student.name} is not enrolled in {course_code}.")
                return False
        else:
            print(f"{self.name} is not teaching {course_code}.")
            return False

    def view_student_grades(self,student,course):
        if course in self.courses_taught:
            if course in student.grades:
                print(f"Student {student.name} grades for {course}: {student.grades[course]}")
            else:
                print(f"{student.name} has no grade for {course}")
        else:
            print(f"{self.name} is not teaching {course}.")

    def get_all_courses(self):
        return self.courses_taught

    def is_student_in_course(self,student,course):
        if course in student.courses:
            return True
        else:
            return False
