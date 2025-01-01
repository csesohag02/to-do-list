# To-Do List Application

## Overview
This is a simple command-line To-Do List application written in Python. It allows users to manage their tasks by adding, viewing, marking as done, and deleting tasks. The tasks are saved in a JSON file for persistence across sessions.

## Features
- **Add Tasks**: Add a task with a description.
- **List Tasks**: View all tasks with their status (Pending or Done).
- **Mark as Done**: Mark tasks as completed.
- **Delete Tasks**: Remove tasks from the list.
- **Data Persistence**: Tasks are stored in a JSON file (`tasks.json`).
- **Error Handling**: Handles invalid inputs and missing files gracefully.

## Requirements
- Python 3.x

## Installation
1. Clone this repository or download the script.
2. Ensure Python 3.x is installed on your system.
3. No external libraries are required; the script uses Python's standard library.

## Usage
Run the script in a terminal or command prompt:
```bash
python todo_list_app.py
```

### Menu Options:
1. **Add Task**: Enter a description to add a new task.
2. **List Tasks**: View all tasks with their respective status.
3. **Mark Task as Done**: Enter the task number to mark it as completed.
4. **Delete Task**: Enter the task number to delete it.
5. **Exit**: Close the application.

## File Details
- **`tasks.json`**: Stores tasks in a structured JSON format. Automatically created on the first run.

### Example format:
```json
[
    {
        "description": "Buy groceries",
        "completed": false
    },
    {
        "description": "Complete Python project",
        "completed": true
    }
]
```

## Error Handling
- If the `tasks.json` file is missing, it will be created automatically.
- Invalid task numbers (e.g., out of range) will display an error message.
- Non-numeric inputs for task operations will prompt the user to enter a valid number.

## Examples

### Example 1: Adding and Listing Tasks
1. Add a task: `Buy groceries`.
   ```bash
   Choose an option: 1
   Enter task description: Buy groceries
   Task added: Buy groceries
   ```
2. List tasks:
   ```bash
   Choose an option: 2
   1. Buy groceries [Pending]
   ```

### Example 2: Marking a Task as Done
1. Mark task 1 as done:
   ```bash
   Choose an option: 3
   Enter task number to mark as done: 1
   Task 1 marked as done.
   ```
2. List tasks:
   ```bash
   Choose an option: 2
   1. Buy groceries [Done]
   ```

### Example 3: Deleting a Task
1. Delete task 1:
   ```bash
   Choose an option: 4
   Enter task number to delete: 1
   Task deleted: Buy groceries
   ```
2. List tasks:
   ```bash
   Choose an option: 2
   No tasks available.
   ```

## Author
- Created and maintained by **Sohag Chakraborty**  
  GitHub: [**@csesohag02**](https://github.com/csesohag02)
