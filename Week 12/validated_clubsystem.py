
class ClubRegistration:
    def __init__(self):
        self.student_info = {}
        self.num_withdrawn = 0
        self.mem_id = 10001

    def register(self):
        while True:
            student_id = input("Enter student ID (4 digits): ").strip()

            if student_id == "":
                print("Student ID cannot be empty.")
            elif not student_id.isdigit():
                print("Student ID must contain numbers only.")
            elif len(student_id) != 4:
                print("Student ID must be exactly 4 digits.")
            else:
                duplicate = False

                for member in self.student_info.values():
                    if member["student_id"] == student_id:
                        duplicate = True
                        break

                if duplicate:
                    print("Student ID already exists.")
                else:
                    break

        while True:
            last_name = input("Enter last name: ").strip()

            if last_name == "":
                print("Last name cannot be empty.")
            elif not last_name.isalpha():
                print("Last name must contain letters only.")
            else:
                last_name = last_name.title()
                break

        while True:
            programme = input(
                "Enter programme (Diploma/Bachelor): "
            ).strip().title()

            if programme == "Diploma" or programme == "Bachelor":
                break
            else:
                print(
                    "Invalid programme. Please enter Diploma or Bachelor."
                )

        membership_id = "AB" + str(self.mem_id)
        self.mem_id = self.mem_id + 1

        self.student_info[membership_id] = {
            "student_id": student_id,
            "last name": last_name,
            "programme": programme
        }

        print("Successfully registered!")
        print("Membership ID:", membership_id)

    def withdraw(self):
        while True:
            memberid = input(
                "Enter membership ID for withdrawal: "
            ).strip().upper()

            if memberid == "":
                print("Membership ID cannot be empty.")
            elif not memberid.isalnum():
                print("Membership ID must contain letters and numbers only.")
            elif memberid not in self.student_info:
                print("Membership ID not found.")
            else:
                break

        lname = input("Enter your last name: ").strip().title()

        if self.student_info[memberid]["last name"] == lname:
            del self.student_info[memberid]
            print("Withdrawn successfully:", memberid)
            self.num_withdrawn = self.num_withdrawn + 1
        else:
            print("Incorrect last name - Access Denied.")

    def display(self):
        if len(self.student_info) == 0:
            print("There are no registered members.")
        else:
            print("\n--- Current Club Members ---")

            for membership_id, member in self.student_info.items():
                print("Membership ID:", membership_id)
                print("Student ID:", member["student_id"])
                print("Last Name:", member["last name"])
                print("Programme:", member["programme"])
                print("---------------------------")

    def summary(self):
        diploma = 0
        bachelor = 0

        for student in self.student_info.values():
            if student["programme"] == "Diploma":
                diploma = diploma + 1
            elif student["programme"] == "Bachelor":
                bachelor = bachelor + 1

        print("\n--- Membership Summary ---")
        print("Number of Diploma members:", diploma)
        print("Number of Bachelor members:", bachelor)
        print("Total currently registered:", len(self.student_info))
        print("Total withdrawn:", self.num_withdrawn)

    def search_member(self):
        search_id = input(
            "Enter student ID or membership ID: "
        ).strip().upper()

        if search_id == "":
            print("Search ID cannot be empty.")
            return

        found = False

        for membership_id, member in self.student_info.items():
            if (
                member["student_id"] == search_id
                or membership_id == search_id
            ):
                print("\n--- Member Found ---")
                print("Student ID:", member["student_id"])
                print("Last Name:", member["last name"])
                print("Programme:", member["programme"])
                print("Membership ID:", membership_id)
                found = True
                break

        if not found:
            print("Member not found.")

    # Main menu
    def menu(self):
        while True:
            print("\n===== CLUB MENU =====")
            print("1. Register Member")
            print("2. Withdraw Member")
            print("3. Display Members")
            print("4. Display Summary")
            print("5. Search Member")
            print("6. Exit")

            choice = input("Choose option: ").strip()

            if choice == "1":
                self.register()
            elif choice == "2":
                self.withdraw()
            elif choice == "3":
                self.display()
            elif choice == "4":
                self.summary()
            elif choice == "5":
                self.search_member()
            elif choice == "6":
                print("Thank you for using the Club Membership System.")
                break
            else:
                print("Invalid choice. Please select 1 to 6.")


club = ClubRegistration()
club.menu()
