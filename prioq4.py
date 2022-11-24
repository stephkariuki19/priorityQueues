class MinHeap:
    def __init__(self, capacity):
        self.storage = [0] * capacity
        self.capacity = capacity
        self.size = 0

    def getLeftChildIndex(self, index):
        return 2 * index + 1

    def getRightChildIndex(self, index):
        return 2 * index + 2

    def getParentIndex(self, index):
        return (index - 1) // 2

    def hasLeftChild(self, index):
        return self.getLeftChildIndex(index) < self.size

    def hasRightChild(self, index):
        return self.getRightChildIndex(index) < self.size

    def hasParent(self, index):
        return self.getParentIndex(index) >= 0

    def leftChild(self, index):
        return self.storage[self.getLeftChildIndex(index)] #getting actual data from that index

    def rightChild(self, index):
        return self.storage[self.getRightChildIndex(index)]

    def parent(self, index):
        return self.storage[self.getParentIndex(index)]

    def isFull(self):
        return self.size == self.capacity

    def swap(self, index1, index2):
        temp = self.storage[index1]
        self.storage[index1] = self.storage[index2]
        self.storage[index2] = temp

    def removeMin(self):
        if (self.size == 0):
            raise Exception("Empty Heap")
        data = self.storage[0] #remove at top of tree
        self.storage[0] = self.storage[self.size - 1] #place last ele at top
        self.storage[self.size - 1] = 0
        self.size -= 1
        self.heapifyDown()
        return data

    def removeAbitrary(self,item):
        if (self.size == 0):
            raise Exception("Empty Heap")
        for i in range(self.size):
            index = self.storage[i][2]
            if item[2] == index:
                element = self.storage[i]
                print(f"found{element} about to remove it")

                if self.hasRightChild(i):
                    rchildindex = self.getRightChildIndex(i)
                    self.storage[i] = self.storage[rchildindex]#now 70
                    curr = self.getLeftChildIndex(i)
                    if self.storage[curr] < self.storage[i]:#try swap or heapify down
                        self.storage[curr],self.storage[i] =self.storage[i],self.storage[curr]
                    self.storage[rchildindex] = 0
                    self.size -= 1
                    print("replacing with right child")
                    self.heapifyDown()
                    return element
                elif (self.hasRightChild(i)==False) and (self.hasLeftChild(i)):
                    lchildindex = self.getLeftChildIndex(i)
                    self.storage[i] = self.storage[lchildindex]
                    self.storage[lchildindex] = 0

                    print("replacing with left child")
                    self.size -= 1
                    self.heapifyDown()
                    return element
                else:
                    self.storage[i] = self.storage[self.size - 1]  # placing last item there...bug alert
                    self.storage[self.size-1] = 0
                    self.size -=1
                    print("has no  child")
                    self.heapifyDown()
                    return element



    def heapifyDown(self):
        index = 0 #start at the top,check for smallest and if min heap,is ok,continue moving down
        while (self.hasLeftChild(index)):
            smallerChildIndex = self.getLeftChildIndex(index)
            if (self.hasRightChild(index) and self.rightChild(index) < self.leftChild(index)):
                smallerChildIndex = self.getRightChildIndex(index)
            if (self.storage[index] < self.storage[smallerChildIndex]):
                break
            else:
                self.swap(index, smallerChildIndex)
            index = smallerChildIndex

    def insert(self, data):
        if (self.isFull()):
            raise Exception("Heap is Full")
        self.storage[self.size] = data#put data at last pos
        self.size += 1
        self.heapifyUp()


    def heapifyUp(self):#check if that parent is > swap to remain min heap,check 4 all parents
        index = self.size - 1
        while (self.hasParent(index) and
               self.parent(index) > self.storage[index]):
            self.swap(self.getParentIndex(index), index)
            index = self.getParentIndex(index)
    def peekQueue(self):
        return self.storage[0]
    def pollQueue(self):
        # min = self.storage[0]
        min = self.removeMin()
        return min
    def Queuesize(self):
        return self.size
    def isEmpty(self):
        return self.size==0
    def replace(self,item,new_item):
        for i in range(self.size):
            if self.storage[i] ==item:
                print(f"found {item},replacing it ")
                self.storage.remove(item)
                #self.insert(new_item)
                #self.storage.add(self.size+1,new_item)
                self.storage.insert(self.size+1,new_item)
                self.heapifyUp()




m = MinHeap(7)
# m.insert(3)
# m.insert(4)
# m.insert(9)
# m.insert(5)
# m.insert(2)

# m.insert((3,"a"))
# m.insert((4,"a"))
# m.insert((9,"z"))
# m.insert((5,"d"))
# m.insert((2,"boy"))
# m.insert((70,"lamu"))

#WITH LOCATION AWARENESS
print( f" is q empty {m.isEmpty()}  ")
m.insert((3,"a",0))
m.insert((4,"a",1))
m.insert((1,"z",2))
m.insert((5,"d",3))
m.insert((2,"boy",4))

print(m.storage)
print("removing an element ")
m.removeAbitrary((2,"boy",4))
m.removeMin()
print(m.storage)
print("peek")
print(m.peekQueue())
print("polling")
#print(m.pollQueue())
print(m.storage)
print(m.Queuesize())
print( f" is q empty {m.isEmpty()}  ")
print("replacing")
m.replace((5,"d",3),(2,"d",3))
print(m.storage)

# print("no removal")
# print(m.storage)
# print("priority of first element")
# val= m.storage[0][0] #returns 2 for 2,boy
# print(val)
# if val ==3:
#     print("same")
# else:
#     print("not same")
# print(m.removeMin())
# print("after removal")
# print(m.storage)
# print(m.hasParent(0))
# print("has left child")
# print(m.leftChild(2))
# print(m.parent(5))
# print("outputting others")
# print(m.storage[3])
#
# #adding a higher priority
# #m.insert((1,"new",6))
# print("added higher priority")
# print(m.storage)
#
# print("removing some element")
# m.removeAbitrary((4,"a",1))
# print(m.storage)
#
# print("test for val2")
# val2= m.storage[0] #returns 2 for 2,boy
# print(val2)
# if val2 == (1,"new"):
#      print("same")
# else:
#     print("not same")
# print("size of array")





