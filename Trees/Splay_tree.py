class Node:
    def __init__(self, value, parent=None, left_child=None, right_child=None, height=1):
        self.value = value
        self.parent = parent
        self.left_child = left_child
        self.right_child = right_child
        self.height = height


class Splay_Tree:
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
        self.root = self.splay(value, cur_node)
        return cur_node
    
    
    def splay(self, value, cur_node):
        if cur_node != self.root.left_child or cur_node != self.root.right_child and cur_node != self.root: 
            if self.fis_left_child(value, cur_node.parent) == True:
                pass
            elif self.is_right_child(value, cur_node.parent) == True:
                pass
        elif cur_node != self.root:
            pass
    
    
    def find(self, value):
        if self.root == None:
            print("Splay Tree is empty")
        else:
            return self._find(value, self.root)
    
    
    def is_left_child(self, value, cur_node):
        if self.root == None:
            return False
        elif cur_node.left_child.value == value:
            return True
        else:
            return False
    
    
    def is_right_child(self, value, cur_node):
        if self.root == None:
            return False
        elif cur_node.right_child.value == value:
            return True
        else:
            return False
    
    def _find(self, value, cur_node):
        if value < cur_node.value and cur_node.left_child != None:
            return self._find(value, cur_node.left_child)
        elif value > cur_node.value and cur_node.right_child != None:
            return self._find(value, cur_node.right_child)
        elif value == cur_node.value:
            self.up(cur_node)
            return True
        else:
            return False
    
    
    def up(self, cur_node):
        if cur_node.parent.parent == None:
            cur_node = self.zig(cur_node.parent)
        else:
            cur_node = self.zig(cur_node.parent)
            cur_node = self.zig(cur_node.parent)
    
    
    def height(self, cur_node):
        if cur_node != None:
            return cur_node.height
        return 0
    
    
    def fixheight(self, cur_node):
        cur_node.height = max(self.height(cur_node.left_child), self.height(cur_node.right_child)) + 1
    
    
    def zig(self, cur_node):
        if cur_node.parent.left_child.value == cur_node.value:
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
        if cur_node.parent.right_child.value == cur_node.value:
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
    
    
    def zigzig(self, cur_node):
        cur_node = self.zig(cur_node)
        cur_node = self.zig(cur_node)
        return cur_node
    
    
    def zigzag(self, cur_node):
        pass
    
    
    def print_tree_preOrder(self):
        if self.root != None:
            self._print_tree_preOrder(self.root)
        else:
            print("Splay Tree is empty")
    
    
    def _print_tree_preOrder(self, cur_node):
        if cur_node != None:
            print(cur_node.value)
            self._print_tree_preOrder(cur_node.left_child)
            self._print_tree_preOrder(cur_node.right_child)
    



tree = Splay_Tree()
n = int(input())
for i in range(n):
    x = int(input())
    tree.insert(x)

#tree.print_tree_preOrder()
print(tree.find(10))
