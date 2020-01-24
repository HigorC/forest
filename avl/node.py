class Node:
    def __init__(self, value = None, left_child = None, right_child = None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child 
        self.balancing_factor = 0
        
    def __str__(self):
        return '    {}\n    {}\n    {}'.format(self.value, self.left_child, self.right_child)
