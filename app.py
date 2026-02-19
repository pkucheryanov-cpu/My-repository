from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return jsonify({"message": "Hello, DevOps!"})

@app.route('/info')
def info():
    return jsonify({
        "version": "1.0.0",
        "author": "Павло"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
