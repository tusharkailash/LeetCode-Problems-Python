class MyStack(object):
    def __init__(self):
        self.q1 = []
        self.q2 = []

    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.q1.append(x)
        # print self.q1

    # @return nothing
    def pop(self):
        while self.q1:
            tmp = self.q1.pop(0)
            if self.q1:
                self.q2.append(tmp)
        # print self.q2.pop()
        # return tmp
        self.q1 = self.q2
        self.q2 = []
        return tmp

    # @return an integer
    def top(self):
        while self.q1:
            tmp = self.q1.pop(0)
            self.q2.append(tmp)
            # remove the if condition as we want the top element inserted in the queue2 and then print.
        self.q1 = self.q2
        self.q2 = []
        return self.q1.pop()

    # @return an boolean
    def empty(self):
        return len(self.q1) == len(self.q2)


obj = MyStack()
obj.push(2)
obj.push(3)
obj.push(4)

print obj.pop()

print obj.empty()
print obj.top()
print obj.pop()
print obj.empty()

