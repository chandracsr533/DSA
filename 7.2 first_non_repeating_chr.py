from collections import deque

text = "programming"

freq = {}

for char in text:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1

# Put characters into queue
queue = deque()

for char in text:
    if freq[char] == 1:
        queue.append(char)

print(queue[0])