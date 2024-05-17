class Node:
    def _init_(self, num=0):
        self.data = num
        self.next = None

# Operations on the linkedlist for Nodes
class LinkedList:
    def _init_(self):
        self.head = None
        self.temp = None
        self.__length = 0

    def appendNode(self, num=0):
        nn = Node(num)
        nn.data = int(input("Enter the New Node Value: "))

        if self.head is None:
            # list is empty
            self.head = nn
            self.temp = nn
            self.__length += 1
        else:
            # list is present
            self.temp = self.head

            while self.temp.next is not None:
                self.temp = self.temp.next

            self.temp.next = nn
            self.__length += 1

    def printList(self):
        print("List is")
        self.temp = self.head
        while self.temp is not None:
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

    def removeNode(self, value):
        current = self.head
        previous = None

        while current is not None:
            if current.data == value:
                if previous is not None:
                    previous.next = current.next
                else:
                    self.head = current.next
                self.__length -= 1
                return
            previous = current
            current = current.next

class StackClass:
    def _init_(self):
        self.stack = LinkedList()

    def printListUsingStack(self):
        stack_data = []
        temp = self.stack.head

        while temp is not None:
            stack_data.append(temp.data)
            temp = temp.next

        print("List (printed using stack):")
        while stack_data:
            print(stack_data.pop(), end="->")
        print("None")

if __name__ == "__main__":
    stack = StackClass()
    stack.stack.appendNode()
    stack.stack.appendNode()
    stack.stack.appendNode()
    stack.stack.printList()
    print("len: ", stack.stack.getLength())
    stack.stack.addNodeBeg()
    stack.stack.printList()
    print("len: ", stack.stack.getLength())
    value_to_remove = int(input("Enter the value to remove: "))
    stack.stack.removeNode(value_to_remove)
    stack.stack.printList()
    print("len: ", stack.stack.getLength())

    stack.printListUsingStack()