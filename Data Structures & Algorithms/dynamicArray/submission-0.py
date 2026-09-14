class DynamicArray:
    def __init__(self, capacity: int):
        self.tracker = [None] * capacity
        self.capacity = capacity
        self.length = 0

    def get(self, i: int) -> int:
        return self.tracker[i]


    def set(self, i: int, n: int) -> None:
        self.tracker[i] = n


    def pushback(self, n: int) -> None:
        if self.length == self.capacity:
            self.resize()
        self.tracker[self.getSize()] = n
        self.length += 1

    def popback(self) -> int:
        elem = self.tracker[self.getSize() - 1]
        self.tracker[self.getSize() - 1] = None
        self.length -= 1
        return elem
 

    def resize(self) -> None:
        currentCapacity = self.capacity
        self.capacity *= 2

        newArray = [None] * (self.capacity)
        for i in range(currentCapacity):
            newArray[i] = self.tracker[i]        
        
        self.tracker = newArray 


    def getSize(self) -> int:
        return self.length
    
    def getCapacity(self) -> int:
        return self.capacity
