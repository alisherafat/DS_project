class Stack:
    """
    implementation of stack using an array.
    end of the list will hold the top element of the stack.
    """

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    # returns last item in the list
    def peek(self):
        return self.items[len(self.items) - 1]

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
