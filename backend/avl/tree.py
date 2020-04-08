from backend.avl import Node

class Tree:
    root = None
    log = []

    def __init__(self, values):
        self.log.clear()
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
            self.log.append("Árvore desbalanceada a direita...")
            if node.right_child.getBalancingFactor() > 0:
                print("Realizando rotação simples a esquerda...")
                return self.simple_left_rotation(node)
            else:
                self.log.append("Realizando rotação dupla a esquerda...")
                return self.double_left_rotation(node)
        if node.getBalancingFactor() == -2:
            self.log.append("Árvore desbalanceada a esquerda...")
            if node.left_child.getBalancingFactor() < 0:
                self.log.append("Realizando rotação simples a direita...")
                return self.simple_right_rotation(node)
            else:
                self.log.append("Realizando rotação dupla a direita...")
                return self.double_right_rotation(node)
        return node

    def simple_left_rotation(self, node):
        self.log.append(f'Realizando rotação simples a esquerda entre o nó [{node.value}] e o nó [{node.right_child.value}]')
        aux = node
        node = node.right_child
        aux.right_child = node.left_child
        node.left_child = aux
        return node

    def simple_right_rotation(self, node):
        self.log.append(f'Realizando rotação simples a direita entre o nó [{node.value}] e o nó [{node.left_child.value}]')
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

    def getLog(self):
        return self.log

    def getHeight(self):
        return self.root.getHeight()