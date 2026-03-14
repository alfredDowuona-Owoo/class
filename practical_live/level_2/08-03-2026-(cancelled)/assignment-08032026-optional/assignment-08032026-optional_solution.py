import csv
import os

class Student:
    def __init__(self, student_id, name, email, address, student_class, is_current, phone, remarks):
        self.student_id = student_id
        self.name = name
        self.email = email
        self.address = address
        self.student_class = student_class
        self.is_current = is_current
        self.phone = phone
        self.remarks = remarks

    def to_dict(self):
        """Converts object data to a dictionary for CSV writing."""
        return {
            "ID": self.student_id,
            "Name": self.name,
            "Email": self.email,
            "Address": self.address,
            "Class": self.student_class,
            "Is_Current": self.is_current,
            "Phone": self.phone,
            "Remarks": self.remarks
        }

class SchoolSystem:
    def __init__(self, filename="students.csv"):
        self.filename = filename
        self.headers = ["ID", "Name", "Email", "Address", "Class", "Is_Current", "Phone", "Remarks"]
        self._initialize_csv()

    def _initialize_csv(self):
        """Creates the CSV file with headers if it doesn't exist."""
        if not os.path.exists(self.filename):
            with open(self.filename, 'w', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=self.headers)
                writer.writeheader()

    def get_new_id(self):
        """Reads the file to find the highest ID and increments it."""
        max_id = 1000
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    max_id = max(max_id, int(row['ID']))
        return max_id + 1

    def add_student(self):
        email = input("Enter Email: ")
        
        # Check if email exists
        with open(self.filename, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row['Email'] == email:
                    print(f"\n! Student Email already exists! Student ID: {row['ID']}")
                    return

        # If not exists, take other inputs
        name = input("Enter Name: ")
        address = input("Enter Address: ")
        s_class = input("Enter Class: ")
        phone = input("Enter Phone: ")
        remarks = input("Enter Remarks: ")
        
        new_id = self.get_new_id()
        new_student = Student(new_id, name, email, address, s_class, True, phone, remarks)

        with open(self.filename, 'a', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=self.headers)
            writer.writerow(new_student.to_dict())
        
        print(f"\n✔ Student Inserted Successfully! ID: {new_id}")

    def lookup_current_by_id(self):
        search_id = input("Enter Student ID: ")
        found = False
        with open(self.filename, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row['ID'] == search_id and row['Is_Current'] == 'True':
                    print(f"\n--- Current Record for ID {search_id} ---")
                    print(row)
                    found = True
        if not found: print("No active record found.")

    def view_remarks_history(self):
        search_id = input("Enter Student ID for History: ")
        print(f"\n{'ID':<6} | {'Class':<6} | {'Remarks'}")
        print("-" * 30)
        with open(self.filename, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row['ID'] == search_id:
                    print(f"{row['ID']:<6} | {row['Class']:<6} | {row['Remarks']}")

    def view_class_roster(self):
        target_class = input("Enter Class to view: ")
        print(f"\n--- Current Students in Class {target_class} ---")
        with open(self.filename, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row['Class'] == target_class and row['Is_Current'] == 'True':
                    print(f"ID: {row['ID']} | Name: {row['Name']}")

# --- Main Execution ---
school = SchoolSystem()

while True:
    print("\n==== SCHOOL MANAGEMENT SYSTEM ====")
    print("1. Add New Student")
    print("2. Lookup Student (Current Class)")
    print("3. View Student Remarks History")
    print("4. View Class Roster")
    print("5. Exit")
    
    choice = input("\nSelect an option (1-5): ")

    if choice == '1':
        school.add_student()
    elif choice == '2':
        school.lookup_current_by_id()
    elif choice == '3':
        school.view_remarks_history()
    elif choice == '4':
        school.view_class_roster()
    elif choice == '5':
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice, please try again.")