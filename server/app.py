from flask import Flask, jsonify, render_template

kitchenroom = {
    'lights':False, 
    'curtains':False, 
    'temp':None
    }

bedroom = {
    'lights':False,
    'curtains':False,
    'temp':None
    }
livingroom = {
    'lights':False, 
    'curtains':False, 
    'temp':None
    }

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')
def index():
    return render_template('index.html')

#########################KITCHENROOM###########################
@app.route('/api/kitchenroom/lights', methods=['GET'])
def lights():
    return jsonify({'lights':kitchenroom['lights']})

@app.route('/api/kitchenroom/curtains', methods=['GET'])
def curtains():
    return jsonify({'curtains':kitchenroom['curtains']})

@app.route('api/bedroom/temp', methods=['GET'])
def temp():
    return jsonify({'temp':kitchenroom['temp']})

#########################BEDROOM###########################
@app.route('/api/bedroom/lights', methods=['GET'])
def lights():
    return jsonify({'lights':bedroom['lights']})

@app.route('/api/bedroom/curtains', methods=['GET'])
def curtains():
    return jsonify({'curtains':bedroom['curtains']})

@app.route('/api/bedroom/temp', methods=['GET'])
def temp():
    return jsonify({'temp':bedroom['temp']})


#########################LIVINGROOM###########################
@app.route('/api/livingroom/lights', methods=['GET'])
def lights():
    return jsonify({'lights':livingroom['lights']})

@app.route('/api/livingroom/curtains', methods=['GET'])
def curtains():
    return jsonify({'curtains':livingroom['curtains']})

@app.route('/api/livingroom/temp', methods=['GET'])
def temp():
    return jsonify({'temp':bedroom['temp']})



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8090)
