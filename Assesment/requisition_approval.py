def requisition_approval(total, staff_id, requisition_id):

    #status pending by default
    status = "Pending"
    approval_reference = ""

    #gave a statement if total is more than 500 than return approved
    if total < 500:
        status = "Approved"
        approval_reference = staff_id + str(requisition_id)[-3:]

    return status, approval_reference
