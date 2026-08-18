info = {}
while True:
    name = input("Enter your name: ")
    if name == "stop" or name == "end" or name == "quit" or name == "":
        break
    phone = input("Enter your phone number: ")
    info[name] = phone
print(info)