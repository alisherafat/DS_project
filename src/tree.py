from src.infix import Infix
from src.node import Node
from src.stack import Stack

calculate = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b,
}


def is_operator(char):
    if char in ['+', '-', '*', '/', '^']:
        return True
    return False


class ExpressionTree:
    def __init__(self, infix):
        self.infix = infix
        self.postfix = Infix(infix).get_postfix()
        self.root = None
        stack = Stack()
        for token in self.postfix:
            if not is_operator(token):
                t = Node(token)
                stack.push(t)
            else:
                t = Node(token)
                t1 = stack.pop()
                t2 = stack.pop()
                t.right = t1
                t.left = t2
                stack.push(t)
        self.root = stack.pop()

    def inorder(self, node):
        if node is not None:
            self.inorder(node.left)
            print(node.value, end='')
            self.inorder(node.right)

    def pre_order(self, node):
        if node is not None:
            print(node.value, end='')
            self.pre_order(node.left)
            self.pre_order(node.right)

    def post_order(self, node):
        if node is not None:
            self.post_order(node.left)
            self.post_order(node.right)
            print(node.value, end='')

    def evaluate(self, node):
        if not node:
            return 0

        if is_operator(node.value):
            left = self.evaluate(node.left)
            right = self.evaluate(node.right)
            return calculate[node.value](left, right)

        return int(node.value)
