from flask import Flask, jsonify, request

app = Flask(__name__)

# Dummy tweet data
tweets = [{"id": 1, "user_id": 1, "content": "Hello, world!"}]

@app.route('/tweets', methods=['GET'])
def get_tweets():
    return jsonify(tweets)

@app.route('/tweets', methods=['POST'])
def post_tweet():
    data = request.json
    tweet = {"id": len(tweets) + 1, "user_id": data['user_id'], "content": data['content']}
    tweets.append(tweet)
    return jsonify(tweet), 201

if __name__ == '__main__':
    app.run(port=5002)
