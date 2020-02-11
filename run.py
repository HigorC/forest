from utils import converter

# arvore = {
#     'value': 5,
#     'left_child': {
#         'value': 2
#     },
#     'rigth_child': {
#         'value': 10
#     }
# }
#
# print (arvore)

from avl import tree
from utils import converter
import json
tree.insert(2)
tree.insert(1)
tree.insert(3)


a = converter.treeToJson(tree.root, {})
tree.printAvl()

# print(json.dumps(tree.root))