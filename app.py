from flask import Flask,jsonify,request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

users_data = [
    {
        'id': 1,
        'username': 'user1',
        'email': 'user1@example.com',
        'age': 25
    },
    {
        'id': 2,
        'username': 'user2',
        'email': 'user2@example.com',
        'age': 30
    },
    {
        'id': 3,
        'username': 'user3',
        'email': 'user3@example.com',
        'age': 22
    },
    {
        'id': 4,
        'username': 'user4',
        'email': 'user4@example.com',
        'age': 28
    },
    {
        'id': 5,
        'username': 'user5',
        'email': 'user5@example.com',
        'age': 35
    },
    {
        'id': 6,
        'username': 'user6',
        'email': 'user6@example.com',
        'age': 26
    },
    {
        'id': 7,
        'username': 'user7',
        'email': 'user7@example.com',
        'age': 31
    },
    {
        'id': 8,
        'username': 'user8',
        'email': 'user8@example.com',
        'age': 24
    },
    {
        'id': 9,
        'username': 'user9',
        'email': 'user9@example.com',
        'age': 29
    },
    {
        'id': 10,
        'username': 'user10',
        'email': 'user10@example.com',
        'age': 27
    },
    {
        'id': 11,
        'username': 'user11',
        'email': 'user11@example.com',
        'age': 33
    },
    {
        'id': 12,
        'username': 'user12',
        'email': 'user12@example.com',
        'age': 23
    },
    {
        'id': 13,
        'username': 'user13',
        'email': 'user13@example.com',
        'age': 32
    },
    {
        'id': 14,
        'username': 'user14',
        'email': 'user14@example.com',
        'age': 28
    },
    {
        'id': 15,
        'username': 'user15',
        'email': 'user15@example.com',
        'age': 26
    },
    {
        'id': 16,
        'username': 'user16',
        'email': 'user16@example.com',
        'age': 29
    },
    {
        'id': 17,
        'username': 'user17',
        'email': 'user17@example.com',
        'age': 34
    },
    {
        'id': 18,
        'username': 'user18',
        'email': 'user18@example.com',
        'age': 31
    },
    {
        'id': 19,
        'username': 'user19',
        'email': 'user19@example.com',
        'age': 27
    },
    {
        'id': 20,
        'username': 'user20',
        'email': 'user20@example.com',
        'age': 25
    }
]

todos = [
    {"id": 1, "task": "Complete homework assignment"},
    {"id": 2, "task": "Go for a 30-minute walk"},
    {"id": 3, "task": "Read a chapter of a book"},
    {"id": 4, "task": "Write in a journal for 10 minutes"},
    {"id": 5, "task": "Prepare a healthy lunch"},
    {"id": 6, "task": "Call a friend or family member"},
    {"id": 7, "task": "Learn a new programming concept"},
    {"id": 8, "task": "Organize your desk or workspace"},
    {"id": 9, "task": "Practice mindfulness meditation for 15 minutes"},
    {"id": 10, "task": "Plan and set goals for the week"},
    {"id": 11, "task": "Research a topic of interest"},
    {"id": 12, "task": "Try a new recipe for dinner"},
    {"id": 13, "task": "Do a quick workout or stretch"},
    {"id": 14, "task": "Listen to a podcast or audiobook"},
    {"id": 15, "task": "Take a break and relax for 20 minutes"},
    {"id": 16, "task": "Learn a new language phrase"},
    {"id": 17, "task": "Write a thank-you note to someone"},
    {"id": 18, "task": "Watch a tutorial on a new skill"},
    {"id": 19, "task": "Volunteer for a community service"},
    {"id": 20, "task": "Create a budget for the month"}
]

@app.route('/')
def home():
    return jsonify({
        "title": "FAKE API"
    })

@app.route('/users')
def get_users():
    return jsonify(users_data)

@app.route('/users/<int:userid>')
def get_user(userid):
    for user in users_data:
        if user['id'] == userid:
            return jsonify(user)
    
    return jsonify({'error': 'User not found'}), 404

@app.route('/todos')
def get_todos():
    return jsonify(todos)

@app.route('/todos/<int:todoid>')
def get_todo(todoid):
    for todo in todos:
        if todo['id'] == todoid:
            return jsonify(todo)
    
    return jsonify({'error': 'User not found'}), 404

@app.errorhandler(404)
def page_not_found(e):
    return jsonify({
        "error": "404 not found"
    }), 404

if __name__ == "__main__":
    app.run(debug=True)