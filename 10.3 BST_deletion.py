class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def delete(root,target):
    if root is None:
        return None

    if target < root.data:
        root.left = delete(root.left,target)
    elif target > root.data:
        root.right = delete(root.right,target)
    else:
        #case1: no child
        if root.left is None and root.right is None:
            return None
        #case2: only left child
        if root.left is None:
            return root.left

        #case3: two children
        successor = root.right
        while successor.left:
            successor = successor.left

        root.data = successor.data
        root.right = delete(root.right,successor.data)

    return root

root  = Node(50)

root.left = Node(30)
root.right = Node(70)

root.left.left = Node(20)
root.left.right = Node(40)

root.right.left = Node(60)
root.right.right = Node(80)

root = delete(50)
