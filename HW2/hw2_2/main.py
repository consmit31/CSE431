class Item:
    def __init__(self, priority, max, next = None) -> None:
        self.priority = priority
        self.max = max
        self.next = next

class Stack:
    def __init__(self, top = None) -> None:
        self.top = top

    def add(self, item : Item):
        if self.top == None:
            self.top = item
        else:
            item.next = self.top
            self.top = item

    def pop(self) -> Item:
        temp = self.top
        self.top = self.top.next
        temp.next = None
        return temp
    
    def getMax(self) -> int:
        return self.top.max

        

idx = int(input())

stack = Stack()
for i in range(idx):
    event = input().split()
    if event[0] == "1":
        p = int(event[1])
        if stack.top != None:
            if p > stack.getMax():
                item = Item(p, p)
            else:
                item = Item(p, stack.getMax())
            stack.add(item)
        else:
            stack.add(Item(p, p))
    if event[0] == "2":
        stack.pop()
    if event[0] == "3":
        print(stack.getMax())
        

