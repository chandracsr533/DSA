# from collections import deque

# queue = deque()

# queue.append(10)
# queue.append(20)
# queue.append(30)

# print(queue)
# queue.popleft()
# print(queue)

###########3

# class Queue:
#     def __init__(self):
#         self.queue = []

#     def enqueue(self,data):
#         self.queue.append(data)

#     def dequeue(self):
#         if len(self.queue) == 0:
#             print("Queue is empty")
#         else:
#             return self.queue.pop(0)

#     def peek(self):
#         if len(self.queue) == 0:
#             print("Queue is empty")
#         else:
#             return self.queue[0]

#     def is_empty(self):
#         return len(self.queue) == 0

# q = Queue()

# q.enqueue(10)
# q.enqueue(20)
# q.enqueue(30)

# print("Queue:",q.queue)
# print("Front:",q.peek())
# print("Removed:",q.dequeue())
# print("Queue:",q.queue)

##########3

from collections import deque

dq = deque()

dq.append(10)
dq.append(20)

dq.appendleft(0)
print(dq)

dq.pop()
print(dq)
dq.popleft()
print(dq)