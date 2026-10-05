def validate_student(name, age, email):

    name = name.strip()

    if name == "":
        return False, "Invalid name"

    if not name.isalpha():
        return False, "Invalid name"

    if not age.isdigit():
        return False, "Invalid age"

    age = int(age)

    if age < 18 or age > 60:
        return False, "Invalid age"

    # Check email
    if email == "":
        return False, "Invalid email"

    if "@" not in email or "." not in email:
        return False, "Invalid email"

    if " " in email:
        return False, "Invalid email"

    return True, "Valid"

# Sample tests
print("John 25 john@email.com ->", validate_student("John", "25", "john@email.com")[1])
print("John2 25 john@email.com ->", validate_student("John2", "25", "john@email.com")[1])
print("John 17 john@email.com ->", validate_student("John", "17", "john@email.com")[1])
print("John 25 johnemail.com ->", validate_student("John", "25", "johnemail.com")[1])

