class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def get(self, index: int) -> int:
        curr = self.head
        counter = 0

        while (counter < index) and curr:
            curr = curr.next
            counter += 1
        
        if not curr:
            return -1

        return curr.data
        

    def insertHead(self, val: int) -> None:
        newNode = Node(val)
        newNode.next = self.head

        if not self.head:
            self.tail = newNode

        self.head = newNode
        

    def insertTail(self, val: int) -> None:
        newNode = Node(val)

        if not self.head:
            self.head = newNode
            self.tail = newNode
            return

        self.tail.next = newNode
        self.tail = newNode


    # 1) Empty. 2) Singleton. 3) Head. 4) Tail. 5) Regular element
    def remove(self, index: int) -> bool:
        # Empty List
        if not self.head:
            return False

        # Element is the head
        if index == 0:        
            self.head = self.head.next

            if not self.head:
                self.tail = None

            return True

        # Element in the list
        curr = self.head
        counter = 1

        while (counter < index) and curr:
            curr = curr.next
            counter += 1
        
        if curr and curr.next:
            # Change tail
            if curr.next == self.tail:
                self.tail = curr

            # Remove element
            curr.next = curr.next.next
            return True
        
        
        return False


    def getValues(self) -> List[int]:
        values = []
        curr = self.head

        while curr:
            values.append(curr.data)
            curr = curr.next

        return values
        

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None