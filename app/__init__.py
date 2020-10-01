from flask import Flask, jsonify

app = Flask(__name__)
app.config['SECRET_KEY'] = 'soroush'


@app.route('/')
def health():
    return jsonify({'MESSAGE': 'This is the health message.'})
