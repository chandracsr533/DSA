class Stack:
    def __init__(self):
        self.stack = []

    def push(self,data):
        self.stack.append(data)

    def pop(self):
        if len(self.stack) == 0:
            print("Stack is empty")
        else:
            return self.stack.pop()

    def peek(self):
        if len(self.stack) == 0:
            print("Stack is empty")
        else:
            return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0
        # if len(self.stack) == 0:
        #     return True
        # else:
        #     return False

stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)

print("Stack:",stack.stack)
print("Top:",stack.peek())
print("Removed:",stack.pop())
print("Is-empty:",stack.is_empty())