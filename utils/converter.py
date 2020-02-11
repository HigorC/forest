from avl import node

def jsonToTree(json):
    pass;

def treeToJson(node, result):
    if node is not None:
        result['value'] = node.value
    if node.left_child is not None:
        result['left_child'] = treeToJson(node.left_child, result)
    if node.right_child is not None:
        result['right_child'] = treeToJson(node.right_child, result)
    return result