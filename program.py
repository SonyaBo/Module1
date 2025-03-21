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
def add_task(name: str, desc: str,priority: str,status: str) -> bool:

    if priority in PRIORITY and status in STATUS:
        tasks[len(tasks)+1] = {"name":name,"description":desc,"priority":priority,"status":status}
        return True
    else:
        return False

def delete_task(id: int) -> bool:
    """
    :param id: id of the task
    :return: true if successful
    """
    if id in tasks:
        del tasks[id]
        return True
    else:
        return False
def show_tasks():
    if not tasks:
        print("No tasks available")
        return False

    for id, details in tasks.items():
        print(f"id: {id} \nname: {details["name"]} \ndescription: {details["description"]}\npriority: {PRIORITY[details["priority"]]} \nstatus: {STATUS[details['status']]}")
        print("-"*25)
    return True

def show_tasks_priority():
    if not tasks:
        print("No tasks available")
        return False

    sorted_tasks = sorted(tasks.items(), key=lambda x: x[1]['priority'],reverse=True)

    for id, details in sorted_tasks:
        print(
            f"id: {id} \nname: {details['name']} \ndescription: {details['description']}\npriority: {PRIORITY[details['priority']]} \nstatus: {STATUS[details['status']]}")
        print("-" * 25)
    return True

def show_tasks_status():
    if not tasks:
        print("No tasks available")
        return False

    sorted_tasks = sorted(tasks.items(), key=lambda x: x[1]['status'], reverse=True)

    for id, details in sorted_tasks:
        print(
            f"id: {id} \nname: {details['name']} \ndescription: {details['description']}\npriority: {PRIORITY[details['priority']]} \nstatus: {STATUS[details['status']]}")
        print("-" * 25)
    return True



def find_task(task: str):
    pass
def update_task_name(id):
    pass
def update_task_desc(id):
    pass
def update_task_priority(id):
    pass
def update_task_status(id):
    pass

add_task("neco","neco","1","1")
add_task("neco","neco","2","2")
add_task("neco","neco","3","3")
add_task("neco","neco","1","1")
show_tasks_status()