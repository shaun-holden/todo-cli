# Build a Command-Line To-Do List (Python)

Learn **lists**, **file I/O**, and **CRUD logic** by building a to-do app step by step in your terminal.

---

## Prerequisites

- Python 3 installed (check with `python3 --version`)
- A terminal (Terminal.app, VS Code terminal, etc.)

---

## Step 1: Create the Project

Open your terminal and paste:

```bash
cd ~/Desktop/todo-cli
touch todo.py
```

This creates the Python file you'll be working in.

---

## Step 2: Learn About Lists

Lists are ordered collections that store your to-do items. Open `todo.py` in your editor and paste this code:

```python
# --- STEP 2: Learning Lists ---

# A list is created with square brackets
todos = ["Buy groceries", "Walk the dog", "Do laundry"]

# Print each item with its position (index)
for i, task in enumerate(todos):
    print(f"  {i + 1}. {task}")

# Add an item to the end
todos.append("Read a book")
print("\nAfter adding 'Read a book':")
for i, task in enumerate(todos):
    print(f"  {i + 1}. {task}")

# Remove an item by index
removed = todos.pop(1)  # removes index 1 ("Walk the dog")
print(f"\nRemoved: {removed}")
for i, task in enumerate(todos):
    print(f"  {i + 1}. {task}")
```

Now run it:

```bash
python3 todo.py
```

**What you learned:**
- `[]` creates a list
- `enumerate()` gives you both the index and the value
- `.append()` adds to the end (Create)
- `.pop(index)` removes by position (Delete)
- `f"..."` is an f-string for easy formatting

---

## Step 3: Learn About File I/O

Your to-dos disappear when the program ends. File I/O lets you **save** and **load** them. Replace everything in `todo.py` with:

```python
# --- STEP 3: Learning File I/O ---
import json

FILENAME = "todos.json"

# SAVE: Write a list to a file
def save_todos(todos):
    with open(FILENAME, "w") as f:
        json.dump(todos, f, indent=2)
    print(f"Saved {len(todos)} tasks to {FILENAME}")

# LOAD: Read a list from a file
def load_todos():
    try:
        with open(FILENAME, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []  # first run, no file yet

# Test it out
my_todos = ["Buy groceries", "Walk the dog"]
save_todos(my_todos)

loaded = load_todos()
print(f"Loaded: {loaded}")
```

Run it:

```bash
python3 todo.py
```

Then check the saved file:

```bash
cat todos.json
```

**What you learned:**
- `json.dump()` writes Python data to a file
- `json.load()` reads it back
- `with open(...)` safely opens/closes files
- `"w"` = write mode, `"r"` = read mode
- `try/except` handles the case where the file doesn't exist yet

---

## Step 4: Build the Full CRUD App

CRUD = **C**reate, **R**ead, **U**pdate, **D**elete. Replace everything in `todo.py` with:

```python
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
```

Run the app:

```bash
python3 todo.py
```

Try these commands inside the app:
1. Type `add` and enter a task
2. Type `show` to see your list
3. Type `done` and pick a number to mark it complete
4. Type `delete` to remove a task
5. Type `quit` to exit

Now run it again — your tasks are still there (loaded from `todos.json`):

```bash
python3 todo.py
```

---

## Step 5: Verify Data Persistence

After adding a few tasks and quitting, inspect the saved data:

```bash
cat todos.json
```

You'll see something like:

```json
[
  {
    "title": "Buy groceries",
    "done": true
  },
  {
    "title": "Learn Python",
    "done": false
  }
]
```

---

## Concepts Summary

| Concept | What You Used | Where |
|---------|--------------|-------|
| **Lists** | `[]`, `.append()`, `.pop()`, `enumerate()` | Storing tasks in memory |
| **Dicts** | `{"title": ..., "done": ...}` | Each task has multiple properties |
| **File I/O** | `open()`, `json.dump()`, `json.load()` | Saving/loading between sessions |
| **Create** | `add_todo()` — appends to list, saves file | Adding new tasks |
| **Read** | `show_todos()` — loops and prints | Displaying tasks |
| **Update** | `toggle_todo()` — flips `done` flag | Marking tasks complete |
| **Delete** | `delete_todo()` — `.pop()` removes from list | Removing tasks |
| **Loop** | `while True` + `break` | Keeps the menu running |
| **Error Handling** | `try/except` | Handles bad input and missing files |

---

## Bonus Challenges (Try These Next)

1. **Edit a task's title** — add an `edit` command
2. **Add priority levels** — high, medium, low
3. **Add due dates** — use `datetime` module
4. **Clear all completed** — delete all tasks where `done` is True
5. **Color output** — use `\033[32m` for green (done) and `\033[0m` to reset
