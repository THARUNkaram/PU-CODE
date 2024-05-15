class Node:
 
  def __init__(self, sname,fname,emp_id,mobile):
    self.sname = sname
    self.fname = fname
    self.emp_id=emp_id
    self.mobile = mobile 
    self.next = None

# operations on the linkedlist for Nodes

class LinkedList:
 
  def __init__(self):
    self.head = None
    self.temp = None
    self.__length = 0
    self.tempp = None
    self.a=None
   
  def appendNode(self,sname,fname,emp_id,mobile):
    nn = Node(sname,fname, emp_id, mobile)
    
    
   
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
        count = 0
        while self.temp is not None:
            count += 1
            print(f" {count}  : First Name: {self.temp.sname}, Surname: {self.temp.fname}, Emp ID: {self.temp.emp_id}, Mobile: {self.temp.mobile}")
             
            self.temp = self.temp.next
        print("None")   
  
  def sortLinkedList(self):
        slow = self.head
        for i in range(self.__length):
            fast = slow.next
            while(fast):
                if slow.sname > fast.sname:
                    slow.sname, fast.sname = fast.sname, slow.sname
                    slow.fname, fast.fname = fast.fname, slow.fname
                    slow.emp_id, fast.emp_id = fast.emp_id, slow.emp_id
                    slow.mobile, fast.mobile = fast.mobile, slow.mobile
                fast = fast.next
            slow = slow.next
        return self.head
        
  def sortLinkedListMobile(self):
        slow = self.head
        for i in range(self.__length):
            fast = slow.next
            while(fast):
                if slow.mobile > fast.mobile:
                    slow.sname, fast.sname = fast.sname, slow.sname
                    slow.fname, fast.fname = fast.fname, slow.fname
                    slow.emp_id, fast.emp_id = fast.emp_id, slow.emp_id
                    slow.mobile, fast.mobile = fast.mobile, slow.mobile
                fast = fast.next
            slow = slow.next
        return self.head      

    
if __name__ == "__main__":
  LL = LinkedList()
  LL.appendNode("tharun","karampudi",250000,7396577271)
  LL.appendNode("xmanoj","gandasiri",300000,8996579787)
  LL.appendNode("rahul","peddi",770000,6796579890)
  LL.appendNode("batta","karingula",60000,9396576876)
  LL.appendNode("zajay","narayana",70000,1396576879)
  LL.printList()
  LL.sortLinkedList()
  LL.printList()
  LL.sortLinkedListMobile()
  LL.printList()
 
  