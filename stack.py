class Stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def is_empty(self):
        self.items == []
    def size(self):
        return len(self.items)
    def peek(self):
        return self.items[len(self.items) -1]

if __name__ == '__main__':
    
    s = Stack()
    for i in ["A", "B", "C"]:
        s.push(i)
    print(s.items)
    print(s.peek())
    print(s.is_empty())
    print(s.size())
    print(s.pop())