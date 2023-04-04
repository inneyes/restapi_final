from flask import Flask, request, jsonify
import json

app = Flask(__name__)

items = [
    {"name": "strawberry short cake", "category": 50, "price": 20, "instock": 60},
    {"name": "banoffee", "category": 30, "price": 150, "instock": 25},
    {"name": "apple pie", "category": 90, "price": 90, "instock": 20},
    {"name": "red velvet", "category": 40, "price": 50, "instock": 30},
    {"name": "cookies", "category": 30, "price": 60, "instock": 40},
]
def _find_next_name(name):
    data = [x for x in items if x['name'] == name]
    return data

print(_find_next_name("strawberry short cake"))



#GET ITEM
@app.route('/item', methods=["GET"])
def get_item():
    return jsonify(items)

# GET item by name
@app.route('/item/<name>', methods=["GET"])
def get_items_name(name):
    data = _find_next_name(name)
    return jsonify(data)

#
@app.route('/post_item', methods=["POST"])
def post_items():
    name = request.form.get('name')
    category = request.form.get('category')
    price = request.form.get('price')
    instock = request.form.get('instock')

    new_data = {
        "name": name,
        "category": category,
        "price": price,
        "instock":instock,
        
    }

    if (_find_next_name(name) == name):
        return {"error": "Bad Request"}, name
    else:
        items.append(new_data)
        return jsonify(items)

@app.route('/update_item/<name>', methods=["PUT"])
def update_item(name):
    
    global items
    category = request.form.get('category')
    price = request.form.get('price')
    instock = request.form.get('instock')

    

    for items in items:
        if name == items["name"]:
            items["category"] = int(category)
            items["price"] = int(price)
            items["instock"] = int(instock)
            return jsonify(items)

    else:
        return "Error", 404

@app.route('/delete_item/<name>', methods=["DELETE"])
def delete_item(name: str):

    data = _find_next_name(name)
    if not data:
        return {"error": "Item not found"}, 404
    else:
        items.remove(data[0])
        return "Item deleted successfully", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)