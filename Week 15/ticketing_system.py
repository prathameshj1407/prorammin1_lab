

from datetime import date


# Ticket Class
class Ticket:
    def __init__(self, ticket_id, employee_id, employee_name, issue_description):

        self.ticket_id = ticket_id
        self.submission_date = date.today()
        self.employee_id = employee_id
        self.employee_name = employee_name
        self.issue_description = issue_description

        self.priority = self.assign_priority()
        self.resolution_message = ""

        # Automatic Password Reset
        if "password reset" in issue_description.lower():

            self.status = "Resolved"

            new_password = employee_id[:2] + employee_name[:2]

            self.resolution_message = "Password reset successfully. New password: " + new_password

        else:
            self.status = "In Progress"

            if self.priority == "High":
                self.resolution_message = "Pending Manager Approval"
            else:
                self.resolution_message = "Waiting for IT Support"

    # Assign Ticket Priority
    def assign_priority(self):

        issue = self.issue_description.lower()

        if ("system outage" in issue or
            "server down" in issue or
            "network down" in issue or
            "security breach" in issue or
            "critical" in issue):

            return "High"

        elif "password reset" in issue:
            return "Low"

        else:
            return "Medium"

    # Update Ticket Status
    def update_status(self, new_status):

        if new_status == "Closed" and self.priority == "High":

            print("High priority ticket requires manager approval.")

        elif new_status in ["Resolved", "In Progress", "Closed"]:

            self.status = new_status
            print("Ticket status updated successfully.")

        else:
            print("Invalid status.")

    # Manager Approval
    def manager_approval(self, choice):

        if self.priority == "High":

            if choice == "1":

                self.status = "Closed"
                self.resolution_message = "Resolution approved by manager."

                print("Manager approved the resolution.")
                print("Ticket is now Closed.")

            elif choice == "2":

                self.status = "In Progress"
                self.resolution_message = "Resolution rejected. Further work required."

                print("Manager rejected the resolution.")
                print("Ticket is now In Progress.")

            else:
                print("Invalid choice.")

        else:
            print("Manager approval is only required for High priority tickets.")


# Help Desk Management Class
class HelpDeskManagement:

    def __init__(self):

        self.ticketlist = []
        self.ticket_id = 10100

    # Submit New Ticket
    def submit_ticket(self):

        employee_id = input("Enter Employee ID: ")
        employee_name = input("Enter Employee Name: ")
        issue_description = input("Enter Issue Description: ")

        ticket = Ticket(
            self.ticket_id,
            employee_id,
            employee_name,
            issue_description
        )

        self.ticketlist.append(ticket)

        print("\nTicket submitted successfully.")
        print("Ticket ID:", ticket.ticket_id)
        print("Priority:", ticket.priority)
        print("Status:", ticket.status)
        print("Resolution Message:", ticket.resolution_message)

        self.ticket_id += 1

    # View All Tickets
    def view_tickets(self):

        if len(self.ticketlist) == 0:

            print("No Tickets Submitted.")
            return

        for ticket in self.ticketlist:

            print("\n---------------- Ticket Details ----------------")

            print("Date:", ticket.submission_date)
            print("Ticket ID:", ticket.ticket_id)
            print("Employee ID:", ticket.employee_id)
            print("Employee Name:", ticket.employee_name)
            print("Issue Description:", ticket.issue_description)
            print("Priority:", ticket.priority)
            print("Status:", ticket.status)
            print("Resolution Message:", ticket.resolution_message)

    # Update Ticket Status
    def update_ticket_status(self):

        ticket_id = int(input("Enter Ticket ID you want to update: "))

        for ticket in self.ticketlist:

            if ticket.ticket_id == ticket_id:

                print("\n1. Resolved")
                print("2. In Progress")
                print("3. Closed")

                choice = input("Enter your choice: ")

                if choice == "1":
                    ticket.update_status("Resolved")

                elif choice == "2":
                    ticket.update_status("In Progress")

                elif choice == "3":
                    ticket.update_status("Closed")

                else:
                    print("Please enter a valid choice.")

                return

        print("Ticket ID not found.")

    # Manager Approval
    def manager_approval(self):

        ticket_id = int(input("Enter Ticket ID for Manager Approval: "))

        for ticket in self.ticketlist:

            if ticket.ticket_id == ticket_id:

                print("\n1. Approve Resolution")
                print("2. Reject Resolution")

                choice = input("Enter your choice: ")

                ticket.manager_approval(choice)

                return

        print("Ticket ID not found.")

    # Ticket Statistics
    def display_summary(self):

        total_tickets = len(self.ticketlist)

        resolved = 0
        in_progress = 0
        closed = 0

        for ticket in self.ticketlist:

            if ticket.status == "Resolved":
                resolved += 1

            elif ticket.status == "In Progress":
                in_progress += 1

            elif ticket.status == "Closed":
                closed += 1

        print("\n------------- Ticket Statistics -------------")

        print("Total number of tickets submitted:", total_tickets)
        print("Total number of resolved tickets:", resolved)
        print("Total number of tickets in progress:", in_progress)
        print("Total number of closed tickets:", closed)

    # Main Menu System
    def menu_system(self):

        while True:

            print("\n========== Help Desk Ticketing System ==========")

            print("1. Submit New Ticket")
            print("2. View All Tickets")
            print("3. Update Ticket Status")
            print("4. Manager Approval")
            print("5. View Ticket Statistics")
            print("6. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.submit_ticket()

            elif choice == "2":
                self.view_tickets()

            elif choice == "3":
                self.update_ticket_status()

            elif choice == "4":
                self.manager_approval()

            elif choice == "5":
                self.display_summary()

            elif choice == "6":
                print("Thank you for using Help Desk Ticketing System.")
                break

            else:
                print("Please enter a valid choice.")


# Create Object
helpdesk = HelpDeskManagement()

# Run Menu
helpdesk.menu_system()
