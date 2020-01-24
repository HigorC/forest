class Node:
    def __init__(self, value = None, l_child = None, r_child = None):
        self.value = value
        self.l_child = l_child
        self.r_child = r_child 
    
    def __str__(self):
        return '    {}\n    {}\n    {}'.format(self.value, self.l_child, self.r_child)
