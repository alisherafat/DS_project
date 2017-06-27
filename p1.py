from src.stack import Stack


def infix2postfix(infix):
    precedence = {"*": 3, "/": 3, "+": 2, "-": 2, "(": 1}
    stack = Stack()
    output = []

    for token in infix:
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


def postfix2infix(postfix):
    stack = Stack()

    for token in postfix:
        token = token.lower()
        if token in "abcdefghijklmnopqrstuvwxyz":
            stack.push(token)
        else:
            operator = token
            operand1 = stack.pop()
            operand2 = stack.pop()
            stack.push(operand2 + operator + operand1)
    return stack.pop()


def infix2prefix(infix):
    precedence = {"*": 3, "/": 3, "+": 2, "-": 2, "(": 1}
    stack = Stack()

    output = []
    temp = []
    for token in infix:
        if token in "abcdefghijklmnopqrstuvwxyz":
            output.append(token)
        elif token == '(':
            stack.push(token)
        elif token == ')':
            top_of_stack = stack.pop()
            while top_of_stack != '(':
                temp.append(top_of_stack)
                top_of_stack = stack.pop()
            output = temp + output
            temp = []
        else:
            while (not stack.is_empty()) and \
                    (precedence[stack.peek()] >= precedence[token]):
                temp.append(stack.pop())
            output = temp + output
            temp = []
            stack.push(token)
    while not stack.is_empty():
        temp.append(stack.pop())
    output = temp + output
    return ' '.join(output)


def prefix2infix(prefix):
    reverse = prefix[::-1]
    temp = postfix2infix(reverse)
    infix = temp[::-1]
    return infix


print(infix2postfix("(a+b)*c-(d-e)*(f+g)"))
print(infix2prefix("(a+b)*c-(d-e)*(f+g)"))
print(postfix2infix("ab+c*de-fg+*-"))
print(prefix2infix("+*+abd/e+f*ad"))
