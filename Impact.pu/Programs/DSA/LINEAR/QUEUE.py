Q =[]
cap=5
rare = 0
front=0 


def enqueue(num):
  global rare
  global Q
  if rare == cap:
    print("Queue is full")
    return
  Q.append(num)
  rare +=1
  
def dequeue():
  global front
  global rare
  if front == rare:
    if (rare == cap):
      front = 0
      rare = 0
    print("Queue is empty")
    return
  print(f"{Q[front]} element is is dequeue")
  front +=1
  
  
def printList():
  if front == rare:
    print("queue is empty")
    return
  print("Queue is")
  #for i in range(front,len(Q),1):# for python 
    #print(Q[i],end= " ")
  print(Q[front:rare+1])
  print()

if __name__ == "__main__":
  enqueue(10)
  enqueue(20)
  enqueue(30)
  enqueue(40)
  enqueue(50)
  enqueue(50)
  printList()
  dequeue()
  printList()
  '''


####USING CLASS stack
class Stack:
    def __init__ (self):
        self.s = []
        self.cap = 6
        self.top = 0
        self.bottom = 0
    
    def pushStk(self, num):
        if self.top == self.cap:
            print("Stack is full.")
            return
        self.s.append(num)
        self.top = self.top + 1
    
    def popStk(self):
        if self.top == self.bottom:
            print("Stack is Empty.")
            return
        ret = self.s[self.top-1]
        self.top = self.top - 1
        return ret
    
    def printStack(self):
        if self.top == self.bottom:
            print("Stack is Empty")
            return
        for i in range(self.top-1,-1,-1):
            print(self.s[i],end=" ")
    
if __name__ =="__main__":

    s = Stack()
    inp = input("Enter String to Reverse: ")
    inp = list(inp)
    for i in inp:
        s.pushStk(i)
    s.printStack()
    '''