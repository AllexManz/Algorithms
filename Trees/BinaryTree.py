class Node:
    def __init__(self, value, parent=None, depth=0):
        self.value = value
        self.parent = parent
        self.left_child = None
        self.right_child = None
        self.depth = depth


class BinaryTree:
    def __init__(self):
        self.root = None
        self.depth = 0

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.insert_(self.root, value)

    def insert_(self, node, value):
        if value >= node.value:
            if node.right_child is None:
                node.right_child = Node(value, parent=node, depth=node.depth + 1)
            else:
                self.insert_(node.right_child, value)
        if value < node.value:
            if node.left_child is None:
                node.left_child = Node(value, parent=node, depth=node.depth + 1)
            else:
                self.insert_(node.left_child, value)

    def find(self, value):
        if self.root is None:
            return None, "There are no elements in the Tree"
        else:
            return self._find(self.root, value)

    def _find(self, node, value):
        if value > node.value:
            if node.right_child is None:
                return None, "Element not found"
            else:
                return self._find(node.right_child, value)
        elif value < node.value:
            if node.left_child is None:
                return None, "Element not found"
            else:
                return self._find(node.left_child, value)
        elif value == node.value:
            return node, "Element Found"

    def print_in_order(self):
        if self.root is not None:
            self.print_in_order_(self.root)
        else:
            print("Tree is Empty")

    def print_in_order_(self, node):
        if node is not None:
            self.print_in_order_(node.left_child)
            print(node.value)
            self.print_in_order_(node.right_child)

    def print_pre_order(self):
        if self.root is not None:
            self.print_pre_order_(self.root)
        else:
            print("Tree is Empty")

    def print_pre_order_(self, node):
        if node is not None:
            print(node.value)
            self.print_pre_order_(node.left_child)
            self.print_pre_order_(node.right_child)

    def print_post_order(self):
        if self.root is not None:
            self.print_post_order_(self.root)
        else:
            print("Tree is Empty")

    def print_post_order_(self, node):
        if node is not None:
            self.print_post_order_(node.left_child)
            self.print_post_order_(node.right_child)
            print(node.value)

    def max(self):
        if self.root is None:
            return "There are no elements in the Tree"
        else:
            return self._max(self.root)

    def _max(self, node):
        if node.right_child is None:
            return node.value
        else:
            return self._max(node.right_child)

    def min(self):
        if self.root is None:
            return "There are no elements in the Tree"
        else:
            return self._min(self.root)

    def _min(self, node):
        if node.left_child is None:
            return node.value
        else:
            return self._min(node.left_child)

    def dependencies(self, value):
        if self.root is None:
            return "There are no elements in the Tree"
        else:
            return self._dependencies(value)

    def _dependencies(self, value):
        node = self.find(value)[0]
        if node is not None:
            print(f"Parent: {node.parent.value}")
            if node.left_child is None:
                print("There is no left child")
            else:
                print(f"Left child: {node.left_child.value}")
            if node.right_child is None:
                print("There is no right child")
            else:
                print(f"Right child: {node.right_child.value}")
            print(f"Depth: {node.depth}")
        else:
            print("There is no element with this key, try another")


BT = BinaryTree()
while True:
    string = input()
    if string == 'stop':
        break
    elif string == '':
        print("The command must contain symbols, but the empty one was given")
    elif string == 'max':
        print(f"Max Element: {BT.max()}")
    elif string == 'min':
        print(f"Min Element: {BT.min()}")
    elif string == 'inorder':
        BT.print_in_order()
    elif string == 'preorder':
        BT.print_pre_order()
    elif string == 'postorder':
        BT.print_post_order()
    elif string == 'help':
        file = open('documentation.txt')
        for line in file:
            print(line.strip())
    elif list(string.split())[0] == 'inf':
        BT.dependencies(int(list(string.split())[1]))
    elif list(string.split())[0] == 'find':
        element = BT.find(int(list(string.split())[1]))[1]
        print(element)
    else:
        node_value = int(string)
        BT.insert(node_value)
        print(f"Node {node_value} added to the Tree")
