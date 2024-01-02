# Fake API

## Overview

This is a simple REST API built with Python's Flask framework. It simulates a user management and todo list application, providing endpoints to manage users and tasks.

## Features

User Management:
Retrieve a list of all users.
Retrieve details of a specific user by ID.
Todo List:
Retrieve a list of all tasks.
Retrieve details of a specific task by ID.

## Technologies Used

Python
Flask
Flask-CORS

## Installation

Clone this repository:

```bash
git clone https://github.com/MarkDacurawat/FLASK_FAKEAPI.git
```

Install the required dependencies:

```bash
pip install flask flask-cors
```

## Usage

Start the development server:

```bash
python app.py
```

Access the API endpoints using a REST client or tools like Postman.

## Endpoints

- **GET /users:** Returns a list of all users.
- **GET /users/<user_id>:** Returns details of a specific user.
- **GET /todos:** Returns a list of all tasks.
- **GET /todos/<todo_id>:** Returns details of a specific task.

## Authors

Mark Dacurawat: https://github.com/MarkDacurawat

## Contributing

We welcome contributions! Please follow these steps:

Fork this repository.
Create a new branch for your changes.
Make your changes and commit them.
Push your changes to your fork.
Submit a pull request.

## License

This project is licensed under the MIT License.

## Additional Notes

This API is intended for demonstration purposes only and is not suitable for production use.
The data is currently stored in hardcoded lists and is not persistent.
