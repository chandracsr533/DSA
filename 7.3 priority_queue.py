import heapq

queue = []

heapq.heappush(queue,30)
heapq.heappush(queue,10)
heapq.heappush(queue,20)

print(heapq.heappop(queue))