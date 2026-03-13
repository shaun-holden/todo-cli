# --- Full CRUD To-Do App with Bonus Features ---
import json
from datetime import datetime

FILENAME = "todos.json"

# ---- COLORS ----

GREEN = "\033[32m"
YELLOW = "\033[33m"
RED = "\033[31m"
RESET = "\033[0m"
DIM = "\033[2m"

PRIORITY_COLORS = {"high": RED, "medium": YELLOW, "low": GREEN}

# ---- FILE I/O ----

def save_todos(todos):
    with open(FILENAME, "w") as f:
        json.dump(todos, f, indent=2)

def load_todos():
    try:
        with open(FILENAME, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# ---- DISPLAY (Read) ----

def show_todos(todos):
    if not todos:
        print("\n  No tasks yet! Add one with 'add'.\n")
        return
    print("\n  Your To-Do List:")
    print("  " + "-" * 45)
    for i, task in enumerate(todos):
        if task["done"]:
            status = f"{GREEN}[x]{RESET}"
            title = f"{DIM}{task['title']}{RESET}"
        else:
            status = "[ ]"
            title = task["title"]

        priority = task.get("priority", "")
        pri_str = ""
        if priority:
            color = PRIORITY_COLORS.get(priority, "")
            pri_str = f" {color}({priority}){RESET}"

        due = task.get("due", "")
        due_str = ""
        if due:
            due_str = f" {DIM}due: {due}{RESET}"

        print(f"  {i + 1}. {status} {title}{pri_str}{due_str}")
    print()

# ---- CREATE ----

def add_todo(todos):
    title = input("  Enter task: ").strip()
    if not title:
        print("  Task cannot be empty.")
        return

    priority = input("  Priority (high/medium/low or skip): ").strip().lower()
    if priority not in ("high", "medium", "low"):
        priority = ""

    due = input("  Due date (YYYY-MM-DD or skip): ").strip()
    try:
        datetime.strptime(due, "%Y-%m-%d")
    except ValueError:
        due = ""

    task = {"title": title, "done": False, "priority": priority, "due": due}
    todos.append(task)
    save_todos(todos)
    print(f"  Added: {title}")

# ---- EDIT ----

def edit_todo(todos):
    show_todos(todos)
    try:
        num = int(input("  Task number to edit: "))
        task = todos[num - 1]
        new_title = input(f"  New title (was: {task['title']}): ").strip()
        if not new_title:
            print("  Title cannot be empty.")
            return
        old_title = task["title"]
        task["title"] = new_title
        save_todos(todos)
        print(f"  Renamed: '{old_title}' -> '{new_title}'")
    except (ValueError, IndexError):
        print("  Invalid task number.")

# ---- UPDATE ----

def toggle_todo(todos):
    show_todos(todos)
    try:
        num = int(input("  Task number to toggle: "))
        task = todos[num - 1]
        task["done"] = not task["done"]
        save_todos(todos)
        status = "done" if task["done"] else "not done"
        print(f"  '{task['title']}' marked as {status}")
    except (ValueError, IndexError):
        print("  Invalid task number.")

# ---- DELETE ----

def delete_todo(todos):
    show_todos(todos)
    try:
        num = int(input("  Task number to delete: "))
        removed = todos.pop(num - 1)
        save_todos(todos)
        print(f"  Deleted: {removed['title']}")
    except (ValueError, IndexError):
        print("  Invalid task number.")

# ---- SEARCH ----

def search_todos(todos):
    keyword = input("  Search keyword: ").strip().lower()
    if not keyword:
        print("  Keyword cannot be empty.")
        return
    matches = [(i, t) for i, t in enumerate(todos) if keyword in t["title"].lower()]
    if not matches:
        print(f"  No tasks matching '{keyword}'.")
        return
    print(f"\n  Results for '{keyword}':")
    print("  " + "-" * 45)
    for i, task in matches:
        if task["done"]:
            status = f"{GREEN}[x]{RESET}"
            title = f"{DIM}{task['title']}{RESET}"
        else:
            status = "[ ]"
            title = task["title"]
        priority = task.get("priority", "")
        pri_str = f" {PRIORITY_COLORS.get(priority, '')}({priority}){RESET}" if priority else ""
        due = task.get("due", "")
        due_str = f" {DIM}due: {due}{RESET}" if due else ""
        print(f"  {i + 1}. {status} {title}{pri_str}{due_str}")
    print()

# ---- SORT ----

PRIORITY_ORDER = {"high": 0, "medium": 1, "low": 2, "": 3}

def sort_todos(todos):
    if not todos:
        print("  No tasks to sort.")
        return
    choice = input("  Sort by (priority/due): ").strip().lower()
    if choice == "priority":
        todos.sort(key=lambda t: PRIORITY_ORDER.get(t.get("priority", ""), 3))
        save_todos(todos)
        print("  Sorted by priority (high -> medium -> low).")
        show_todos(todos)
    elif choice == "due":
        todos.sort(key=lambda t: t.get("due", "") or "9999-99-99")
        save_todos(todos)
        print("  Sorted by due date (earliest first).")
        show_todos(todos)
    else:
        print("  Invalid option. Use 'priority' or 'due'.")

# ---- EXPORT ----

def export_todos(todos):
    if not todos:
        print("  No tasks to export.")
        return
    filename = input("  Export filename (default: todos.txt): ").strip()
    if not filename:
        filename = "todos.txt"
    with open(filename, "w") as f:
        f.write("TO-DO LIST\n")
        f.write("=" * 45 + "\n\n")
        for i, task in enumerate(todos):
            status = "[x]" if task["done"] else "[ ]"
            priority = task.get("priority", "")
            pri_str = f" ({priority})" if priority else ""
            due = task.get("due", "")
            due_str = f" due: {due}" if due else ""
            f.write(f"{i + 1}. {status} {task['title']}{pri_str}{due_str}\n")
    print(f"  Exported {len(todos)} task(s) to {filename}")

# ---- CLEAR COMPLETED ----

def clear_completed(todos):
    completed = [t for t in todos if t["done"]]
    if not completed:
        print("  No completed tasks to clear.")
        return
    remaining = [t for t in todos if not t["done"]]
    todos.clear()
    todos.extend(remaining)
    save_todos(todos)
    print(f"  Cleared {len(completed)} completed task(s).")

# ---- HELP ----

def show_help():
    print("\n  Available Commands:")
    print("  " + "-" * 45)
    print("  show     Display all tasks")
    print("  add      Add a new task (with priority and due date)")
    print("  edit     Rename an existing task")
    print("  done     Toggle a task's completion status")
    print("  delete   Remove a task")
    print("  search   Find tasks by keyword")
    print("  sort     Sort tasks by priority or due date")
    print("  export   Save tasks as a plain text file")
    print("  clear    Remove all completed tasks")
    print("  help     Show this help message")
    print("  quit     Exit the app")
    print()

# ---- MAIN MENU ----

def main():
    todos = load_todos()
    print("\n  === TO-DO LIST ===")

    while True:
        print("  Commands: show | add | edit | done | delete | search | sort | export | clear | help | quit")
        command = input("  > ").strip().lower()

        if command == "show":
            show_todos(todos)
        elif command == "add":
            add_todo(todos)
        elif command == "edit":
            edit_todo(todos)
        elif command == "done":
            toggle_todo(todos)
        elif command == "delete":
            delete_todo(todos)
        elif command == "search":
            search_todos(todos)
        elif command == "sort":
            sort_todos(todos)
        elif command == "export":
            export_todos(todos)
        elif command == "clear":
            clear_completed(todos)
        elif command == "help":
            show_help()
        elif command == "quit":
            print("  Goodbye!")
            break
        else:
            print("  Unknown command. Type 'help' for a list of commands.")

main()
