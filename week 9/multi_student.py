students = []


def validate_student(name, age, email):
    # Check name
    if name == "":
        return False

    # Check age
    if age <= 0:
        return False

    # Check email
    if "@" not in email or "." not in email:
        return False

    return True


# Enter 3 students
for i in range(3):

    print(f"\nEnter details for Student {i + 1}")

    name = input("Enter name: ")
    age = int(input("Enter age: "))
    email = input("Enter email: ")

    # Validate
    if validate_student(name, age, email):

        student = {
            "name": name,
            "age": age,
            "email": email
        }

        students.append(student)

        print(f"Student {i + 1} added")

    else:
        print(f"Student {i + 1} invalid")


# Display the final list
print("\nRegistered Students:")

for student in students:
    print(student)