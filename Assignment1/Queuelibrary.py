from collections import deque

queue = deque()

queue.append(40)
queue.append(50)
queue.append(60)

print(queue.popleft())   
print(queue.popleft())   
print(queue.popleft())