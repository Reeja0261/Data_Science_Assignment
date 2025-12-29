class Queue:
    def __init__(q):
        q.items = []

    def enqueue(q, value):
        q.items.append(value)

    def dequeue(q):
        if q.is_empty():
            return None
        else:
            return q.items.pop(0)

    def is_empty(q):
        return len(q.items) == 0


q = Queue()
q.enqueue(10)
q.enqueue(20)
print(q.dequeue())  
print(q.dequeue())