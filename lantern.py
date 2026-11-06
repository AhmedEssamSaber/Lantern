import argparse
import storage
from export import export_tasks


def main():
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command")

    add_parser = sub.add_parser("add")
    add_parser.add_argument("title")

    list_parser = sub.add_parser("list")

    list_parser.add_argument(
        "--sort",
        action="store_true",
        help="Sort tasks by title"
    )

    list_parser.add_argument(
        "--done",
        action="store_true",
        help="Show completed tasks only"
    )

    export_parser = sub.add_parser("export")
    export_parser.add_argument(
        "--csv",
        action="store_true",
        help="Export tasks as CSV"
    )


    


    export_parser = sub.add_parser("export")
    export_parser.add_argument(
        "--csv",
        action="store_true",
        help="Export tasks as CSV"
    )
    args = parser.parse_args()

    if args.command == "add":
        print("Task added:", args.title)

    elif args.command == "list":
        tasks = storage.load()

        if args.done:
            tasks = [task for task in tasks if task.get("done", False)]

        if args.sort:
            tasks = sorted(tasks, key=lambda task: task["title"].lower())

        if not tasks:
            print("No tasks found.")
        else:
            print("Listing tasks")
            for task in tasks:
                print(task["title"])

    elif args.command == "export":
        if args.csv:
            tasks = storage.load()
            export_tasks(tasks)
        else:
            export_parser.print_help()


if __name__ == "__main__":
    main()