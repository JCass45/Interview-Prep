class MyQueue(object):
    def __init__(self):
        self.enq_stack = []
        self.deq_stack = []

    def peek(self):
        if len(self.deq_stack) == 0:
            return self.enq_stack[0]

        return self.deq_stack[-1]

    def pop(self):
        if len(self.deq_stack) == 0:
            len_enq = len(self.enq_stack)
            for i in range(len_enq):
                self.deq_stack.append(self.enq_stack.pop())

        val = self.deq_stack.pop()
        print('enq:', self.enq_stack)
        print('deq:', self.deq_stack)
        return val

    def put(self, value):
        self.enq_stack.append(value)
        print('enq:', self.enq_stack)
        print('deq:', self.deq_stack)


queue = MyQueue()
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())
