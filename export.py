import csv
import sys


def export_tasks(tasks):
    writer = csv.writer(sys.stdout)
    writer.writerow(["title", "done"])

    for task in tasks:
        writer.writerow([
            task["title"],
            task.get("done", False)
        ])