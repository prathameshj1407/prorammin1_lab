
class Requisition:
    # Shared class attributes
    requisition_counter = 10000
    all_requisitions = []

    def __init__(self, date, staff_id, staff_name):
        # Generate a unique requisition ID
        Requisition.requisition_counter += 1
        self.requisition_id = Requisition.requisition_counter

        # Information belonging to this object
        self.date = date
        self.staff_id = staff_id
        self.staff_name = staff_name
        self.items = []
        self.total = 0.0
        self.status = "Pending"
        self.approval_reference = "Not available"

        # Track every submitted requisition
        Requisition.all_requisitions.append(self)

    def add_requisition(self, items):
        """Store the items and calculate the total."""
        if not items:
            raise ValueError("A requisition must contain at least one item.")

        calculated_total = 0.0

        for item in items:
            if "name" not in item or "price" not in item:
                raise ValueError("Each item needs a name and a price.")

            price = float(item["price"])

            if not item["name"].strip() or price < 0:
                raise ValueError("Enter a valid item name and price.")

            calculated_total += price

        self.items = [item.copy() for item in items]
        self.total = round(calculated_total, 2)

        # Determine the initial approval status
        self.approve_requisition()
        return self.total

    def approve_requisition(self):
        """Automatically approve totals below $500."""
        if self.total < 500:
            self.status = "Approved"
            self.approval_reference = (
                self.staff_id + str(self.requisition_id)[-3:]
            )
        else:
            self.status = "Pending"
            self.approval_reference = "Not available"

        return self.status

    def respond_to_requisition(self, decision):
        """Allow a manager to respond to a pending request."""
        if self.status != "Pending":
            raise ValueError("Only pending requisitions can be reviewed.")

        decision = decision.strip().lower()

        if decision == "approved":
            self.status = "Approved"
            self.approval_reference = (
                self.staff_id + str(self.requisition_id)[-3:]
            )
        elif decision == "not approved":
            self.status = "Not approved"
            self.approval_reference = "Not available"
        else:
            raise ValueError(
                "Decision must be Approved or Not approved."
            )

        return self.status

    def display_requisition(self):
        """Display the details of this requisition."""
        print(f"Date: {self.date}")
        print(f"Requisition ID: {self.requisition_id}")
        print(f"Staff ID: {self.staff_id}")
        print(f"Staff Name: {self.staff_name}")
        print(f"Total: ${self.total:.2f}")
        print(f"Status: {self.status}")
        print(
            "Approval Reference Number: "
            f"{self.approval_reference}"
        )
        print("-" * 40)

    @classmethod
    def display_requisitions(cls):
        """Display every requisition submitted."""
        for requisition in cls.all_requisitions:
            requisition.display_requisition()

    @classmethod
    def requisition_statistics(cls):
        """Return counts for each requisition status."""
        statistics = {
            "total": len(cls.all_requisitions),
            "approved": 0,
            "pending": 0,
            "not_approved": 0
        }

        for requisition in cls.all_requisitions:
            if requisition.status == "Approved":
                statistics["approved"] += 1
            elif requisition.status == "Pending":
                statistics["pending"] += 1
            elif requisition.status == "Not approved":
                statistics["not_approved"] += 1

        return statistics

    @classmethod
    def display_statistics(cls):
        """Print the current requisition statistics."""
        stats = cls.requisition_statistics()

        print("\nRequisition Statistics")
        print(
            "Total requisitions submitted:",
            stats["total"]
        )
        print(
            "Total approved requisitions:",
            stats["approved"]
        )
        print(
            "Total pending requisitions:",
            stats["pending"]
        )
        print(
            "Total not approved requisitions:",
            stats["not_approved"]
        )



# Test 1: Total below $500
request1 = Requisition(
    "03/04/2024", "FN19", "John Paul"
)
request1.add_requisition([
    {"name": "Keyboard", "price": 150},
    {"name": "Mouse", "price": 50},
    {"name": "Monitor", "price": 250}
])


# Test 2: Total above $500
request2 = Requisition(
    "05/04/2024", "FN20", "Tracy Brown"
)
request2.add_requisition([
    {"name": "Laptop", "price": 1000}
])


# Test 3: High-value requisition
request3 = Requisition(
    "07/05/2024", "FN15", "Emma Wellington"
)
request3.add_requisition([
    {"name": "Computer equipment", "price": 3500}
])


# Test 4: Another total below $500
request4 = Requisition(
    "03/05/2024", "FN02", "Catlin White"
)
request4.add_requisition([
    {"name": "Office supplies", "price": 490}
])


# Test 5: Leave a requisition pending
request5 = Requisition(
    "10/05/2024", "FN25", "Alex Green"
)
request5.add_requisition([
    {"name": "Printer", "price": 650}
])


# Display all five before manager responses
print("INITIAL REQUISITIONS")
Requisition.display_requisitions()

print("\nSTATISTICS BEFORE MANAGER RESPONSES")
Requisition.display_statistics()


# Manager responds to pending requisitions
request2.respond_to_requisition("Approved")
request3.respond_to_requisition("Not approved")

# Request 5 remains pending


# Display updated information
print("\nUPDATED REQUISITIONS")
Requisition.display_requisitions()

print("\nSTATISTICS AFTER MANAGER RESPONSES")
Requisition.display_statistics()
