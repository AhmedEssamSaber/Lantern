def add_task(title):
    task = {"title": title.strip(), "done": False}
    return task



def list_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return

    for task in tasks:
        print(task)
