class CircularQueueArray:
    n = 0
    f = r = -1
    arr = []
    def __init__(self):
        self.n = int(input("Enter size of Queue : "))
        self.arr = [0 for x in range(self.n)]
    
    def isFull(self):
        return (self.r>self.f and self.f+self.r==self.n-1) or (self.f>self.r and self.f-1==self.r)
    def isEmpty(self):
        return self.f==-1 and self.r==-1
    def enqueue(self,data):
        if(self.isEmpty()):
            self.f = self.r = 0
            self.arr[self.r] = data
        elif(self.isFull()):
            print("Queue Overflow!")
        elif(self.r+self.f==self.n-1):
            self.r = 0
            self.arr[self.r] = data
        else:
            self.r += 1
            self.arr[self.r] = data
    
    def dequeue(self):
        if(self.isEmpty()):
            print("Queue Underflow!!")
        elif(self.r+self.f==self.n-1):
            self.f = 0
        elif(self.r==self.f):
            self.f = self.r = -1
        else:
            self.f += 1
    def print(self):
        if(self.isEmpty()):
            print("Queue Empty")
        elif(self.f>self.r):
            itr = self.f
            end = self.n
            for i in range(itr,end):
                print(self.arr[i])
            itr = 0
            end = self.r
            for i in range(itr,end):
                print(self.arr[i])

        else:
            for i in range(self.f,self.r+1):
                print(self.arr[i])

q = CircularQueueArray()
q.enqueue(1)
q.enqueue(23)
q.enqueue(-10)
q.dequeue()
q.print()



    