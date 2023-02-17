from flask import Flask, jsonify, render_template, request, redirect, url_for
from dataclasses import dataclass

def bool_to_str(condition):
    if type(condition) == bool:
        if condition == False:
            return 'disabled'
        else:
            return 'enabled'
    else:
        return condition

def rev_bool(cond):
    return not cond

@dataclass
class roomCond:
    lights : bool = False
    curtains: bool = False
    temp: float = False       

kitchenroom = roomCond
bedroom = roomCond
livingroom = roomCond
livingroom.curtains = True
print(livingroom())

str_err = 'Name Error, there is no room or module with such name'

# app = Flask(__name__, template_folder='templates', static_folder='static')

# @app.route('/')
# def index():
#     return render_template(
#         'index.html',
#         livingroom_curt_var = livingroom.curtains,
#         livingroom_lights_var = livingroom.lights,
#         livingroom_temp_var=livingroom['temp'],

#         bedroom_curt_var=bool_to_str(bedroom['curtains']),
#         bedroom_lights_var=bool_to_str(bedroom['lights']),
#         bedroom_temp_var=bedroom['temp'],

#         kitchenroom_curt_var=bool_to_str(kitchenroom['curtains']),
#         kitchenroom_lights_var=bool_to_str(kitchenroom['lights']),
#         kitchenroom_temp_var=kitchenroom['temp'],
#     )

# #################### ROOM MODULE CONDITION #######################
# @app.route('/api/<room>/<module>', methods=['GET', 'PUT'])
# def get_module_cond(module, room):
#     if request.method == 'POST':
#         try:
#             if request.form.get('action1') == 'VALUE1':
#                 globals()[room][f'{module}'] = rev_bool(globals()[room][f'{module}'])
#         except KeyError:
#             return str_err
#     else:
#         try:
#             return jsonify({f'{module}':globals()[room][f'{module}']})
#         except KeyError:
#             return str_err

# @app.route('/api/<room>', methods=['GET'])
# def get_room_cond(room):
#     try:
#         return jsonify(globals()[room])
#     except KeyError:
#         return 'Name Error, there is no room with such name'

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=8090)
