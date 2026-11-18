
class Requisition:
    requisition_counter = 10000

    def __init__(self, date, staff_id, staff_name):
        Requisition.requisition_counter = Requisition.requisition_counter + 1

        self.requisition_id = Requisition.requisition_counter
        self.date = date
        self.staff_id = staff_id
        self.staff_name = staff_name
        self.items = []
        self.total = 0.0
        self.status = "Pending"
        self.approval_reference = "Not available"

    def add_requisition(self, items):
        self.items = items
        self.total = 0

        for item in self.items:
            self.total = self.total + item["price"]

        if self.total < 500:
            self.status = "Approved"
            self.approval_reference = (
                self.staff_id + str(self.requisition_id)[-3:]
            )

    def respond_to_requisition(self, decision):
        if self.status == "Pending":
            if decision == "1":
                self.status = "Approved"
                self.approval_reference = (
                    self.staff_id + str(self.requisition_id)[-3:]
                )
                print("Requisition approved.")

            elif decision == "2":
                self.status = "Not approved"
                print("Requisition not approved.")

            else:
                print("Invalid choice. Please enter 1 or 2.")

        else:
            print("This requisition has already been processed.")

    def display_requisition(self):
        print("\n------------------------------")
        print("Requisition Details")
        print("------------------------------")
        print("Requisition ID:", self.requisition_id)
        print("Date:", self.date)
        print("Staff ID:", self.staff_id)
        print("Staff Name:", self.staff_name)

        print("\nItems:")
        for item in self.items:
            print(item["name"], "- $", format(item["price"], ".2f"))

        print("Total: $", format(self.total, ".2f"))
        print("Status:", self.status)
        print("Approval Reference:", self.approval_reference)
        print("------------------------------")


class RequisitionManagement:

    def __init__(self):
        self.requisitionlist = []

    def submit_requisition(self):
        print("\nSubmit a New Requisition")

        date = input("Enter Date (DD-MM-YYYY): ")

        while (
            len(date) != 10
            or date[2] != "-"
            or date[5] != "-"
            or not (date[:2] + date[3:5] + date[6:]).isdigit()
        ):
            print("Please enter the date in DD-MM-YYYY format.")
            date = input("Enter Date (DD-MM-YYYY): ")

        staff_id = input("Enter Staff ID: ")

        while not staff_id.isdigit() or len(staff_id) < 2:
            print("Invalid Staff ID. Please enter a numeric ID.")
            staff_id = input("Enter Staff ID: ")

        staff_name = input("Enter Staff Name: ")

        while (
            staff_name.strip() == ""
            or not staff_name.replace(" ", "").isalpha()
        ):
            print("Please enter a valid staff name.")
            staff_name = input("Enter Staff Name: ")

        requisition = Requisition(date, staff_id, staff_name)

        items = []

        while True:
            item_name = input("Enter Item Name: ")

            while item_name.strip() == "":
                print("Item name cannot be empty.")
                item_name = input("Enter Item Name: ")

            item_price = input("Enter Item Price: ")

            while not item_price.replace(".", "", 1).isdigit():
                print("Please enter a valid price.")
                item_price = input("Enter Item Price: ")

            item_price = float(item_price)

            while item_price <= 0:
                print("Price should be greater than zero.")
                item_price = input("Enter Item Price: ")

                while not item_price.replace(".", "", 1).isdigit():
                    print("Please enter a valid price.")
                    item_price = input("Enter Item Price: ")

                item_price = float(item_price)

            item = {
                "name": item_name,
                "price": item_price
            }

            items.append(item)

            choice = input("Add another item? (yes/no): ")

            if choice.lower() != "yes":
                break

        requisition.add_requisition(items)
        self.requisitionlist.append(requisition)

        print("\nRequisition submitted successfully.")
        print("Your Requisition ID is:", requisition.requisition_id)
        print("Requisition Status:", requisition.status)

    def display_requisitions(self):
        if len(self.requisitionlist) == 0:
            print("\nNo requisitions available.")

        else:
            for requisition in self.requisitionlist:
                requisition.display_requisition()

    def manager_approval(self):
        print("\nManager Approval")

        requisition_id = input("Enter Requisition ID: ")

        while not requisition_id.isdigit():
            print("Please enter a numeric Requisition ID.")
            requisition_id = input("Enter Requisition ID: ")

        requisition_id = int(requisition_id)

        for requisition in self.requisitionlist:

            if requisition.requisition_id == requisition_id:

                if requisition.status != "Pending":
                    print("This requisition has already been processed.")
                    return

                print("\n1. Approve")
                print("2. Not Approve")

                choice = input("Enter your choice: ")

                while choice != "1" and choice != "2":
                    print("Please enter 1 or 2.")
                    choice = input("Enter your choice: ")

                requisition.respond_to_requisition(choice)
                return

        print("Requisition ID not found.")

    def display_statistics(self):
        approved = 0
        pending = 0
        not_approved = 0

        for requisition in self.requisitionlist:

            if requisition.status == "Approved":
                approved = approved + 1

            elif requisition.status == "Pending":
                pending = pending + 1

            elif requisition.status == "Not approved":
                not_approved = not_approved + 1

        print("\n------------------------------")
        print("Requisition Statistics")
        print("------------------------------")
        print("Total Requisitions:", len(self.requisitionlist))
        print("Approved:", approved)
        print("Pending:", pending)
        print("Not Approved:", not_approved)
        print("------------------------------")

    def menu_system(self):

        while True:
            print("\n==============================")
            print("Requisition Management System")
            print("==============================")
            print("1. Submit a Requisition")
            print("2. Display All Requisitions")
            print("3. Manager Approval")
            print("4. Display Statistics")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.submit_requisition()

            elif choice == "2":
                self.display_requisitions()

            elif choice == "3":
                self.manager_approval()

            elif choice == "4":
                self.display_statistics()

            elif choice == "5":
                print("Thank you for using the system.")
                break

            else:
                print("Invalid choice. Please enter a number from 1 to 5.")


# Start the program

pro = RequisitionManagement()
pro.menu_system()
