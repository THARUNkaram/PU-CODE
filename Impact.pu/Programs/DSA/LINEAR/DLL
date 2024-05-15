class Node:
    def __init__(self):
        self.data = 0
        self.next = None
        self.prev = None

class DLinkedList:

    def __init__(self):
        self.head = None
        self.temp = None
        self.res = ""
        self.ser = ""


    def append(self, num=0):
        nn = Node()
        if num == 0:
            num = int(input("Enter the new Node Value"))
            nn.data = num
        else:
            nn.data = num

        if self.head == None:
            # empty list
            self.head = nn
            self.temp = nn
        else:
            # list is present
            self.temp = self.head
            while(self.temp.next != None):
                self.temp = self.temp.next
            self.temp.next = nn
            nn.prev = self.temp


    def printFList(self):

        print("List is")
        self.temp = self.head
        while(self.temp != None):
            print(self.temp.data,end="->")
            self.res += str(self.temp.data) +" "
            self.temp = self.temp.next
        print("None")

    def printBList(self):
        print("Backward List is")
        self.temp = self.head
        while (self.temp.next != None):
            self.temp = self.temp.next
        while(self.temp != None):
            print(self.temp.data, end="->")
            self.ser += str(self.temp.data) +" "
            self.temp = self.temp.prev
        print("None")
      
    def palin(self):
      if self.res == self.ser: 
        print(f"{self.res} xis a palindrome ")
      else:
        print("not a palindrome ")
        
    

if __name__ == "__main__":
    dLL = DLinkedList()
    dLL.append(100)
    dLL.append(150)
    dLL.append(150)
    dLL.append(100)
    dLL.printFList()
    dLL.printBList()
    dLL.palin()