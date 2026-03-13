# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

A command-line to-do list application built in Python as a learning project. It teaches lists, file I/O, and CRUD operations step by step.

## Running the App

```bash
python3 todo.py
```

Interactive commands inside the app: `show`, `add`, `done`, `delete`, `quit`.

## Architecture

- **`todo.py`** — Single-file application containing all logic. Currently contains Step 2 (learning lists demo). The README walks through progressive steps, with the full CRUD app defined in Step 4.
- **`todos.json`** — Data persistence file (created at runtime). Stores tasks as JSON array of `{"title": string, "done": boolean}` objects.
- No external dependencies — uses only Python standard library (`json` module).

## Key Patterns

- Tasks are stored as a list of dicts: `[{"title": "...", "done": false}, ...]`
- `save_todos()` / `load_todos()` handle JSON file I/O with `try/except FileNotFoundError` for first-run safety
- The app uses a `while True` input loop with string-matched commands for the menu
- All mutations (add, toggle, delete) call `save_todos()` immediately after modifying the list

## Current State

The `todo.py` file contains the full CRUD app from Step 4 in the README.
