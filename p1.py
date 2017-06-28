from src.stack import Stack
from src.infix import Infix


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


def prefix2infix(prefix):
    reverse = prefix[::-1]
    temp = postfix2infix(reverse)
    infix = temp[::-1]
    return infix


print(Infix("(a+b)*c-(d-e)*(f+g)").get_postfix())
print(Infix("(a+b)*c-(d-e)*(f+g)").get_prefix())
print(postfix2infix("ab+c*de-fg+*-"))
print(prefix2infix("+*+abd/e+f*ad"))
