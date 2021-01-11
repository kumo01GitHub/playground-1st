from flask import Blueprint, jsonify, request, render_template

# DB
stores = [
    {
        'name': 'my_store',
        'items': [
            {
            'name': 'chocolate',
            'price': 120
            }
        ]
    }
]

app = Blueprint('stores', __name__)

# GET /store/<string:name>
@app.route('/stores/<string:name>') # 'http://127.0.0.1:5000/store/some_name'
def get_store(name):
    for store in stores:
        if store["name"] == name:
            return jsonify(store)
    return jsonify({"message": "no store named {} found.".format(name)})

# POST /store data: {name:}
@app.route('/stores', methods=['POST'])
def create_store():
    request_data = request.get_json()
    store = next(filter(lambda x: x["name"]==request_data["name"], stores), None)
    if store != None:
        return jsonify({"message": "store named {} already exist.".format(request_data["name"])})
    else:
        new_store = {
            "name": request_data["name"],
            "items": request_data["items"]
        }
        stores.append(new_store)
        return jsonify({"message": "{} store is added.".format(request_data["name"])})

# PUT /store data: {name:}
@app.route('/stores/<string:name>', methods=['PUT'])
def update_store(name):
    request_data = request.get_json()
    store = next(filter(lambda x: x["name"] == name, stores), None)
    if store == None:
        return jsonify({"message": "no store named {} found.".format(name)})
    else:
        store["items"] = request_data["items"]
        return jsonify({"message": "{} is updated.".format(name)})

# DELETE /stores/<string:name>
@app.route('/stores/<string:name>', methods=['DELETE'])
def delete_store(name):
    global stores
    stores = list(filter(lambda x: x["name"] != name, stores))
    return jsonify({"message": "Delete store named {}".format(name)})

# GET /stores
@app.route('/stores')
def get_stores():
    return jsonify({'stores': stores})
