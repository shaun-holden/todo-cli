# --- STEP 4: Full CRUD To-Do App ---
import json

FILENAME = "todos.json"

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
    print("  " + "-" * 30)
    for i, task in enumerate(todos):
        status = "x" if task["done"] else " "
        print(f"  {i + 1}. [{status}] {task['title']}")
    print()

# ---- CREATE ----

def add_todo(todos):
    title = input("  Enter task: ").strip()
    if not title:
        print("  Task cannot be empty.")
        return
    todos.append({"title": title, "done": False})
    save_todos(todos)
    print(f"  Added: {title}")

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

# ---- MAIN MENU ----

def main():
    todos = load_todos()
    print("\n  === TO-DO LIST ===")

    while True:
        print("  Commands: show | add | done | delete | quit")
        command = input("  > ").strip().lower()

        if command == "show":
            show_todos(todos)
        elif command == "add":
            add_todo(todos)
        elif command == "done":
            toggle_todo(todos)
        elif command == "delete":
            delete_todo(todos)
        elif command == "quit":
            print("  Goodbye!")
            break
        else:
            print("  Unknown command. Try: show, add, done, delete, quit")

main()
