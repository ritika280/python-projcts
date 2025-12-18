tasks = []

while True:
    print("1.Add Task  2.View Tasks  3.Delete  4.Exit")
    ch = input("Enter choice: ")

    if ch == "1":
        task = input("Enter task: ")
        tasks.append(task)

    elif ch == "2":
        for i, task in enumerate(tasks):
            print(i+1, task)

    elif ch == "3":
        num = int(input("Enter task number: "))
        tasks.pop(num-1)

    else:
        break

