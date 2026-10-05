def validate_student(name, age, email):

    name = name.strip()

    if name == "":
        return False, "Invalid name"

    if not name.isalpha():
        return False, "Invalid name"

    if age < 18 or age > 60:
        return False, "Invalid age"

    if email == "":
        return False, "Invalid email"

    if "@" not in email or "." not in email:
        return False, "Invalid email"

    if " " in email:
        return False, "Invalid email"

    return True, "Valid"

try:
    name = input("Enter name: ")
    age = input("Enter age: ")
    email = input("Enter email: ")

    age = int(age)

    valid, message = validate_student(name, age, email)

    if valid:
        print("Student accepted")
    else:
        print(message)

except ValueError:
    print("Error: invalid input")