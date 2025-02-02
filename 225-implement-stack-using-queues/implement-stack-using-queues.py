class Queue():
    def __init__(self,k:'int'):
        # You must use Python List
        # Must use all spaces
        self._a = [None]*k #CANNOT CHANGE THIS. k space is already allocated
        self._MAX = k
        ## YOU CAN HAVE YOUR PRIVATE DATA MEMBER HERE
        self._front = -1
        self._rear = -1
        self._size =0
        self._capacity= k

    def isEmpty(self) -> bool:
        if self._size == 0:
            return True

        return False

    def isFull(self) -> bool:
        if self._size == self._capacity:
            return True
        return False
        
    def enQueue(self, T) -> bool:
        if self.isFull():
            return False 
            
        if self.isEmpty():
            self._front = 0
            self._rear = 0
        else:
            if self._rear == self._MAX - 1:
                self._rear = 0
            else:
                self._rear += 1
                
        self._a[self._rear] = T
        self._size +=1
        return True

    
    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
            
        removed = self._a[self._front]
        if self._front == self._rear:
            self._front = -1
            self._rear = -1
        else:
            if self._front == self._MAX - 1:
                self._front = 0
            else:
                self._front += 1
        self._size -=1
        return True

        
    def Front(self)->'T':
        ## YOU CANNOT CALL pop(0). NOTE: pop(0) is O(n). We want THETA(1)
        if self.isEmpty():
            return -1
        return self._a[self._front]
    
    def Rear(self):
        if self.isEmpty():
            return -1
        return self._a[self._rear]

    

   

        
    ## WRITE ALL OTHER ROUTINES
    
    #Print from FRONT TO REAR
    def __str__(self)->'string':
        s = ""
        if self.isEmpty():
            return "Queue is empty"
        if self._front <= self._rear:
            for i in range(self._front, self._rear + 1):
                s += str(self._a[i]) 
        else:
            for i in range(self._front, self._MAX):
                s += str(self._a[i]) + " "
            for i in range(0, self._rear + 1):
                s += str(self._a[i]) 
        
        return s
        ## WRITE CODE HERE
        
    def __len__(self)->'int':
        # print("WRITE CODE to return number of elements in Queue at this point")
        return self._size
    
class MyStack():
    def __init__(self, n:'size'=10): 
        # ONLY DATA STRUCTURE YOU CAN USE HERE IS ONLY QUEUE THAY YOU WROTE
        self._stack = Queue(n)

    def empty(self) -> bool:
        return self._stack.isEmpty()

    def isfull(self) -> bool:
        return self._stack.isFull()

    
    def push(self, x) -> bool:
        return self._stack.enQueue(x)

    def pop(self):
        popped = self._stack.Rear()
        if popped != -1:
            self._stack._rear -=1
        self._stack._size -= 1
        return popped

    def top(self):
        if self.empty():
            return -1
        return self._stack.Rear()

    

    def __len__(self) -> int:
        return self._stack._size

    