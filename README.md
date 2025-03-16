# To-Do List App with FastAPI

This is a simple to-do list web app built with FastAPI and plain HTML/JavaScript. The app allows you to add tasks and mark them as complete, with completed tasks moving to the bottom of the list and appearing greyed out with a strikethrough.

## Features

- Add new tasks to the list.
- Mark tasks as completed — completed tasks are moved to the bottom of the list and displayed with a strikethrough.
- FastAPI backend with in-memory storage (resets when the server restarts).
- Vanilla JavaScript frontend with simple DOM manipulation.

## Tech Stack

- FastAPI (Python)
- HTML, CSS, and Vanilla JavaScript for the frontend

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/todo-app.git
cd todo-app
```

2. Create a virtual environment and install dependencies:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install fastapi uvicorn
```

## Running the App

Start the FastAPI server with Uvicorn:

```bash
uvicorn main:app --reload
```

The app should now be accessible at [http://localhost:8000](http://localhost:8000).

## Project Structure

```
├── main.py
└── static
    └── index.html
```

- `main.py`: FastAPI backend handling tasks.
- `static/index.html`: Frontend interface.

## Usage

1. Open [http://localhost:8000](http://localhost:8000) in your browser.
2. Add tasks using the input field and "Add Task" button.
3. Check off completed tasks to move them to the bottom.

## Future Improvements

- Persistent storage using a database.
- Docker containerization.
- Enhanced UI/UX.

## License

This project is licensed under the MIT License.

---

Enjoy building with FastAPI! 🚀



