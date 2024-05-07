tasks=[]
tasksv2=[]

def add_task():
    task=input("Enter a new task:")
    tasks.append(task)
    print(":Task added successfully")

def view_task():
    if len(tasks) == 0:
        print("no task")
    else:
        print("list of tasks:")
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task}")
def delete_task():
    if len(tasks) == 0:
        print("no tasks to delete.")
    else:
        print("tasks:")
        for i, task in enumerate(tasks):
            print(f"i{i+1}. {task}")
    choice = int(input("enter the task number to delete:"))
    if 0 < choice <= len(tasks):
        del tasks[choice-1]
        print("task deleted yo.")
    else:
        print("invalid task number.")

def mark_task():
    if len(tasks) == 0:
        print("no tasks to change")
    else:
        print("tasks")
        for i, task in enumerate(tasks):
            print(f"1{i+1}. {tasks}")
    choice = int(input("enter the task number to mark as done"))
    if 0 < choice <= len(task):
        tasks.pop[choice-1]
        tasksv2.append(choice)
        print= (str(tasksv2))


def main():
    while True:
        print("*****To Do List Application*****")
        print('1. Add task')
        print("2. View task")
        print("3. Delete task")
        print("4. Quit")
        print("5. mark task as done")
        choice= int(input("enter your choice:"))
        if choice == 1:
            add_task()
        elif choice == 2:
            view_task()
        elif choice == 3:
            delete_task()
        elif choice == 4:
            print("thank you for using To Do List Application")
        elif choice == 5:
            mark_task()

            break
        else:
            print("invalid choice. Please try again.")
if __name__ == "__main__":
    main()



