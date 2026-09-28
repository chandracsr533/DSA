# import heapq

# heap = []

# heapq.heappush(heap,30)
# heapq.heappush(heap,10)
# heapq.heappush(heap,20)
# heapq.heappush(heap,5)

# print(heap)

# minimum = heapq.heappop(heap)
# print(minimum)


import heapq

numbers = [30,10,50,20,5]

print(numbers)
heapq.heapify(numbers)
print(numbers)