from flask import Flask, jsonify, render_template

conditions = {'curtains': False}

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/curtains_stat', methods=['GET'])
def curtains():
    return jsonify({'curtains':conditions['curtains']})

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)
