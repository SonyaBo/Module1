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
def add_task(task: str,priority: str,status: str) -> bool:
    """
    :param task: text of the task
    :param priorit y: priority of the task
    :param status: status of the task
    :return: true if successful
    """
    if priority in PRIORITY and status in STATUS:
        tasks[len(tasks)+1] = {"task":task,"priority":priority,"status":status}
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
        print("No tasks available.")
        return

    for id, details in tasks.items():
        print(f"id: {id} \ntask: {details["task"]} \npriority: {PRIORITY[details["priority"]]} \nstatus: {STATUS[details['status']]}")
        print("-"*25)

def update_task(id, **kwargs):
    pass
def update_task(id,**kwargs):
    pass

def save():
    pass
add_task("neco","1","1")
show_tasks()