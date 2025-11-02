# Student Record Management System
# Created by Nsude Thelma

students = []  # list to store student records

def add_student():
    name = input("Enter student name: ")
    student_id = input("Enter student ID: ")
    grade = input("Enter student grade: ")
    students.append({"Name": name, "ID": student_id, "Grade": grade})
    print(f" {name} added successfully!\n")

def view_students():
    if not students:
        print("No student records found.\n")
        return
    print("\n=== Student Records ===")
    for i, student in enumerate(students, start=1):
        print(f"{i}. Name: {student['Name']}, ID: {student['ID']}, Grade: {student['Grade']}")
    print()

def update_student():
    student_id = input("Enter the student ID to update: ")
    for student in students:
        if student["ID"] == student_id:
            print(f"Current Record: {student}")
            student["Name"] = input("Enter new name: ")
            student["Grade"] = input("Enter new grade: ")
            print(" Record updated successfully!\n")
            return
    print(" Student ID not found.\n")

def delete_student():
    student_id = input("Enter the student ID to delete: ")
    for student in students:
        if student["ID"] == student_id:
            students.remove(student)
            print(" Student deleted successfully!\n")
            return
    print(" Student ID not found.\n")

def main():
    while True:
        print("=== Student Record Management System ===")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            update_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            print("Exiting program... Goodbye!")
            break
        else:
            print(" Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
