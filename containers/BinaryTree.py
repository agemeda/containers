'''
'''


class Node():
    '''
    You do not have to implement anything within this class.
    Given a node t, you can visualize the node by running str(t)
    in the python interpreter.
    This is a key method to perform debugging,
    so you should get familiar with how to visualize these strings.
    '''

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left    # NOTE: left should always be a Node
        self.right = right  # NOTE: right should always be a Node

    def __str__(self):
        ret = '('
        ret += str(self.value)
        ret += ' - '
        if self.left:
            ret += str(self.left)
            ret += ' '
        ret += '- '
        if self.right:
            ret += str(self.right)
            ret += ' '
        ret += ')'
        return ret


class BinaryTree():
    '''
    '''

    def __init__(self, root=None):
        '''
        '''
        if root:
            self.root = Node(root)
        else:
            self.root = None

    def __str__(self):
        '''
        We can visualize a tree by visualizing its root node.
        '''
        return str(self.root)

    def print_tree(self, traversal_type):
        '''
        '''
        if traversal_type == 'preorder':
            return self.preorder_print(self.root, '')
        elif traversal_type == 'inorder':
            return self.inorder_print(self.root, '')
        elif traversal_type == 'postorder':
            return self.postorder_print(self.root, '')
        else:
            raise ValueError('Traversal type is not supported.')

    def preorder_print(self, start, traversal):
        '''
        Prints the nodes using a preorder traversal.
        '''
        if start:
            traversal += str(start.value) + '-'
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

    def inorder_print(self, start, traversal):
        '''
        Prints the nodes using a inorder traversal.
        '''
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += str(start.value) + '-'
            traversal = self.inorder_print(start.right, traversal)
        return traversal

    def postorder_print(self, start, traversal):
        '''
        Prints the nodes using a postorder traversal.
        '''
        if start:
            traversal = self.postorder_print(start.left, traversal)
            traversal = self.postorder_print(start.right, traversal)
            traversal += str(start.value) + '-'
        return traversal

    def to_list(self, traversal_type):
        '''
        FIXME:
        Implement this function
        '''
        if traversal_type == 'inorder':
            return self.inorder(self.root, [])
        if traversal_type == 'preorder':
            return self.preorder(self.root, [])
        if traversal_type == 'postorder':
            return self.postorder(self.root, [])

    def preorder(self, start, traversal):
        '''
        FIXME:
        Implement this function by modifying the _print functions above.
        '''
        if start:
            traversal.append(start.value)
            traversal = self.preorder(start.left, traversal)
            traversal = self.preorder(start.right, traversal)
        return traversal

    def inorder(self, start, traversal):
        '''
        FIXME:
        Implement this function by modifying the _print functions above.
        '''
        if start:
            traversal = self.inorder(start.left, traversal)
            traversal.append(start.value)
            traversal = self.inorder(start.right, traversal)
        return traversal

    def postorder(self, start, traversal):
        '''
        FIXME:
        Implement this function by modifying the _print functions above.
        '''
        if start:
            traversal = self.postorder(start.left, traversal)
            traversal = self.postorder(start.right, traversal)
            traversal.append(start.value)
        return traversal

    def __len__(self):
        '''
        Returns the number of elements contained in the tree.
        Recall that `tree.__len__()` will desugar to `size(len)`.
        '''
        return BinaryTree.__len__helper(self.root)

    @staticmethod
    def __len__helper(node):
        '''
        FIXME:
        Implement this function.
        '''
        if node is None:
            return 0
        if node:
            val = 1
            if node.left:
                val += BinaryTree.__len__helper(node.left)
            if node.right:
                val += BinaryTree.__len__helper(node.right)
        return val

    def height(self):
        '''
        '''
        return BinaryTree._height(self.root)

    @staticmethod
    def _height(node):
        '''
        FIXME:
        Implement this function.
        '''
        if not node:
            return -1

        lefth = BinaryTree._height(node.left)
        righth = BinaryTree._height(node.right)
        return 1 + max(lefth, righth)
