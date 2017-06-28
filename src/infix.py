from .stack import Stack


class Infix:
    def __init__(self, infix):
        self.infix = infix

    def get_postfix(self):
        precedence = {"*": 3, "/": 3, "+": 2, "-": 2, "(": 1}
        stack = Stack()
        output = []

        for token in self.infix:
            # check for operand
            if token in "abcdefghijklmnopqrstuvwxyz" or token in "0123456789":
                output.append(token)
            elif token == '(':
                stack.push(token)
            elif token == ')':
                top_token = stack.pop()
                while top_token != '(':
                    output.append(top_token)
                    top_token = stack.pop()
            else:
                while (not stack.is_empty()) and \
                        (precedence[stack.peek()] >= precedence[token]):
                    output.append(stack.pop())
                stack.push(token)

        while not stack.is_empty():
            output.append(stack.pop())

        return "".join(output)

    def get_prefix(self):
        precedence = {"*": 3, "/": 3, "+": 2, "-": 2, "(": 1}
        stack = Stack()

        output = []
        for token in self.infix:
            if token in "abcdefghijklmnopqrstuvwxyz":
                output.append(token)
            elif token == '(':
                stack.push(token)
            elif token == ')':
                top_of_stack = stack.pop()
                while top_of_stack != '(':
                    output.append(top_of_stack)
                    top_of_stack = stack.pop()
            else:
                while (not stack.is_empty()) and \
                        (precedence[stack.peek()] >= precedence[token]):
                    output.append(stack.pop())
                stack.push(token)
        while not stack.is_empty():
            output.append(stack.pop())
        return ' '.join(output)
