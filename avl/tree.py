from node import Node

root = None

def insert(value):
    global root
    if root is None:
        root = Node(value)
    else:
        root = insert_with_node(value, root)

def insert_with_node(value, node):
    if node is None:
        return Node(value)
    elif value < node.value:
        node.left_child = insert_with_node(value, node.left_child)
    elif value > node.value:
        node.right_child = insert_with_node(value, node.right_child)

    return fixBalance(node)

def fixBalance(node):
    if node.getBalancingFactor() == 2:
        print("Árvore desbalanceada a direita...")
        if node.right_child.getBalancingFactor() > 0:
            print("Realizando rotação simples a esquerda...")
            return simple_left_rotation(node)
        else:
            print("Realizando rotação dupla a esquerda...")
            return double_left_rotation(node)
    if node.getBalancingFactor() == -2:
        print("Árvore desbalanceada a esquerda...")
        if node.left_child.getBalancingFactor() < 0:
            print("Realizando rotação simples a direita...")
            return simple_right_rotation(node)
        else:
            print("Realizando rotação dupla a direita...")
            return double_right_rotation(node)
    return node

def simple_left_rotation(node):
    aux = node
    node = node.right_child
    aux.right_child = node.left_child
    node.left_child = aux
    return node

def simple_right_rotation(node):
    aux = node
    node = node.left_child
    aux.left_child = node.right_child
    node.right_child = aux
    return node

def double_left_rotation(node):
    node.right_child = simple_right_rotation(node.right_child)
    return simple_left_rotation(node)

def double_right_rotation(node):
    node.left_child = simple_left_rotation(node.left_child)
    return simple_right_rotation(node)

def printAvl():
    print("altura", root.getHeight())
    print("balanco", root.getBalancingFactor())
    print(root)

def inOrdem(node):
    if node is not None:
        inOrdem(node.left_child)
        print (node.value)
        inOrdem(node.right_child)
