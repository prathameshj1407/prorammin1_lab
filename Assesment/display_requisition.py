def display_requisitions(date, requisition_id, staff_id,staff_name, total, status,approval_reference):

    print("\nPrinting requisitions:")
    print("Date:", date)
    print("Requisition ID:", requisition_id)
    print("Staff ID:", staff_id)
    print("Staff Name:", staff_name)
    print("Total: ",format(total))
    print("Status:", status)

    if approval_reference:
        print("Approval Reference Number:", approval_reference)
    else:
        print("Approval Reference Number: N/A")