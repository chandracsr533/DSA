class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def search(root,target):
    if root is None:
        return False

    if root.data == target:
        return True
    
    if target < root.data:
        return search(root.left,target)
    else:
        return search(root.right,target)
    
# def search(root, target):
#     current = root
#     while current:
#         if current.data == target:
#             return True
#         elif target < current.data:
#             current = current.left
#         else:
#             current = current.right
#     return False


root = Node(50)

root.left = Node(30)
root.right = Node(70)

root.left.left = Node(20)
root.left.right = Node(40)

root.right.left = Node(60)
root.right.right = Node(80)


target = 60

if search(root,target):
    print("Found")
else:
    print("Not found")