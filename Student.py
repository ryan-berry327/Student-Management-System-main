from Person import Person 

class Student(Person):

    def __init__(self,name,age,id_number,grades = None,courses = None):
        super().__init__(name,age,id_number)
        self.grades = grades if grades else {} 
        self.courses = courses if courses else []

    # Adds the grade for the student and replaces current grades
    # Handles errors for cases such as grade not being integer, course not found
    # and grade not being in the boundary of 0 - 100
    def add_grade(self,course_code,grade):
        try:
            grade = int(grade)
        except ValueError:
            print("Invalid grade, must be an integer")
            return False # Handles string cases or None

        if course_code in self.courses:
            if 0 <= grade <= 100:
                self.grades[course_code] = grade
                return True
            else:
                print("Invalid grade, must be between 0 and 100")
                return False 
        else:
            print("Course not found")
            return False      
        

    # Calculates the GPA of the student
    def calculate_gpa(self):
        # If grades is empty
        if not self.grades:
            return 0
        return sum(self.grades.values()) / len(self.grades) # .values because it is a dictionary
        
    def enroll(self,course_code):
        if course_code not in self.courses:
            self.courses.append(course_code)
            print(f"{self.name} has been enrolled in {course_code}.")
        else:
            print(f"{self.name} is already enrolled in {course_code}.")

    # Displays all the info of the students
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, ID Number: {self.id_number}")
        print(f"Enrolled Courses: {self.courses}")
        print(f"GPA: {self.calculate_gpa():.2f}")


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
