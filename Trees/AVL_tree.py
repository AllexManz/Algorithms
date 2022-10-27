class Node:
    def __init__(self, value, parent = None, left_child = None, right_child = None, height = 1):
        self.value = value
        self.parent = parent
        self.left_child = left_child
        self.right_child = right_child
        self.height = height


class AVL_Tree:
    def __init__(self):
        self.root = None
    
    
    def insert(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            self.insert2(value, self.root)
            
            
    def insert2(self, value, cur_node):
        if value < cur_node.value:
            if cur_node.left_child == None:
                cur_node.left_child = Node(value, parent = cur_node)
            else:
                cur_node.left_child = self.insert2(value, cur_node.left_child)
        elif value > cur_node.value:
            if cur_node.right_child == None:
                cur_node.right_child = Node(value, parent = cur_node)
            else:
                cur_node.right_child = self.insert2(value, cur_node.right_child)
        else:
            print('Node is exist')
        cur_node = self.balance(cur_node)
        return cur_node
        
    
    def height(self, cur_node):
        if cur_node != None:
            return cur_node.height
        return 0
    
    
    def fixheight(self, cur_node):
        cur_node.height = max(self.height(cur_node.left_child), self.height(cur_node.right_child)) + 1
        
    
    def R_rotate(self, cur_node):
        q = cur_node.left_child
        cur_node.left_child = q.right_child
        q.right_child = cur_node
        q.parent = cur_node.parent
        cur_node.parent = q
        if q.parent == None:
            self.root = q
        self.fixheight(cur_node)
        self.fixheight(q)
        return q
    
    
    def L_rotate(self, cur_node):
        p = cur_node.right_child
        cur_node.right_child = p.left_child
        p.left_child = cur_node
        p.parent = cur_node.parent
        cur_node.parent = p
        if p.parent == None:
            self.root = p
        self.fixheight(cur_node)
        self.fixheight(p)
        return p
    
    
    def balance(self, cur_node):
        self.fixheight(cur_node)
        if self.difference(cur_node) == 2:
            if self.difference(cur_node.right_child) < 0:
                cur_node.right_child = self.R_rotate(cur_node.right_child)
            return self.L_rotate(cur_node)
        if self.difference(cur_node) == -2:
            if self.difference(cur_node.left_child) > 0:
                cur_node.left_child = self.L_rotate(cur_node.left_child)
            return self.R_rotate(cur_node)
        return cur_node
    
    
    def difference(self, cur_node):
        return self.height(cur_node.right_child) - self.height(cur_node.left_child)
    
    
    def print_tree_preOrder(self):
        if self.root != None:
            self._print_tree_preOrder(self.root)
        else:
            print('Binary Search Tree is empty')
    
    
    def _print_tree_preOrder(self, cur_node):
        if cur_node != None:
            print(cur_node.value)
            self._print_tree_preOrder(cur_node.left_child)
            self._print_tree_preOrder(cur_node.right_child)
        
            
n = int(input())

avl = AVL_Tree()
for i in range(n):
    x = int(input())
    avl.insert(x)

avl.print_tree_preOrder()
