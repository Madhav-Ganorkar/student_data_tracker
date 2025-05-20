student_records = []
def add_student():
    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")
    marks = []
    
    for i in range(1, 4):
        try:
            mark = float(input(f"Enter marks for subject {i}: "))
            marks.append(mark)
        except ValueError:
            print("❌ Please enter a valid number!")
            return

    student = {
        "Name": name,
        "Roll No": roll_no,
        "Subject1": marks[0],
        "Subject2": marks[1],
        "Subject3": marks[2]
    }

    student_records.append(student)
    print("✅ Student added successfully!\n")

def display_records():
    if not student_records:
        print("⚠️ No student records found!\n")
        return

    print("========== All Student Records ==========")
    for student in student_records:
        print(f"Name      : {student['Name']}")
        print(f"Roll No   : {student['Roll No']}")
        print(f"Subject 1 : {student['Subject1']}")
        print(f"Subject 2 : {student['Subject2']}")
        print(f"Subject 3 : {student['Subject3']}")
        print("-" * 40)

def calculate_average():
    if not student_records:
        print("⚠️ No student records found!\n")
        return

    print("========== Student Averages ==========")
    for student in student_records:
        total = student['Subject1'] + student['Subject2'] + student['Subject3']
        avg = total / 3
        print(f"{student['Name']} (Roll No: {student['Roll No']}) - Average Marks: {avg:.2f}")
    print("-" * 40)

import csv  # File ke start mein (top) ye line add karna na bhoolna

def save_to_csv():
    if not student_records:
        print("⚠️ No student records to save!\n")
        return

    filename = "student_records.csv"
    try:
        with open(filename, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["Name", "Roll No", "Subject1", "Subject2", "Subject3"])
            writer.writeheader()
            writer.writerows(student_records)
        print(f"✅ Records saved successfully to {filename}\n")
    except Exception as e:
        print(f"❌ Error while saving file: {e}")


def main():
    while True:
        print("========= Student Data Tracker =========")
        print("1. Add Student")
        print("2. Display All Records")
        print("3. Calculate Average Marks")
        print("4. Save Records to CSV")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            display_records()
        elif choice == '3':
            calculate_average()
        elif choice == '4':
            save_to_csv()
        elif choice == '5':
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("You selected option:", choice)
            print()

if __name__ == "__main__":
    main()



