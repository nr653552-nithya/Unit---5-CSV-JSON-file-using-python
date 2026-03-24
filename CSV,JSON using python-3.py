import csv
import json

CSV_FILE = "students.csv"
JSON_FILE = "students.json"

def init_csv():
    try:
        with open(CSV_FILE, "r") as file:
            pass
    except FileNotFoundError:
        with open(CSV_FILE, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["name", "age", "marks", "grade"])

def add_student():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    marks = int(input("Enter marks: "))

    # Grade logic
    if marks >= 90:
        grade = "A"
    elif marks >= 75:
        grade = "B"
    elif marks >= 50:
        grade = "C"
    else:
        grade = "Fail"

    with open(CSV_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, age, marks, grade])

    print("✅ Student added!")

def read_csv():
    students = []
    try:
        with open(CSV_FILE, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                row["age"] = int(row["age"])
                row["marks"] = int(row["marks"])
                students.append(row)
    except FileNotFoundError:
        return []
    
    return students

def convert_to_json():
    students = read_csv()
    with open(JSON_FILE, "w") as file:
        json.dump(students, file, indent=4)
    print("✅ Converted to JSON!")

def view_students():
    students = read_csv()
    if not students:
        print("No data found!")
        return

    print("\n📋 Student List:")
    for s in students:
        print(s)

def average_marks():
    students = read_csv()
    if not students:
        print("No data found!")
        return

    avg = sum(s["marks"] for s in students) / len(students)
    print("📊 Average:", avg)

def topper():
    students = read_csv()
    if not students:
        print("No data found!")
        return

    top = max(students, key=lambda x: x["marks"])
    print("🏆 Topper:", top["name"], "-", top["marks"])

init_csv()

while True:
    print("\n📊 MENU")
    print("1. Add Student")
    print("2. View Students")
    print("3. Average Marks")
    print("4. Topper")
    print("5. Convert CSV → JSON")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        average_marks()
    elif choice == "4":
        topper()
    elif choice == "5":
        convert_to_json()
    elif choice == "6":
        print("👋 Exit")
        break
    else:
        print("❌ Invalid choice")
