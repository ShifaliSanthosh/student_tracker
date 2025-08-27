def is_valid_id(student_id: str) -> bool:
    return student_id.strip() != "" and student_id.isalnum() #to check if it's not blank and that it is numbers & letters

def is_valid_name(name: str) -> bool:
    return name.strip() != "" and all(x.isalpha() or x.isspace() for x in name) #alphabetical & no space

def is_valid_department(dept: str) -> bool:
    return dept.strip() != ""

def is_valid_marks(marks: str) -> bool:
    try:
        value = float(marks)
        return 0 <= value <= 100
    except ValueError:
        return False

def is_valid_thesis(thesis: str) -> bool:
    return thesis.strip() != ""

def is_valid_choice(choice: str, options: list) -> bool:
    return choice.isdigit() and int(choice) in options
