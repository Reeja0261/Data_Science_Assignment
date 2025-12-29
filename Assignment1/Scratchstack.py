class Stack:
    def __init__(s):
        s.items = []   

    def push(s, value):
        s.items.append(value)   

    def pop(s):
        if s.is_empty():
            return None            
        return s.items.pop()    

    def peek(s):
        if s.is_empty():
            return None
        return s.items[-1]      

    def is_empty(s):
        return len(s.items) == 0



s = Stack()
s.push(10)
s.push(10)
print(s.pop())  
print(s.pop())  