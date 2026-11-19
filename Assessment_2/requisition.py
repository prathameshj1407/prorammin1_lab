
# Requisition Class
class Requisition:

    # Shared class attribute
    requisition_counter = 10000

    def __init__(self, date, staff_id, staff_name):

        Requisition.requisition_counter += 1

        self.requisition_id = Requisition.requisition_counter

        self.date = date
        self.staff_id = staff_id
        self.staff_name = staff_name

        self.items = []
        self.total = 0.0

        self.status = "Pending"
        self.approval_reference = "Not available"

    # Add Requisition Items
    def add_requisition(self, items):

        self.items = items

        total = 0.0

        for item in self.items:
            total = total + item["price"]

        self.total = total

        self.approve_requisition()

        return self.total

    # Automatic Approval
    def approve_requisition(self):

        if self.total < 500:

            self.status = "Approved"

            self.approval_reference = (
                self.staff_id + str(self.requisition_id)[-3:]
            )

        else:

            self.status = "Pending"
            self.approval_reference = "Not available"

        return self.status

    # Manager Response
    def respond_to_requisition(self, decision):

        if self.status != "Pending":

            print("This requisition does not require manager approval.")
            return

        if decision == "1":

            self.status = "Approved"

            self.approval_reference = (
                self.staff_id + str(self.requisition_id)[-3:]
            )

            print("Requisition approved successfully.")

        elif decision == "2":

            self.status = "Not approved"
            self.approval_reference = "Not available"

            print("Requisition not approved.")

        else:

            print("Please enter a valid choice.")

    # Display One Requisition
    def display_requisition(self):

        print("\n--------------- Requisition Details ---------------")

        print("Date:", self.date)
        print("Requisition ID:", self.requisition_id)
        print("Staff ID:", self.staff_id)
        print("Staff Name:", self.staff_name)

        print("\nRequisition Items:")

        for item in self.items:

            print("Item Name:", item["name"])
            print("Item Price: $", item["price"])

        print("Total: $", format(self.total, ".2f"))
        print("Status:", self.status)
        print("Approval Reference Number:", self.approval_reference)

        print("----------------------------------------------------")


# Requisition Management Class
class RequisitionManagement:

    def __init__(self):

        self.requisitionlist = []

    # Submit New Requisition
    def submit_requisition(self):

        date = input("Enter Date: ")
        while not (len(date) == 10 and date[2] == "-" and date[5] == "-" and date[0:2].isdigit()
                   and date[3:5].isdigit() and date[6:10].isdigit()):
            print("Date cannot be empty and Date should be in the format DD-MM-YYYY.")
            date = input("Enter Date: ")

        staff_id = input("Enter Staff ID: ")
        while staff_id == "" or len(staff_id) < 2 or not staff_id.isdigit():
            print("Invalid Staff ID, Please Enter Valid ID.")
            staff_id = input("Enter Staff ID: ")

        staff_name = input("Enter Staff Name: ")
        while staff_name == "":
            print("Staff Name cannot be empty, Please write your Name.")
            staff_name = input("Enter Staff Name: ")

        requisition = Requisition(date, staff_id, staff_name)

        items = []

        while True:

            item_name = input("Enter Item Name: ")
            while item_name == "":
                print("Item Name cannot be empty, Please write an Item Name.")
                item_name = input("Enter Item Name: ")

            item_price = float(input("Enter Item Price: "))
            while item_price <= 0:
                print("price should be greater than Zero.")
                item_price = float(input("Enter Item Price: "))

            item = {
                "name": item_name,
                "price": item_price
            }

            items.append(item)

            choice = input("Add another item (yes/no): ")

            if choice.lower() != "yes":
                break

        requisition.add_requisition(items)

        self.requisitionlist.append(requisition)

        print("\nRequisition submitted successfully.")

        print("Requisition ID:", requisition.requisition_id)
        print("Total: $", format(requisition.total, ".2f"))
        print("Status:", requisition.status)
        print("Approval Reference:", requisition.approval_reference)

    # Display All Requisitions
    def display_requisitions(self):

        if len(self.requisitionlist) == 0:

            print("No requisitions submitted.")
            return

        for requisition in self.requisitionlist:

            requisition.display_requisition()

    # Manager Approval
    def manager_approval(self):

        requisition_id = input("Enter Requisition ID for manager approval: ")
        while not requisition_id.isdigit():
            print("Invalid ID, Please Enter valid ID.")
            requisition_id = input("Enter Requisition ID for manager approval: ")
        requisition_id = int(requisition_id)

        for requisition in self.requisitionlist:

            if requisition.requisition_id == requisition_id:

                print("\n1. Approve Requisition")
                print("2. Not Approve Requisition")

                choice = input("Enter your choice: ")
                while choice != "1" and choice != "2":
                    print("please Enter 1 or 2 as a valid choice.")
                    choice = input("Enter your choice: ")

                requisition.respond_to_requisition(choice)

                return

        print("Requisition ID not found.")

    # Display Requisition Statistics
    def display_statistics(self):

        total_requisitions = len(self.requisitionlist)

        approved = 0
        pending = 0
        not_approved = 0

        for requisition in self.requisitionlist:

            if requisition.status == "Approved":

                approved += 1

            elif requisition.status == "Pending":

                pending += 1

            elif requisition.status == "Not approved":

                not_approved += 1

        print("\n========== Requisition Statistics ==========")

        print("Total requisitions submitted:", total_requisitions)
        print("Total approved requisitions:", approved)
        print("Total pending requisitions:", pending)
        print("Total not approved requisitions:", not_approved)

    # Main Menu System
    def menu_system(self):

        while True:

            print("\n========== Requisition Management System ==========")

            print("1. Add New Requisition")
            print("2. Display All Requisitions")
            print("3. Manager Approval")
            print("4. Display Requisition Statistics")
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

                print("Thank you for using Requisition Management System.")
                break

            else:

                print("Please enter a valid choice.")


# Create Object
pro = RequisitionManagement()

# Run Menu
pro.menu_system()
