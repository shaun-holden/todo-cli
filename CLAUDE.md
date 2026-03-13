# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

A command-line to-do list application built in Python as a learning project. It teaches lists, file I/O, and CRUD operations step by step.

## Running the App

```bash
python3 todo.py
```

Interactive commands inside the app: `show`, `add`, `edit`, `done`, `delete`, `clear`, `quit`.

## Architecture

- **`todo.py`** — Single-file application containing all logic (full CRUD app plus bonus features).
- **`todos.json`** — Data persistence file (created at runtime). Stores tasks as JSON array of `{"title": string, "done": boolean, "priority": string, "due": string}` objects.
- No external dependencies — uses only Python standard library (`json`, `datetime`).

## Key Patterns

- Tasks are stored as a list of dicts with keys: `title`, `done`, `priority` (high/medium/low or empty), `due` (YYYY-MM-DD or empty)
- `save_todos()` / `load_todos()` handle JSON file I/O with `try/except FileNotFoundError` for first-run safety
- The app uses a `while True` input loop with string-matched commands for the menu
- All mutations (add, edit, toggle, delete, clear) call `save_todos()` immediately after modifying the list
- ANSI color codes are used for output: green for done, red/yellow/green for priority levels, dim for completed task titles
