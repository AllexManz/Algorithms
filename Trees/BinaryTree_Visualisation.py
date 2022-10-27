from tkinter import Tk, Canvas, Entry, Button, messagebox


class Node:
    def __init__(self, canvas, value, x, y, depth, parentx=None, parenty=None):
        self.value = value
        self.depth = depth
        self.left_child = None
        self.right_child = None
        self.x = x
        self.y = y
        self.px = parentx
        self.py = parenty
        self.fill = 'yellow'
        self.outline = 'black'
        self.width = 1
        self.canvas = canvas
        self.radius = 15
        self.id = self.canvas.create_oval(x - self.radius, y - self.radius,
                                          x + self.radius, y + self.radius,
                                          outline=self.outline, fill=self.fill,
                                          width=self.width)
        self.text = self.canvas.create_text(x, y, text=str(self.value))
        if self.px is not None and self.py is not None:
            self.line = self.canvas.create_line(self.x, self.y,
                                                self.px, self.py,
                                                fill='black',
                                                width=2)
            self.canvas.lower(self.line)


class BinaryTree:
    def __init__(self, canvas):
        self.canvas = canvas
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(self.canvas, value, 500, 40, 1)
        else:
            self.insert_(self.root, value)

    def insert_(self, node, value):
        if value >= node.value:
            if node.right_child is None:
                node.right_child = Node(self.canvas, value, node.x + 400 // (node.depth * 3), node.y + 75, node.depth + 1, node.x, node.y)
            else:
                self.insert_(node.right_child, value)
        if value < node.value:
            if node.left_child is None:
                node.left_child = Node(self.canvas, value, node.x - 400 // (node.depth * 3), node.y + 75, node.depth + 1, node.x, node.y)
            else:
                self.insert_(node.left_child, value)

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


def GUI_insert(entr):
    n = entr.get()
    if not n.isdigit():
        print('Wrong input')
    else:
        n = int(n)
        BT.insert(n)
        print(n)


tk = Tk()
print(chr(27) + "[2J")
tk.title("Graph")
tk.geometry('1000x500')
cv = Canvas(tk, width=1300, height=700, bg="white")
cv.pack()
BT = BinaryTree(cv)
entr = Entry(tk, width=5)
entr.place(x=10, y=10)
but = Button(tk, text='Insert', command=lambda: GUI_insert(entr))
but.place(x=40, y=10)


tk.resizable(False, False)
tk.mainloop()
