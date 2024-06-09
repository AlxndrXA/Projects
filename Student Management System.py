import json

def load_student_list(filename):
    ## Loading the student.json file
    try:
        with open(filename) as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


student_list = load_student_list('students.json')

def save_student_list(filename, student_list):
    ## Saving the json file
    with open(student_list, 'w', encoding="utf-8") as file:
        json.dump(filename, file, indent=4)


# STUDENTS #
def student(v):
    student_name = input("Student Name: ")

    if v:
        student_list[student_name] = {}
        student_list[student_name]['Grade'] = 1
        student_list[student_name]['Marks'] = []
    else:
        if student_name in student_list:
            del student_list[student_name]
        else:
            txtRed("\n Student not found.")

    save_student_list(student_list, 'students.json')

# MARKS #

def mark(v):
    student_name = input("Student Name: ")

    if student_name in student_list:
        if v:
            grade = int(input("Mark: "))
            student_list[student_name]['Marks'].append(grade)
        else:
            grade = int(input("Mark: "))
            student_list[student_name]['Marks'].remove(grade)
    else:
        txtRed("\nStudent not found.")
    save_student_list(student_list, 'students.json')

def update_grade():
    student_name = input("Student Name: ")
    if student_name in student_list:
        a = int(input("Grade: "))
        student_list[student_name]['Grade'] = a
    else:
        txtRed("\n Student not found.")
    save_student_list(student_list, 'students.json')
def main():
    while True:
        txtGreen("\n  Student Management System")
        print("[1] Add Student")
        print("[2] Remove Student")
        print("[3] List Students")
        txtYellow("\n  Options")
        print("[4] Add Mark")
        print("[5] Remove Mark")
        print("\n[6] Update Grade")
        print("[7] List Marks of a student")
        print("[8] Calculate Final Score")
        print("[0] Exit")

        command = input("\033[95m {}\033[00m".format("Enter your choice:"))

        if command == '1':
            student(True)
        elif command == '2':
            student(False)
        elif command == '3':
            txtGreen("\n Students")
            for studentName, details in student_list.items():
                txtYellow(studentName)
                print("Grade:", details["Grade"])
                print("Marks:", details["Marks"])
                print("")
        elif command == '4':
            mark(True)
        elif command == '5':
            mark(False)
        elif command == '6':
            update_grade()
        elif command == '7':
            student_name = input("Student Name: ")
            if student_name in student_list:
                print(student_list[student_name]['Marks'])
            else:
                txtRed("\n Student not found.")
        elif command == '8':
            student_name = input("Student Name: ")
            if student_name in student_list:
                marks = student_list[student_name]['Marks']
                total_marks = len(marks)
                sum_marks = sum(marks)
                txtGreen(f"Final Score: {sum_marks / total_marks:.2f}")
            else:
                print("\n Student Not Found")
        elif command == '0':
            break
        else:
            txtRed("\n Invalid input")

def txtGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def txtYellow(skk): print("\033[93m {}\033[00m" .format(skk))
def txtRed(skk): print("\033[91m {}\033[00m" .format(skk))


if __name__ == '__main__':
    main()
