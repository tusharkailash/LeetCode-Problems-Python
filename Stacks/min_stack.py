class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack1.append(x)
        if len(self.stack2) == 0 or x <= self.stack2[-1]:
            self.stack2.append(x)

    def pop(self):
        """
        :rtype: void
        """
        temp = self.stack1[-1]
        self.stack1.pop()
        if temp == self.stack2[-1]:
            self.stack2.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack1[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.stack2[-1]

obj = MinStack()
obj.push(2)
obj.push(3)
obj.push(14)
obj.push(6)
print obj.pop()
print obj.getMin()
obj.push(1)
obj.push(10)
print obj.pop()
print obj.pop()
obj.push(1)
print obj.getMin()





