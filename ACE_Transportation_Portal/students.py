# students.py
# Student Registration Management

class Student:
    def __init__(self, student_id, name, pass_type, route_number):
        self.student_id = student_id
        self.name = name
        self.pass_type = pass_type  # "Monthly" or "Semester"
        self.route_number = route_number
        self.is_active = True
    
    def display_info(self):
        print("\n=== Student Information ===")
        print(f"Student ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Pass Type: {self.pass_type}")
        print(f"Route Number: {self.route_number}")
        print(f"Active: {'Yes' if self.is_active else 'No'}")
        print("-" * 30)
    
    def deactivate(self):
        self.is_active = False
        print(f"✓ Student {self.student_id} deactivated!")


class StudentManager:
    def __init__(self):
        self.students = []  # List of Student objects
    
    def add_student(self, student):
        self.students.append(student)
        print(f"✓ Student {student.student_id} registered successfully!")
    
    def find_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None
    
    def display_all_students(self):
        if not self.students:
            print("No students registered!")
            return
        print("\n=== All Registered Students ===")
        count = 1
        for student in self.students:
            print(f"\nStudent #{count}:")
            student.display_info()
            count = count + 1