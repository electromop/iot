from flask import Flask, jsonify, render_template

def bool_to_str(condition):
    if type(condition) == bool:
        if condition == False:
            return 'disabled'
        else:
            return 'enabled'
    else:
        return condition

kitchenroom = {
    'lights':False, 
    'curtains':False, 
    'temp':1
    }

bedroom = {
    'lights':False,
    'curtains':False,
    'temp':0
    }
livingroom = {
    'lights':False, 
    'curtains':False, 
    'temp': 0
    }

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')
def index():
    return render_template(
        'index.html',
        livingroom_curt_var=bool_to_str(livingroom['curtains']),
        livingroom_lights_var=bool_to_str(livingroom['lights']),
        livingroom_temp_var=livingroom['temp'],

        bedroom_curt_var=bool_to_str(bedroom['curtains']),
        bedroom_lights_var=bool_to_str(bedroom['lights']),
        bedroom_temp_var=bedroom['temp'],

        kitchenroom_curt_var=bool_to_str(kitchenroom['curtains']),
        kitchenroom_lights_var=bool_to_str(kitchenroom['lights']),
        kitchenroom_temp_var=kitchenroom['temp'],
    )

#################### ROOM MODULE CONDITION #######################
@app.route('/api/<room>/<module>')
def room_module_cond(module, room):
    try:
        return jsonify({f'{module}':globals()[room][f'{module}']})
    except KeyError:
        return 'Name Error, there is no room or module with such name'

@app.route('/api/<room>')
def room_cond(room):
    try:
        return jsonify(globals()[room])
    except KeyError:
        return 'Name Error, there is no room with such name'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8090)
