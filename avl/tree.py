from avl import Node

class Tree:
    root = None

    def __init__(self, values):
        if values is not None and type(values) is list:
            self.insert_with_array(values)

    def insert(self, value):
        global root
        if self.root is None:
            self.root = Node(value)
        else:
            self.root = self.insert_with_node(value, self.root)

    def insert_with_node(self, value, node):
        if node is None:
            return Node(value)
        elif value < node.value:
            node.left_child = self.insert_with_node(value, node.left_child)
        elif value > node.value:
            node.right_child = self.insert_with_node(value, node.right_child)

        return self.fixBalance(node)

    def insert_with_array(self, values):
        for value in values:
            self.insert(value)

    def fixBalance(self, node):
        if node.getBalancingFactor() == 2:
            print("Árvore desbalanceada a direita...")
            if node.right_child.getBalancingFactor() > 0:
                print("Realizando rotação simples a esquerda...")
                return self.simple_left_rotation(node)
            else:
                print("Realizando rotação dupla a esquerda...")
                return self.double_left_rotation(node)
        if node.getBalancingFactor() == -2:
            print("Árvore desbalanceada a esquerda...")
            if node.left_child.getBalancingFactor() < 0:
                print("Realizando rotação simples a direita...")
                return self.simple_right_rotation(node)
            else:
                print("Realizando rotação dupla a direita...")
                return self.double_right_rotation(node)
        return node

    def simple_left_rotation(self, node):
        aux = node
        node = node.right_child
        aux.right_child = node.left_child
        node.left_child = aux
        return node

    def simple_right_rotation(self, node):
        aux = node
        node = node.left_child
        aux.left_child = node.right_child
        node.right_child = aux
        return node

    def double_left_rotation(self, node):
        node.right_child = self.simple_right_rotation(node.right_child)
        return self.simple_left_rotation(node)

    def double_right_rotation(self, node):
        node.left_child = self.simple_left_rotation(node.left_child)
        return self.simple_right_rotation(node)

    def printAvl(self):
        print("altura", self.root.getHeight())
        print("balanco", self.root.getBalancingFactor())
        print(self.root)

    def inOrdem(self, node):
        if node is not None:
            self.inOrdem(node.left_child)
            print(node.value)
            self.inOrdem(node.right_child)

    def toArrayInOrder(self, node, arrayTree):
        if node is not None:
            arrayTree.append(node.value)
            self.toArrayInOrder(node.left_child, arrayTree)
            self.toArrayInOrder(node.right_child, arrayTree)

        return arrayTree

    def getArrayTree(self):
        return self.toArrayInOrder(self.root, [])

    def getTree(self):
        return self.root

