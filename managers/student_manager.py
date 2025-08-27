

class StudentManager:

    def __init__(self):
        self.students = [] #for list of students

    def add_student(self, student):
        self.students.append(student)
        print(f"Added the student of ID: {student.id}")
    
    def remove_student(self, id):
        for s in self.students:
            if s.id == id:
                self.students.remove(s)
                print(f"Removed student with ID {s.id}")
        return f"ID NOT FOUND"


    def find_student_by_name(self, name):
        for s in self.students:
            if s.name.lower() == name.lower(): #to avoid any mismatch - python is case sensitive
                return s

    def list_students(self):
        return self.students # this automatically calls student.__str__()

    def get_top_scorer(self, subject):
        top_student = None
        top_score = -1
        for s in self.students:
            if subject in s.scores:
                if s.scores[subject] > top_score: #s.scores for one student since for loop
                    top_score = s.scores[subject]
                    top_student = s
        return top_student

    def get_department_average(self, dept):
        dept_students = []
        for s in self.students:
            if s.dept.lower() == dept.lower():
                dept_students.append(s) 
        if not dept_students:
            return 0.0
        for s in dept_students:
            total = sum(s.get_average_score()) #to easen the student based work-check 
            return total / len(dept_students)