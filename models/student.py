class Student:
    def __init__(self, id: str, name: str, dept: str, scores = None):
        self.id = id
        self.name = name
        self.dept = dept
        self.scores = scores if scores is not None else {} #dictionary created for a single student but has all subjects + marks of that one student


    def add_score(self, subject: str, marks: float): #subject = key; marks = value
        self.scores[subject] = marks

    def get_average_score(self) -> float:
        return sum(self.scores.values()) / len(self.scores) 
    
    # self.scores means all enteries (all subjects & respective marks) of the /one/ student in the dictionary
    # and so se=lf.scores.values() means - all marks!
    # subject & marks are column names given by user// as per syntax it is still keys & values

    def __str__(self):
        if self.scores:
            avg_score = self.get_average_score()
            score_info = f"Average Score: {avg_score:.2f}"
        else:
            score_info = "No scores added yet."

        return (f"Student ID: {self.id}\n"
                f"Name: {self.name}\n"
                f"Department: {self.dept}\n"
                f"{score_info}")

    
class GraduateStudent(Student):
    def __init__(self, id, name, dept, thesis_title):
        super().__init__(id, name, dept)
        self.thesis_title = thesis_title
        
    def __str__(self):
        std = super().__str__()
        return f"{std}\n Thesis Title: {self.thesis_title}"

    