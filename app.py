from threading import Thread

from flask import Flask, jsonify, make_response, request
from response import highlight_words

app = Flask(__name__)


@app.route('/')
def sentiment_analysis():
    """"method that outputs a response"""
    if request.method == 'GET':
        text = request.args.get('text')
        return highlight_words(text)
    return make_response(jsonify({'error': 'sorry! unable to parse', 'status_code': 200}), 200)


# We only need this for local development.
if __name__ == '__main__':
    app.run()
