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

    if node.getBalancingFactor() == 2:
        print("Árvore desbalanceada...")
        print("Realizando rotação simples a esquerda...")
        return simple_left_rotation(node)
    return node

def simple_left_rotation(node):
    aux = node
    node = node.right_child
    aux.right_child = node.left_child
    aux.balancing_factor -=2
    node.left_child = aux
    node.balancing_factor -=1
    return node

def printAvl():
    print(root)

def teste():
    print("altura", root.getHeight())
    print("balanco", root.getBalancingFactor())

def inOrdem(node):
    if node is not None:
        inOrdem(node.left_child)
        print (node.value)
        inOrdem(node.right_child)
