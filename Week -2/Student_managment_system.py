import json
import os

FILE_NAME = "students.json"
class Student:
    def __init__(self, student_id, name, grade):
        self.student_id = student_id
        self.name = name
        self.grade = grade

    def to_dict(self):
        return {
            "id": self.student_id,
            "name": self.name,
            "grade": self.grade}
      
class StudentManager:
    def __init__(self):
        self.students = {}
        self.load_data()

    def load_data(self):
        if os.path.exists(FILE_NAME):
            with open(FILE_NAME, "r") as file:
                data = json.load(file)
                self.students = data
        else:
            self.students = {}

    def save_data(self):
        with open(FILE_NAME, "w") as file:
            json.dump(self.students, file, indent=4)

    def add_student(self, student):
        if student.student_id in self.students:
            print("Student ID already exists.")
            return
        self.students[student.student_id] = student.to_dict()
        self.save_data()
        print("Student added successfully.")

    def update_student(self, student_id, name, grade):
        if student_id not in self.students:
            print("Student not found.")
            return
        self.students[student_id]["name"] = name
        self.students[student_id]["grade"] = grade
        self.save_data()
        print("Student updated successfully.")
    def delete_student(self, student_id):
        if student_id not in self.students:
            print("Student not found.")
            return
        del self.students[student_id]
        self.save_data()
        print("Student deleted successfully.")
    def list_students(self):
        if not self.students:
            print("No student records found.")
            return
        print("\n--- Student Records ---")
        print(f"{'ID':<10}{'Name':<20}{'Grade'}")
        print("-" * 40)

        for sid, data in self.students.items():
            print(f"{sid:<10}{data['name']:<20}{data['grade']}")
        print("-" * 40)


def main():
    manager = StudentManager()

    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. List Students")
        print("5. Exit")

        choice = input("Enter choice (1-5): ")

        if choice == "1":
            sid = input("Enter Student ID: ")
            name = input("Enter Name: ")
            grade = input("Enter Grade: ")
            student = Student(sid, name, grade)
            manager.add_student(student)

        elif choice == "2":
            sid = input("Enter Student ID to update: ")
            name = input("Enter New Name: ")
            grade = input("Enter New Grade: ")
            manager.update_student(sid, name, grade)

        elif choice == "3":
            sid = input("Enter Student ID to delete: ")
            manager.delete_student(sid)

        elif choice == "4":
            manager.list_students()

        elif choice == "5":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()

