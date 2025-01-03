from flask import Flask, jsonify, request

app = Flask(__name__)

notifications = []

@app.route('/notifications', methods=['POST'])
def send_notification():
    data = request.json
    notification = {"user_id": data['user_id'], "message": data['message']}
    notifications.append(notification)
    return jsonify({"status": "Notification sent", "notification": notification}), 200

if __name__ == '__main__':
    app.run(port=5003)
