Overview

This project is a Work Breakdown & Task Management System designed to efficiently manage project tasks, timelines, and dependencies. It allows users to create, update, delete, and track tasks through a web interface while providing a clear backend API structure for future scalability.

The system also incorporates LLM-assisted reasoning for task prioritization, error detection, and workflow optimization.

Features

Create, update, delete, and view tasks

Track task status (To Do, In Progress, Completed)

Dependency-based task sequencing

Timeline view for project milestones

LLM-assisted suggestions for task optimization

Secure authentication with JWT tokens

RESTful API for easy integration with other services

Tech Stack

Backend: Python, Flask

Frontend: HTML, CSS, JavaScript (React optional)

Database: MySQL / SQLite

Authentication: JWT-based secure login

Tools: Postman (API testing), Swagger (API documentation)

Installation

Clone the repository:

git clone https://github.com/username/project-name.git
cd project-name


Create a virtual environment:

python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate


Install dependencies:

pip install -r requirements.txt


Set up the database:

Configure config.py for database credentials

Run migration scripts or create tables manually

Run the Flask server:

python app.py


Open the frontend:

Open index.html in your browser (if standalone)

Or run React frontend if applicable

Usage

Register / Login with your account

Create a new task with details: name, description, and dependencies

Update or mark tasks as completed

View all tasks and timeline to track progress

API Endpoints
Method	Endpoint	Description
GET	/tasks	Retrieve all tasks
POST	/tasks	Create a new task
GET	/tasks/{id}	Retrieve task by ID
PUT	/tasks/{id}	Update task details
DELETE	/tasks/{id}	Delete a task
POST	/auth/register	Register a new user
POST	/auth/login	User login and get JWT token
Project Structure
project/
├─ app.py             # Main Flask app
├─ models.py          # Database models
├─ routes/
│  ├─ task_routes.py  # Task-related API endpoints
│  ├─ auth_routes.py  # Authentication endpoints
├─ services/
│  ├─ task_service.py # Business logic for tasks
├─ utils/
│  ├─ validators.py   # Input validation functions
├─ static/            # CSS, JS, images
├─ templates/         # HTML templates
└─ requirements.txt   # Python dependencies
