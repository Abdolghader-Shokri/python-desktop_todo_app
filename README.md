```markdown
# Desktop Todo App (Python Desktop App)

A simple but well‑structured **Desktop Todo Manager** built with Python and Tkinter.  
This project demonstrates clean project architecture, separation of concerns, and GUI application development practices such as modular design, service layers, data modeling, and JSON‑based data persistence.

The application allows users to **create tasks, view tasks, mark tasks as completed, and delete tasks** through a graphical interface while storing the data locally in a JSON file.

This project was designed as a learning exercise to practice building maintainable Python desktop applications using a modular structure similar to real software projects.

---

## Features

- Add new tasks
- View a list of saved tasks
- Mark tasks as completed or uncompleted
- Delete tasks
- Persistent data storage using JSON
- Simple and clean graphical interface with Tkinter
- Modular architecture (UI, models, services)
- Separation of UI logic and data storage logic

---

## Technologies

- Python 3
- Tkinter for GUI development
- JSON for local data storage
- Standard Python libraries (datetime, json, os)

---

## Project Structure

```
desktop_todo_app/
│
├── main.py
│
├── models/
│   └── task.py
│
├── services/
│   └── storage_service.py
│
└── ui/
    └── app.py
```

*(Note: The `data/tasks.json` file is generated automatically within the project directory upon the first save.)*

---

## Installation

Clone the repository:

```
git clone https://github.com/your-username/desktop-todo-app.git
cd desktop-todo-app
```

Create and activate a virtual environment (optional but recommended):

```
python -m venv venv
source venv/bin/activate
```

---

## Running the Application

Run the program using:

```
python main.py
```

The graphical interface will open, allowing you to create and manage tasks.

---

## Data Storage

All tasks are stored locally in `data/tasks.json` (created automatically).  
Each task is serialized as a JSON object containing:

- id
- title
- completed
- created_at

---

## Learning Goals

This project was built to practice:

- Building desktop applications with Tkinter
- Designing modular Python project structures
- Separating UI logic from business logic
- Managing application data with JSON storage
- Applying object‑oriented programming principles
- Writing maintainable and scalable Python code

---

## License

This project is licensed under the MIT License.  
See the `LICENSE` file for details.
```