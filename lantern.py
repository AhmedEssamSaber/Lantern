import argparse

import storage
from tasks import list_tasks


def main():
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command")

    add_parser = sub.add_parser("add")
    add_parser.add_argument("title")

    list_parser = sub.add_parser("list")

    args = parser.parse_args()

    if args.command == "add":
        print("Task added:", args.title)

    elif args.command == "list":
      tasks = storage.load()
      if not tasks:
        print("No tasks found.")
      else:
        if args.sort:
          tasks.sort(key=lambda x: x["title"])
        list_tasks(tasks)



if __name__ == "__main__":
    main()