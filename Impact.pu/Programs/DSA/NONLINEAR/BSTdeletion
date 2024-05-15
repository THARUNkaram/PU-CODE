class BinTree:
    def __init__(self, val=0):
        self.data = val
        self.left = None
        self.right = None

    def insert(self, val):
        if self.data == 0:
            self.data = val
            return
        if self.data < val:
            if self.right is None:
                self.right = BinTree(val)

            else:
                self.right.insert(val)
        else:
            if self.left is None:
                self.left = BinTree(val)
            else:
                self.left.insert(val)

    def preOrder(self):
      #root - left - right
      print(self.data, end=" ")
      if self.left is not None:
        self.left.preOrder()
      if self.right is not None:
            self.right.preOrder()
      
      
            
    def inOrder(self):
      
        # Left-Root-Right
        if self.left is not None:
            self.left.inOrder()
        print(self.data, end=" ")
        if self.right is not None:
            self.right.inOrder()
        #print("hdfh")

    def postOrder(self):
        # Left-Right-Root
        if self.left is not None:
            self.left.postOrder()
        if self.right is not None:
            self.right.postOrder()
        print(self.data, end=" ")
        
    #deletion of leaf nodes uing two pointers

    def delofLeftLeaf(self,a=0):
      slow = self
      fast = slow.left
      
      while(fast.left):
        slow = slow.left
        fast = fast.left
      #print(slow.data, fast.data)
      if slow.right is None:
        slow.left = None
    
    def delofRightLeaf(self,a=0):
      slow = self
      fast = slow.right
      
      while(fast.right):
        slow = slow.right
        fast = fast.right
      #print(slow.data, fast.data)
      if slow.left is None:
        slow.right = None 
        
    def find_max(self):
      if self.right is None:
        print(self.data)
        return 
      return self.right.find_max()

    def find_min(self):
      if self.left is None:
        print(self.data)
        return 
      return self.left.find_min()
  
    def delete(self, val):
        if self is None:
            return self
        
        if val < self.data:
            self.left = self.left.delete(val)
        elif val > self.data:
            self.right = self.right.delete(val)
        else:
            # one child node
            if self.left is None:
                temp = self.right
                self = None
                return temp
            elif self.right is None:
                temp = self.left
                self = None
                return temp
            else:
              
              '''# Node with two children 
              temp = self.find_min()
              # Copy 
              self.data = temp
              # Delete copy data
              #self.right = self.right.delete(temp)'''
        return self
        
    '''
    def delete(self, val):
      if val < self.data:
        if self.left:
          self.left = self.left.delete(val)
        elif val > self.data:
          if self.right:
            self.right = self.right.delete(val)
        else:
          if self.left is None and self.right is None:
            return None
          elif self.left is None:
            return self.right
          elif self.right is None:
            return self.left

          temp = self.right.find_min()
          self.data = temp.data
          self.right = self.right.delete(temp.data)

        return self'''
    '''   
    def printL(self):
      print(self.data,end=" ")
      while self.left:
        print(self.left.data,end=" ")
        self.left = self.left.left
      print()
      while self.right:
        print(self.right.data,end=" ")
        self.right = self.right.right'''
        
      
      
      
bt = BinTree()
bt.insert(50)
bt.insert(30)
bt.insert(20)
bt.insert(40)
bt.insert(70)
bt.insert(60)
bt.insert(80)
bt.insert(10)
bt.insert(25)
bt.insert(8)
#bt.delofLeftLeaf()
#bt.delofRightLeaf()
bt.find_min()
bt.find_max()
#bt.printL()
#print(bt.data)
# 10 7 5 15 25 20
bt.preOrder()
print()
bt.delete(50)
bt.preOrder()
print()
# 5 7 10 15 20 25
bt.inOrder()
#bt.inorder()
# 5 7 20 25 15 10
print()
bt.postOrder()

print()
print()
bt.inOrder()