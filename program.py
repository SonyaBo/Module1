tasks = {}
LOW = "1"
MEDIUM = "2"
HIGH = "3"
STATUS = {
    LOW: "low",
    MEDIUM: "medium",
    HIGH: "high"
}
def add_task(task: str,priority: str,status: str) -> bool:
    if priority in status:
        tasks[len(tasks)+1] = {"task":task,"priority":priority,"status":status}



def delete_task(id):
    pass

def update_task(id,num):
    pass

def save():
    pass
