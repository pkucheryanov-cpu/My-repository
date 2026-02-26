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

@app.route('/health')
def health():
    return jsonify({"status": "healthy"})

@app.route('/api/environment')
def get_environment():
    return jsonify({
        "app": "ShopEasy",
        "env": "development",
        "node": "20.x",
        "developer": "p.kucheryanov"
    })

@app.route('/api/config')
def get_config():
    return jsonify({
        "app": "ShopEasy",
        "debug": False,
        "locale": "uk-UA",
        "owner": "p.kucheryanov"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

