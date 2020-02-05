class Node:
    def __init__(self, value = None, left_child = None, right_child = None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child 

    def __str__(self):
        return '    {}\n    {}\n    {}'.format(self.value, self.left_child, self.right_child)

    def getHeight(self):
        if self is not None:
            heightLeftChild = self.left_child.getHeight() if self.left_child is not None else 0
            heightRightChild = self.right_child.getHeight() if self.right_child is not None else 0

            if self.left_child is None and self.right_child is None:
                return 1

            return heightLeftChild + 1 if heightLeftChild > heightRightChild else heightRightChild + 1
        return 0

    def getBalancingFactor(self):
        heightLeftChild = self.left_child.getHeight() if self.left_child is not None else 0
        heightRightChild = self.right_child.getHeight() if self.right_child is not None else 0

        return heightRightChild - heightLeftChild
