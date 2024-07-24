from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

items = [
    {"id": i, "name": f"Элемент {i}", "category": "Category A" if i % 2 == 0 else "Category B", "description": f"Максимально полное описание элемента {i}. Деталей очень много"} for i in range(1, 100)
]

@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

@app.route('/item/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item["id"] == item_id), None)
    if item is None:
        return jsonify({"error": "Item not found"}), 404
    return jsonify(item)

if __name__ == '__main__':
    app.run(debug=True)
