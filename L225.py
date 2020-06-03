#队列实现栈

class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = []

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        self.q.append(x)
        self.t = x

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        p = []
        for i in range(len(self.q) - 1):
            self.t = self.q.pop(0)
            p.append(self.t)

        x = self.q.pop()
        self.q = p
        return x

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.t

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        if len(self.q) != 0:
            return False
        else:
            return True

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()