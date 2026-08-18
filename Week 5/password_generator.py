first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
fav_number = input("Enter your favorite number: ")
spe_char = input("Enter your special character: ")

password = first_name[:2].upper() + last_name[-2:].lower() + fav_number + spe_char

print("Generated Password: ", password)