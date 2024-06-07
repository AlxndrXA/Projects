import json

def load_student_list(filename):
    try:
        with open(filename) as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


student_list = load_student_list('students.json')

def save_student_list(filename, student_list):
    with open(student_list, 'w') as file:
        json.dump(filename, file, indent=4)


# STUDENTS #
def STUDENT(v):
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
    main()

# MARKS #

def MARK(v):
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
    main()

def UPDATE_GRADE():
    student_name = input("Student Name: ")
    if student_name in student_list:
        a = int(input("Grade: "))
        student_list[student_name]['Grade'] = a
    else:
        txtRed("\n Student not found.")
    save_student_list(student_list, 'students.json')
    main()
def main():
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

    command = input("\033[95m {}\033[00m" .format("Enter your choice:"))

    if command == '1':
        STUDENT(True)
    elif command == '2':
        STUDENT(False)
    elif command == '3':
        txtGreen("\n Students")
        for studentName, details in student_list.items():
            txtYellow(studentName)
            print("Grade:", details["Grade"])
            print("Marks:", details["Marks"])
            print("")
        main()
    elif command == '4':
        MARK(True)
    elif command == '5':
        MARK(False)
    elif command == '6':
        UPDATE_GRADE()
    elif command == '7':
        student_name = input("Student Name: ")
        if student_name in student_list:
            print(student_list[student_name]['Marks'])
        else:
            txtRed("\n Student not found.")
        main()
    elif command == '8':
        student_name = input("Student Name: ")
        if student_name in student_list:
            marks = student_list[student_name]['Marks']
            total_marks = len(marks)
            sum_marks = sum(marks)
            txtGreen(f"Final Score: {sum_marks / total_marks:.2f}")
        else:
            print("\n Student Not Found")
        main()

def txtGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def txtYellow(skk): print("\033[93m {}\033[00m" .format(skk))
def txtRed(skk): print("\033[91m {}\033[00m" .format(skk))


if __name__ == '__main__':
    main()
