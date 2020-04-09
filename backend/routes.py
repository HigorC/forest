from flask import Blueprint, request, jsonify
from backend.avl import Tree
import jsons

routes_blueprint = Blueprint('routes_blueprint', __name__)

@routes_blueprint.route('/insert/<valueToInsert>', methods=['POST'])
def insert(valueToInsert):
    requestJson = request.get_json()
    actualTreeArray = requestJson.get('tree')
    typeTree = requestJson.get('type')

    tree = None

    if typeTree == 'avl':
        tree = Tree(actualTreeArray)

    tree.insert(int(valueToInsert))

    result = {
        'tree': jsons.dump(tree.getTree()),
        'height': tree.getHeight(),
        'log': tree.getLog()
    }

    return jsonify(result), 200, {'Content-Type': 'application/json'}