# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None

# first = Node(5)
# second = Node(15)
# third = Node(25)
# fourth = Node(35)

# first.next = second
# second.next = third
# third.next = fourth

# current = first

# while current:
#     print(current.data)
#     current = current.next

#################33

"""Insering a new node"""

# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None

# first = Node(5)
# second = Node(15)
# third = Node(25)
# fourth = Node(35)


# first.next = second
# second.next = third
# third.next = fourth

# new_node = Node(20)

# current = second
# # current = second

# new_node.next = second.next
# second.next = new_node
# # new_node.next = current.next
# # current.next = new_node

# current = first

# while current:
#     print(current.data)
#     current = current.next


#####################3

"""Deleting a node"""

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None


# first = Node(5)
# second = Node(15)
# third = Node(20)
# fourth = Node(25)
# fifth = Node(35)

# first.next = second
# second.next = third
# third.next = fourth
# fourth.next = fifth


# # Delete 20
# current = second

# current.next = current.next.next


# # Traverse
# current = first

# while current:
#     print(current.data)
#     current = current.next

####################3

"""Reverse a linked list"""

# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None

# first = Node(5)
# second = Node(10)
# third = Node(15)
# fourth = Node(20)

# first.next = second
# second.next = third
# third.next = fourth

# previous = None
# current = first

# while current:
#     next_node = current.next
#     current.next = previous
#     previous = current
#     current = next_node

# first = previous

# current = first

# while current:
#     print(current.data)
#     current = current.next

#################

"""Finding the middle node"""

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None


# first = Node(10)
# second = Node(20)
# third = Node(30)
# fourth = Node(40)
# fifth = Node(50)
# sixth = Node(60)

# first.next = second
# second.next = third
# third.next = fourth
# fourth.next = fifth
# fifth.next = sixth


# slow = first
# fast = first     #second middle
# # fast = first.next     #first middle

# while fast and fast.next:
#     slow = slow.next
#     fast = fast.next.next

# print(slow.data)

############################

"""Cycle Detection 🔄"""

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None


# first = Node(10)
# second = Node(20)
# third = Node(30)
# fourth = Node(40)

# first.next = second
# second.next = third
# third.next = fourth

# # Create a cycle
# fourth.next = second


# slow = first
# fast = first

# while fast and fast.next:
#     slow = slow.next
#     fast = fast.next.next

#     if slow == fast:
#         print("Cycle detected")
#         break
# else:
#     print("No cycle")

###################

