from collections import deque
class Queue:

    def __init__(self):
        self.items = deque

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Очередь пуста")
        else:
            return self.items.popleft()
    

    def peek(self):
        if self.is_empty():
            raise IndexError("Очередь пуста")
        else:
            return self.items[0]
    
    def is_empty(self):
        return not self.items

    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
    
q = Queue()
q.push(3)
q.push(5)
q.push(8)

print(q.pop())
print(q.pop())
print(q.pop())


