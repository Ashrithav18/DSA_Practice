class TwoStacks:

    def __init__(self, n):
        self.size = n
        self.arr = [None] * n
        self.top1 = -1
        self.top2 = n

    def push1(self, x):
        if self.top1 < self.top2 - 1:
            self.top1 += 1
            self.arr[self.top1] = x
        else:
            print("Stack Overflow")

    def push2(self, x):
        if self.top1 < self.top2 - 1:
            self.top2 -= 1
            self.arr[self.top2] = x
        else:
            print("Stack Overflow")

    def pop1(self):
        if self.top1 >= 0:
            x = self.arr[self.top1]
            self.top1 -= 1
            return x
        return -1

    def pop2(self):
        if self.top2 < self.size:
            x = self.arr[self.top2]
            self.top2 += 1
            return x
        return -1
ts = TwoStacks(6)

ts.push1(2)
ts.push1(3)
ts.push2(4)

print(ts.pop1())   # 3
print(ts.pop2())   # 4
print(ts.pop2())   # -1