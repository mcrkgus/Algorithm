#스택으로 큐 구현하기 - 파이썬
class HyunQueue():
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self,x):
        self.stack1.append(x)

    def pop(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop() if self.stack2 else -1

    def size(self):
        return len(self.stack1) + len(self.stack2)

    def empty(self):
        return not self.stack1 and not self.stack2

    def front(self):
        if self.stack2:
            return self.stack2[-1]
        elif self.stack1:
            return self.stack1[0]
        else:
            return -1

    def back(self):
        if self.stack1:
            return self.stack1[-1]
        elif self.stack2:
            return self.stack2[0]
        else:
            return -1
