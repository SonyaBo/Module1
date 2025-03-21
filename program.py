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

def delete_task(id: int) -> bool:
    """
    :param id: id of the task
    :return: true if successful
    """


def update_task(id,num):
    pass

def save():
    pass

add_task("hw","1","1")
print(tasks[1])