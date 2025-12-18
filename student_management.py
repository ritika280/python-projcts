students = []

def add_student():
    name = input("Enter name: ")
    roll = input("Enter roll no: ")
    students.append({"name": name, "roll": roll})

def view_students():
    for s in students:
        print(s["roll"], s["name"])

while True:
    print("1.Add  2.View  3.Exit")
    choice = input("Choose: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    else:
        break

