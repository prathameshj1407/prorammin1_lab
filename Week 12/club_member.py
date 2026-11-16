class ClubRegistration:
    def __init__(self):
        self.student_info = {}
        self.num_withdrawn = 0
        self.mem_id = 10001

    def register(self):
        student_id = input("Enter student ID: ")
        last_name = input("Enter last name: ")
        programme = input("Enter your programme (Diploma/Bachelor): ")
        membership_id = "AB" + str(self.mem_id)
        self.mem_id = self.mem_id + 1

        self.student_info[membership_id] = {
            "student_id": student_id,
            "last name": last_name,
            "programme": programme
        }
        print("Successfully registered", membership_id)

    def withdraw(self):
        memberid = input("Enter your membership ID for withdraw: ")
        lname = input("Enter your last name: ")

        if memberid in self.student_info:
            if self.student_info[memberid]["last name"] == lname:
                del self.student_info[memberid]
                print("Withdrawn successfully", memberid)
                self.num_withdrawn = self.num_withdrawn + 1
            else:
                print("Incorrect last name - Access Denied")
        else:
            print("Incorrect membership ID")

    def display(self):
        for k, v in self.student_info.items():
            print("ID: ", k)
            print("Student ID: ", v["student_id"])
            print("Last Name: ", v["last name"])
            print("Programme: ", v["programme"])

    def summary(self):
        diploma = 0
        bachelor = 0

        for student in self.student_info.values():
            if student["programme"] == "Diploma":
                diploma = diploma +  1
            else:
                bachelor = bachelor + 1

        print("Number Diploma: ", diploma)
        print("Number of Bachelor: ", bachelor)
        print("Total registered", len(self.student_info))

    def menu(self):
        while True:
            print("Club membership system")
            print("1: Registration")
            print("2: Withdraw")
            print("3: Display")
            print("4: Summary")
            print("5: Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.register()
            elif choice == "2":
                self.withdraw()
            elif choice == "3":
                self.display()
            elif choice == "4":
                self.summary()
            else:
                break

club = ClubRegistration()
club.menu()