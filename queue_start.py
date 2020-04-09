from collections import deque

queue = deque()

queue.append(2)
queue.append(42)
queue.append(12)
queue.append(34)
queue.append(10)

print(queue)

num = queue.popleft()
print(num)
print(queue)
