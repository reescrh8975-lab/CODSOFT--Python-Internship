contacts = {}

while True:
    print("1.Add 2.View 3.Exit")
    ch = input("Choice: ")

    if ch == "1":
        name = input("Name: ")
        phone = input("Phone: ")
        contacts[name] = phone

    elif ch == "2":
        for name, phone in contacts.items():
            print(name, "-", phone)

    elif ch == "3":
        break
