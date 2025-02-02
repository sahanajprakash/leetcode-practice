class Stack():
    def __init__(self): 
        #MUST USE ONLY PYTHON LIST
        self._a = []
        self._max_space = 0
        self._l=0

    def push(self, item):
        self._a.append(item)
        self._l+=1
        self._max_space = max(self._max_space, self._l)

    def pop(self):
        if self._a:
            popped = self._a.pop()
            self._l -=1
            return popped
        else:
            return None

    def top(self):
        return self._a[-1]

    def empty(self):
        return False if self._a else True

    def space(self):
        return self._max_space

    def __len__(self):
        return self._l

class MyQueue():
    def __init__(self): 
        # ONLY DATA STRUCTURE YOU CAN USE HERE IS ONLY STACK THAT YOU WROTE
        self._stack1 = Stack()
        self._stack2 = Stack()
        self._front = -1
    
    def push(self, x):
        
        if self._stack1.empty():
            self._front = x

        while not self._stack1.empty():
            self._stack2.push(self._stack1.pop())
            
        self._stack2.push(x)
        
        while not self._stack2.empty():
            self._stack1.push(self._stack2.pop())
        
            
        

    def pop(self):
        popped = self._stack1.pop()
        if not self._stack1.empty():
            self._front = self._stack1.top()
        return popped

    def peek(self):
        return self._front

    def empty(self):
        return self._stack1.empty()

    def __len__(self):
        return self._stack1._l
