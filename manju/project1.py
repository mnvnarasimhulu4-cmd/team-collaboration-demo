FILE_NAME = "s.txt"

ADMIN_USERNAME = "aanand"
ADMIN_PASSWORD = "aanand630037"

class Student:
    def __init__(self, roll, name, marks):
        self.roll = roll
        self.name = name
        self.marks = marks
        self.total = sum(marks)
        self.percent = self.total / len(marks)

    def to_string(self):
        marks_str = ",".join(map(str, self.marks))
        return f"{self.roll}|{self.name}|{marks_str}\n"

    @staticmethod
    def from_string(line):
        parts = line.strip().split("|")
        roll = parts[0]
        name = parts[1]
        marks = list(map(int, parts[2].split(",")))
        return Student(roll, name, marks)

    def display(self):
        print(f"Roll: {self.roll}, Name: {self.name}, Total: {self.total}, Percentage: {self.percent:.2f}")


class StudentManager:
    def __init__(self):
        self.students = []
        self.load_data()

    def load_data(self):
        try:
            file = open(FILE_NAME, "r")
            for line in file.readlines():
                student = Student.from_string(line)
                self.students.append(student)
            file.close()
        except FileNotFoundError:
            pass

    def save_data(self):
        file = open(FILE_NAME, "w")
        for s in self.students:
            file.write(s.to_string())
        file.close()

    def add_student(self):
        roll = input("Enter Roll Number: ")
        name = input("Enter Name: ")
        marks = []
        for i in range(3):
            m = int(input(f"Enter Marks for Subject {i+1}: "))
            marks.append(m)

        student = Student(roll, name, marks)
        self.students.append(student)
        self.save_data()
        print("Student record added successfully.")

    def view_all(self):
        if not self.students:
            print("No records found.")
            return

        print("\n--- All Student Records ---")
        for s in self.students:
            s.display()

    def search_student(self):
        roll = input("Enter Roll Number: ")
        for s in self.students:
            if s.roll == roll:
                print("Record Found:")
                s.display()
                return
        print("Record not found.")

    def search_by_name(self):
        name = input("Enter Name to Search: ").lower()
        found = False
        for s in self.students:
            if s.name.lower() == name:
                s.display()
                found = True
        if not found:
            print("No record found with that name.")

    def update_marks(self):
        roll = input("Enter Roll Number: ")
        for s in self.students:
            if s.roll == roll:
                marks = []
                for i in range(3):
                    m = int(input(f"Enter New Marks for Subject {i+1}: "))
                    marks.append(m)

                s.marks = marks
                s.total = sum(marks)
                s.percent = s.total / 3

                self.save_data()
                print("Marks updated successfully.")
                return

        print("Record not found.")

    def delete_student(self):
        roll = input("Enter Roll Number to Delete: ")
        for i, s in enumerate(self.students):
            if s.roll == roll:
                print(f"Student Found: {s.name}")
                confirm = input("Confirm Delete? (yes/no): ").lower()
                if confirm == "yes":
                    self.students.pop(i)
                    self.save_data()
                    print("Record deleted successfully.")
                else:
                    print("Deletion cancelled.")
                return
        print("Record not found.")

    def sort_by_percentage(self):
        if not self.students:
            print("No records found.")
            return
        sorted_students = sorted(self.students, key=lambda x: x.percent, reverse=True)
        print("\n--- Sorted by Percentage (High to Low) ---")
        for s in sorted_students:
            s.display()

    def highest_lowest(self):
        if not self.students:
            print("No records found.")
            return
        highest = max(self.students, key=lambda x: x.percent)
        lowest = min(self.students, key=lambda x: x.percent)
        print("\nHighest Scorer:")
        highest.display()
        print("\nLowest Scorer:")
        lowest.display()

    def show_rank_list(self):
        if not self.students:
            print("No records found.")
            return
        ranked = sorted(self.students, key=lambda s: s.percent, reverse=True)
        print("\n--- Rank List ---")
        for i, s in enumerate(ranked, start=1):
            print(f"Rank {i}: {s.name} | {s.percent:.2f}%")
    def admin_login(self):
        print("\n===== Admin Login =====")
        for i in range(3):
            u = input("Enter Username: ")
            p = input("Enter Password: ")
            if u == ADMIN_USERNAME and p == ADMIN_PASSWORD:
                print("Login Successful.")
                return True
            print("Incorrect! Try again.")
        print("Too many attempts! System Locked.")
        return False
    def menu (self):
        if not self.admin_login():
            return
        while True:
            print("\n======= student result management =======")
            print("1. Add student")
            print("2. view all records")
            print("3. search by roll")
            print("4. update marks")
            print("5. delete student")
            print("6. sort by percentage")
            print("7. Highest and Lowest scorrer")
            print("8. search by name")
            print("9. Rank list")
            print("10. exit")
            
            choice =input("Enter your choice : ")
        
            if choice == '1':
                self.add_student()
            elif choice == '2':
                self.view_all()
            elif choice == '3':
                self.search_student()
            elif choice == '4':
                self.update_marks()
            elif choice == '5':
                self.delete_student()
            elif choice == '6':
                self.sort_by_percentage()
            elif choice == '7':
                self.highest_lowest()
            elif choice == '8':
                self.search_by_name()
            elif choice == '9':
                self.show_rank_list()
            elif choice == '10':
                print("Program exiting")
                break
            else:
                print("please enter valid inputs")
manager = StudentManager()
manager.menu()
