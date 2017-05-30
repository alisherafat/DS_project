from src.stack import Stack


def infix2postfix(infix_str):
    precedence = {"*": 3, "/": 3, "+": 2, "-": 2, "(": 1}
    stack = Stack()
    output = []
    tokens = infix_str.split()

    for token in tokens:
        token = token.lower()
        # check for operand
        if token in "abcdefghijklmnopqrstuvwxyz":
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

    return " ".join(output)


print(infix2postfix("a * b + c * d"))
print(infix2postfix("( a + b ) * c - ( d - e ) * ( f + g )"))
print(infix2postfix("a + b * ( c / ( d + e ) ) * f"))
