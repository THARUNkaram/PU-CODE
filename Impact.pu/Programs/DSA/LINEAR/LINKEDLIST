class Node:
  def __init__(self, num=0):
    self.data = num
    self.next = None

# operations on the linkedlist for Nodes

class LinkedList:
 
  def __init__(self):
    self.head = None
    self.temp = None
    self.__length = 0
    self.tempp = None
    self.a=None
   
  def appendNode(self,num=0):
    nn = Node(num)
    nn.data = int(input("Enter the New Node Value: "))
   
    if self.head == None:
      #list is empty
     
      self.head = nn
      self.temp = nn
      self.__length += 1
    else:
      #list is present
      self.temp = self.head
     
      while(self.temp.next != None):
        self.temp = self.temp.next
     
      self.temp.next = nn
      self.__length += 1
     
     
  def printList(self):
    print("List is")
    self.temp = self.head
    while(self.temp != None):
      print(self.temp.data, end="->")
      self.temp = self.temp.next
    print("None")
 
  def getLength(self):
    return self.__length
 
  def addNodeBeg(self, num=0):
    nn = Node()
    nn.data = int(input("Enter Value: "))
    nn.next = self.head
   
    self.head = nn
    self.__length += 1

  #deletion
  def deletionB(self):
    if self.head == None:
      print("the list is empty")
      return 
    self.temp = self.head 
    self.head = self.temp.next
    self.temp = self.head
    
  def deletEE(self):
    if self.head == None:
      print("the list is empty")
      return 
    self.temp = self.head
    while(self.temp.next != None):
      self.temp = self.temp.next
    self.temp = None
    
	#sorting	
  def sortLinkedList(self):
        slow = self.head
        for i in range(self.__length):
            fast = slow.next
            while(fast):
                if slow.data > fast.data:
                    slow.data, fast.data = fast.data, slow.data
                fast = fast.next
            slow = slow.next
        return self.head
	    
  def maxsum(self):
    slow = self.head
    maxm = 0
    lenList = LL.getLength()
    for i in range(lenList):
        fast = slow.next
        if i < lenList - 1:
            a = abs(slow.data - fast.data)
        else:
            break
        fast = fast.next
        slow= slow.next
        if maxm < a:
            maxm = a
    print(maxm)
		
  def middel(self):
     slow = self.head
     fast = self.head
     while fast and fast.next:
        fast = fast.next.next
        slow =slow.next
     print(slow.data)

     

  def reverse(self):
     prev=None
     curr= self.head
     while curr is not None:
        next = curr.next
			  
        curr.next = prev
			  
        prev = curr
			  
        curr = next
     self.head= prev
     
 

if __name__ == "__main__":
  LL = LinkedList()
  LL.appendNode()
  LL.appendNode()
  LL.appendNode()
  LL.appendNode()
  LL.printList()
  print("len: ",LL.getLength())
  #LL.addNodeBeg()
  LL.printList()
  print("len: ",LL.getLength())
  #print(LL.deletionB())
 # LL.deletEE()
  #LL.printList()
  LL.reverse()
  #LL.printOut()
  LL.printList()
  LL.sortLinkedList()
  LL.printList()
  LL.maxsum()