# To-Do List App with FastAPI

A simple to-do list application built with FastAPI and JavaScript, showcasing API integration and basic frontend functionalities.

## Features

- Add new tasks to the list
- View all tasks in real-time
- Persistent server-side task management (in-memory for now)

## Tech Stack

- Backend: FastAPI (Python)
- Frontend: HTML, CSS, JavaScript (Vanilla)
- Hosting: Uvicorn

## How to Run

1. Clone the repository:

    git clone https://github.com/yourusername/todo-list-app.git
    cd todo-list-app

2. Install dependencies:

    pip install fastapi uvicorn

3. Run the FastAPI server:

    uvicorn main:app --reload

4. Access the app in your browser at:

    http://127.0.0.1:8000

## API Endpoints

- GET /tasks — Retrieve all tasks
- POST /tasks — Add a new task (expects JSON payload)

Example payload for adding a task:

    {
      "task": "Buy groceries"
    }

## Learnings

This project helped reinforce concepts related to:

- FastAPI for building RESTful APIs
- Frontend-backend integration with fetch API
- Real-time updates and UI interaction handling with JavaScript

## Next Steps

- Add a database for persistent storage
- Implement user authentication
- Containerize the app with Docker

## Acknowledgments

- FastAPI documentation: https://fastapi.tiangolo.com/
- Inspiration from various FastAPI tutorials online

---

Feel free to customize it further to reflect your experience and any additional features you’d like to highlight. Let me know if you’d like me to add anything or refine the structure. 🚀
