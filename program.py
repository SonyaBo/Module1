tasks = {}
LOW = "1"
MEDIUM = "2"
HIGH = "3"
PRIORITY = {
    LOW: "low",
    MEDIUM: "medium",
    HIGH: "high"
}
DONE = "1"
DOING = "2"
TODO = "3"
STATUS = {
    DONE: "done",
    DOING: "doing",
    TODO: "todo"
}

def load_tasks() -> None:
    """
    Loads tasks from a file 'tasks.txt' into the tasks dictionary
    Each task is expected to have an ID, name, description, priority, and status

    :return: None
    """
    try:
        with open('tasks.txt', 'r') as f:
            lines = f.readlines()
            for line in lines:
                task_data = line.strip().split(",")
                if len(task_data) == 5:
                    id, name, description, priority, status = task_data
                    tasks[id] = {
                        'name': name,
                        'description': description,
                        'priority': priority,
                        'status': status
                    }
    except FileNotFoundError:
        pass

def save_tasks() -> None:
    """
    Saves the tasks from the tasks dictionary to a file 'tasks.txt'
    Each task is saved with an ID, name, description, priority, and status

    :return: None
    """
    with open('tasks.txt', 'w') as f:
        for id, task in tasks.items():
            f.write(f"{id},{task['name']},{task['description']},{task['priority']},{task['status']}\n")

def add_task(name: str, desc: str, priority: str) -> bool:
    """
    Adds a task to the tasks dictionary

    :param name: name of the task
    :param desc: description of the task
    :param priority: priority of the task, must be in PRIORITY
    :return: True if the task was added
    """
    if priority in PRIORITY and name != "" and desc != "":
        tasks[len(tasks) + 1] = {"name": name, "description": desc, "priority": priority, "status": TODO}
        save_tasks()
        return True
    else:
        return False

def delete_task(id: int) -> bool:
    """
    Deletes a task from the tasks dictionary by its ID

    :param id: The ID of the task
    :return: True if the task was deleted
    """
    if id in tasks:
        del tasks[id]
        save_tasks()
        return True
    else:
        return False

def show_tasks() -> bool:
    """
    Displays all tasks in the tasks dictionary

    :return: True if tasks are displayed
    """
    if not tasks:
        print("No tasks available")
        return False

    for id, details in tasks.items():
        print(
            f"id: {id} \nname: {details['name']} \ndescription: {details['description']}\npriority: {PRIORITY[details['priority']]} \nstatus: {STATUS[details['status']]}")
        print("-" * 25)
    return True

def show_tasks_priority() -> bool:
    """
    Displays tasks sorted by their priority

    :return: True if tasks are displayed
    """
    if not tasks:
        print("No tasks available")
        return False

    sorted_tasks = sorted(tasks.items(), key=lambda x: x[1]['priority'], reverse=True)

    for id, details in sorted_tasks:
        print(
            f"id: {id} \nname: {details['name']} \ndescription: {details['description']}\npriority: {PRIORITY[details['priority']]} \nstatus: {STATUS[details['status']]}")
        print("-" * 25)
    return True

def show_tasks_status() -> bool:
    """
    Displays tasks sorted by their status

    :return: True if tasks are displayed
    """
    if not tasks:
        print("No tasks available")
        return False

    sorted_tasks = sorted(tasks.items(), key=lambda x: x[1]['status'], reverse=True)

    for id, details in sorted_tasks:
        print(
            f"id: {id} \nname: {details['name']} \ndescription: {details['description']}\npriority: {PRIORITY[details['priority']]} \nstatus: {STATUS[details['status']]}")
        print("-" * 25)
    return True

def find_task(task: str) -> bool:
    """
    Finds tasks by their name or description

    :param task: The name or description of the task
    :return: True if at least 1 task is found
    """
    found = False
    for id, details in tasks.items():
        if task.lower() in details["name"].lower() or task.lower() in details["description"].lower():
            found = True
            print(
                f"id: {id} \nname: {details['name']} \ndescription: {details['description']}\npriority: {PRIORITY[details['priority']]} \nstatus: {STATUS[details['status']]}")
            print("-" * 25)
    if not found:
        print("No tasks found.")
    return found

def update_task_name(id: int, name: str) -> bool:
    """
    Updates the name of an existing task

    :param id: The ID of the task
    :param name: The new name of the task
    :return: True if the name is updated
    """
    tasks[id]["name"] = name
    save_tasks()
    return True

def update_task_desc(id: int, desc: str) -> bool:
    """
    Updates the description of an existing task

    :param id: The ID of the task
    :param desc: The new description
    :return: True if the description is updated
    """
    tasks[id]["description"] = desc
    save_tasks()
    return True

def update_task_priority(id: int, prior: str) -> bool:
    """
    Updates the priority of an existing task

    :param id: The ID of the task
    :param prior: The new priority of the task, must be in PRIORITY
    :return: True if the priority is updated
    :raises Exception: If the given priority is not valid
    """
    if prior in PRIORITY:
        tasks[id]["priority"] = prior
        save_tasks()
        return True
    else:
        raise Exception(f"\"{prior}\" is not a valid priority")

def update_task_status(id: int, status: str) -> bool:
    """
    Updates the status of an existing task

    :param id: The ID of the task
    :param status: The new status of the task, must be in STATUS
    :return: True if the status is updated
    :raises Exception: If the given status is not valid
    """
    if status in STATUS:
        tasks[id]["status"] = status
        save_tasks()
        return True
    else:
        raise Exception(f"\"{status}\" is not a valid status")

while True:
    load_tasks()
    print("\n","-"*20)
    print("Welcome to TASK MANAGER (gl)\n\n")
    print("Show tasks: 1")
    print("Add task: 2")
    print("Update task: 3")
    print("Delete task: 4")
    print("Leave: 0")
    choise = input(">")

    if choise == "1":
        print("Show all tasks: 1")
        print("Show tasks by priority: 2")
        print("Show tasks by status: 3")
        print("Find task: 4")
        choise = input(">")
        if choise == "1":
            show_tasks()
        elif choise == "2":
            show_tasks_priority()
        elif choise == "3":
            show_tasks_status()
        elif choise == "4":
            task = input("Enter name or description: ")
            find_task(task)
        else:
            print("Do not understand")
            continue
    elif choise == "2":
        name = input("Enter name of the task: ")
        desc = input("Enter description of the task: ")
        while True:
            print("Choose priority: 1-LOW, 2-MEDIUM, 3-HIGH")
            priority =input(">")

            if priority not in PRIORITY:
                print("Invalid priority, please enter 1, 2, or 3")
                continue
            else:
                break
        if not add_task(name, desc, priority):
            print("Something wnet wrong")
    elif choise == "3":
        id = input("Enter id of the task: ")
        print("Update name: 1")
        print("Update description: 2")
        print("Update priority: 3")
        print("Update status: 4")
        choise = input(">")
        try:
            if choise == "1":
                name = input("Enter new name: ")
                update_task_name(id,name)
            elif choise == "2":
                desc = input("Enter description: ")
                update_task_desc(id,desc)
            elif choise == "3":
                priority = input("Enter priority: 1-LOW, 2-MEDIUM, 3-HIGH: ")
                update_task_desc(id, priority)
            elif choise == "4":
                stat = input("Enter status 1-DONE, 2-DOING, 3-TODO: ")
                update_task_desc(id, stat)
            else:
                print("Do not understand")
                continue
        except Exception as e:
            print(e)
    elif choise == "4":
        id = input("Enter id of the task to be deleted: ")
        if not delete_task(id):
            print("Something went wrong")
    elif choise == "0":
        break
    else:
        print("Sorry what?\n")