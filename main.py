from managers.student_manager import StudentManager
from models.student import Student, GraduateStudent
from utils.validation import (
    is_valid_id, is_valid_name, is_valid_department,
    is_valid_marks, is_valid_thesis, is_valid_choice
)




def main():
    manager = StudentManager()

    while True:
        print("Welcome to Student Performance Tracker")
        print("1. Add Student \n2. Remove Student \n3. Add Scores \n4. List All Students \n5. Top Scorer in Subject \n6. Department Average \n7. Exit")
        choice = input("Enter the choice ") #don't make it (int)
        if not is_valid_choice(choice, [1, 2, 3, 4, 5, 6, 7]):
            print("Invalid choice. Please enter a number between 1 and 7.")

            #have to make the choices in between doble quotes cause it is a string
        
        if choice == "1":
            student_type = input("Type (student/graduate): ").strip().lower()
            id = input("ID: ")
            name = input("Name: ")
            dept = input("Department: ")

            if not is_valid_id(id) or not is_valid_name(name) or not is_valid_department(dept):
                print("Invalid entries. Please try again.")
                continue


            if student_type.lower() == "graduate":
                thesis = input("Thesis Title: ")
                student = GraduateStudent(id, name, dept, thesis)
            else:
                student = Student(id, name, dept)

            manager.add_student(student)

        elif choice == "2":
            id = input("Enter the ID of the Student to be removed: ")
            if not is_valid_id(id):
                print("Invalid ID entry")
            manager.remove_student(id)

        elif choice == "3":
            nm = input("Enter the Name for the student whose marks you want to enter: ")
            print("Enter subjects and marks (type 'X' to finish):")
            student = manager.find_student_by_name(nm)
            while True:
                subject = input("Subject: ")
                if subject.upper() == 'X':
                    break
                marks = float(input(f"Marks for {subject}: "))
                student.add_score(subject, marks)

        elif choice == "4":
            for student in manager.list_students():
                    print(student)


        elif choice == "5":
            sub = input("Enter the subject for checking the top scorer: ")
            manager.get_top_scorer(sub)

        elif choice == "6":
            dept = input("Enter the department for the average calculation: ")
            manager.get_department_average(dept)

        elif choice == "7":
            exit()


if __name__ == "__main__":
    main()
