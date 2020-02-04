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

    return calculate_balancing_factor(node)

def simple_left_rotation(node):
    aux = node
    node = node.right_child
    aux.right_child = node.left_child
    aux.balancing_factor -=2
    node.left_child = aux
    node.balancing_factor -=1
    return node

def calculate_balancing_factor_from_root():
    global root
    root = calculate_balancing_factor(root)

def calculate_balancing_factor(node):
    if node is not None:
        calculate_balancing_factor(node.left_child)
        calculate_balancing_factor(node.right_child)
    
        if node.left_child is None and node.right_child is None:
            node.balancing_factor = 0
        else:
            left_tree_abs_balance = abs(node.left_child.balancing_factor) + 1 if node.left_child is not None else 0
            right_tree__abs_balance = abs(node.right_child.balancing_factor) + 1 if node.right_child is not None else 0

            node.balancing_factor = right_tree__abs_balance - left_tree_abs_balance

            if node.balancing_factor is 2:
                node = simple_left_rotation(node)
    return node

def printAvl():
    print(root)

def inOrdem(node):
    if node is not None:
        inOrdem(node.left_child)
        print (node.value)
        inOrdem(node.right_child)
