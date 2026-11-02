import json

def load():
    with open("tasks.json", "r") as f:
        return json.load(f)

def save(tasks):
    with open("tasks.json", "w") as f:

        json.dump(tasks, f, sort_keys=True, indent=2)

        
        

