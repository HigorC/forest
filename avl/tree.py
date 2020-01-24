from node import Node

root = None

def insert(value):
    global root
    if root is None:
        root = Node(value)
    else:
        insert_with_node(value, root)

def insert_with_node(value, node):
    # if node is None:
    #     return Node(value)
    if value < node.value:
        if node.l_child is None:
            node.l_child = Node(value)
        else:
            insert_with_node(value, node.l_child)
    elif value > node.value:
        if  node.r_child is None:
            node.r_child = Node(value)
        else:
            insert_with_node(value, node.r_child)

insert(10)
insert(5)
insert(3)
insert(7)
insert(1)
insert(4)
insert(6)
insert(8)

insert(15)
insert(12)
insert(17)
insert(11)
insert(13)
insert(16)
insert(18)


print(root)