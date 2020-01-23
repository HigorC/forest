from node import Node

root = None

# a = Node(2)
# c = Node(4)
# e = Node(6)
# g = Node(8)
# b = Node(3, a, c)
# f = Node(7, e, g)
# d = Node(5, b, f)

def insert(value):
    nodeToSet = search(value, root)
    if nodeToSet == None:
        nodeToSet.value = value

def search(value, node):
    if node is None:
        node = Node(value)
        return node
    elif value == node.value:
        return node
    elif value < node.value:
        return search(value, node.l_child)
    elif value > node.value:
        return search(value, node.r_child)


root = insert(1)
root = insert(2)
print(root)