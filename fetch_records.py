from flask import Flask, jsonify
import sqlite3
from flask_cors import CORS


app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
CORS(app)


@app.route('/api/v1/user/<int:user_id>/karma-position', methods=['GET'])
def get_karma_position(user_id):
    conn = sqlite3.connect('mydatabase.db')
    c = conn.cursor()

    # Get all users ordered by karma_score
    c.execute('''
        SELECT users.id, users.karma_score, images.url
        FROM users
        INNER JOIN images ON users.image_id = images.id
        ORDER BY users.karma_score DESC
    ''')
    users = c.fetchall()

    # Find the position of the requested user
    position = next((i for i, user in enumerate(users) if user[0] == user_id), None)

    if position is None:
        return jsonify({'error': 'User not found'}), 404

    # Get the two users above and below the requested user
    if position == 0 or position == 1:
        start = 0
        end = 5

    elif position == len(users) - 2 or position == len(users) - 1:
        start = len(users) - 5
        end = len(users) 
    else:
        start = max(0, position - 2)
        end = min(len(users), position + 3)
    result = users[start:end]

    
    
    # Format the result
    result = [
        {
            'id': user[0],
            'position': i + 1,
            'karma_score': user[1],
            'image_url': user[2]
        }
        for i, user in enumerate(result, start=start)
    ]
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)