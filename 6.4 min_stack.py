# class MinStack:
#     def __init__(self):
#         self.stack = []
#         self.min_stack = []

#     def push(self,value):
#         self.stack.append(value)

#         if not self.min_stack or value <= self.min_stack[-1]:
#             self.min_stack.append(value)

#     def pop(self):
#         value = self.stack.pop()

#         if value == self.min_stack[-1]:
#             self.min_stack.pop()

#         return value

#     def get_min(self):
#         return self.min_stack[-1]


# s = MinStack()

# s.push(10)
# s.push(5)
# s.push(20)
# s.push(3)

# print(s.stack)
# print(s.min_stack)

# print(s.get_min())  # 3

# s.pop()

# print(s.get_min())  # 5

