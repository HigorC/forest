from flask import Blueprint, request
from avl import Tree

routes_blueprint = Blueprint('routes_blueprint', __name__)

@routes_blueprint.route('/avl/insert/<valueToInsert>', methods=['POST'])
def insert(valueToInsert):
    actualTreeArray = request.get_json()

    avlTree = Tree(actualTreeArray)

    avlTree.insert(int(valueToInsert))

    return str(avlTree.getArrayTree())
