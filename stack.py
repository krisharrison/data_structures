"""Stack Data Structure"""

# Stack class that extend List
class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return -1

    def is_empty(self):
        return self.items == []

    def peak(self):
        if not self.is_empty():
            last_index = len(self.items) - 1
            return self.items[last_index]

    def get_stack(self):
        return self.items


s = Stack()
s.push("A")
s.push("B")
s.push("C")
s.push("D")
print("Get stack: ", s.get_stack())


print("Is empty: ", s.is_empty())

print(s.pop())

print(s.peak())

print(s.get_stack())
