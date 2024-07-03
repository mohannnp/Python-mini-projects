def task():
    tasks = []#empty list
    print("----WELCOME TO THE TASK MANANAGEMENT APP----")

    total_task =int(input("Enter how many task you want to add="))
    for i in range(1,total_task+1):
        task_name =input(f"Enter task {i} =")#enter task 1=
        tasks.append(task_name)

    print(f"Today's tasks are\n{tasks}")
    while True:
        operation = int(input("Enter 1-Add\n 2-Update\n 3-Delete\n 4-View\n 5-Exit/Stop"))
        if operation ==1:
            add = input("Enter the task you want to add = ")
            tasks.append(add)
            print(f"Task {add} has been succesfully added...")

        elif operation == 2:
            updated_val = input("Enter the task name you want to update =")
            if updated_val in tasks:
                Up = input("Enter new task = ")
                ind = tasks.index(updated_val)#it will return integer value 1,2,3 smthng like that
                tasks[ind] =Up
                print(f"Updated task {Up}")

        elif operation == 3:
            del_val= input("Which task you want to delete =")
            if del_val in tasks:
                ind = tasks.index(del_val)
                del tasks[ind]
                print(f"Task {del_val} has been deleted....")

        elif operation == 4:
            print(f"Total tasks = {tasks}")
            
        elif operation == 5:
            print("Closing the program....")
            break

        else:
            print("Invalid Input!!...")




            # tasks.append(updated_val)
            # print(f"the updated task is {updated_val} ")
