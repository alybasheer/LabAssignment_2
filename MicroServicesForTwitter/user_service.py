from flask import Flask, jsonify, request

app = Flask(__name__)

# Dummy user data
users = [{"id": 1, "name": "Ali"}, {"id": 2, "name": "Ahmed"}]

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    user = {"id": len(users) + 1, "name": data['name']}
    users.append(user)
    return jsonify(user), 201

if __name__ == '__main__':
    app.run(port=5001)
