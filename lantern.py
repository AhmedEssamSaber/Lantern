import argparse


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
        print("Listing tasks")


if __name__ == "__main__":
    main()