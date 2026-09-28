from collections import deque

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

root = Node(10)

root.left = Node(20)
root.right = Node(30)

root.left.left = Node(40)
root.left.right = Node(50)

def level_order(root):
    if root is None:
        return

    queue = deque()
    queue.append(root)

    while queue:
        current = queue.popleft()

        print(current.data)

        if current.left:
            queue.append(current.left)

        if current.right:
            queue.append(current.right)

level_order(root)