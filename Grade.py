from Student import Student
from Course import Course

class Grade:
    def __init__(self, student,course,grade,letter_grade):
        self.student = student
        self.course = course
        self.grade = grade
        self.letter_grade = letter_grade

    def calculate_letter_grade(self):
        if 90 <= self.grade <= 100:
            self.letter_grade = 'A'
        elif 80 <= self.grade <= 89:
            self.letter_grade = 'B'
        elif 70 <= self.grade <= 79:
            self.letter_grade = 'C'
        elif 60 <= self.grade <= 69:
            self.letter_grade = 'D'
        elif self.grade < 60:
            self.letter_grade = 'F'
        
        return self.letter_grade 

    def update_grade(self,new_grade):
        if  0 <= new_grade <= 100:
            self.grade = new_grade
            self.calculate_letter_grade()
            return True
        else:
            print("Invalid grade, please put a grade between 0 to 100.")
            return False 
        
    def get_grade_info(self):
        return f"Student: {self.student.name}, Course: {self.course.course_name}, Grade: {self.grade}, Letter Grade: {self.calculate_letter_grade()}"

    def is_passing(self):
        if self.grade >= 60:
            print("This grade is passing.")
            return True
        else:
            print("This grade is failing.")
            return False
    