class myList:
    def __init__(self):
        self.storage = []
        #self.capacity = capacity
        self.size = 0
    # def isFull(self): removing capacity concept
    #     return self.size == self.capacity
    def isEmpty(self):
        return len(self.storage) ==0
    def addPatient(self,item):
        # if (self.isFull()):
        #     raise Exception("Queue is Full")
        #self.storage[self.size] = item  # put data at last pos
        self.storage.append(item)
        self.size += 1
        self.sortList(self.storage)
    def sortList(self,list):
        n = len(self.storage)
        for pass_num in range(n-1,0,-1):
            for i in range(pass_num):
                if list[i] > list[i+1]:
                    list[i],list[i+1]=list[i+1],list[i]
    def removePatient(self,item):
        # if self.size==0:
        #     raise Exception("Queue is empty")
        for i in range(len(self.storage)-1):
            if self.storage[i] ==item:
                print(f"found {item}")
                self.storage.pop(i)#reduces capacity
                #self.storage[self.size+1]=0

    def replace(self,item,newitem):# new item=new key,old value
        if self.size==0:
            raise Exception("Queue is empty")
        for i in range(len(self.storage)):
            if self.storage[i] ==item:
                print(f"found {item}")
                self.storage.pop(i)#reduces capacity
                self.storage.append(newitem)
                self.sortList(self.storage)
            # if self.storage[i][0] == key:
            #     print(f"found key,removing it {key}")
            #     self.storage.pop(i)
                # self.storage.pop(i)
                # print("about to remove")
                # self.storage.append(replacement)
                # print("removed")
                #self.sortList(self.storage)
                # remove

    def Queuesize(self):
        return len(self.storage)
    def peekQueue(self):
        return self.storage[0]
    def pollQueue(self):
        first_item = self.storage[0]
        self.removePatient(first_item)
        return first_item





# def replaceKey(key, replacement):
#     if len(hos_line) == 0:
#         raise Exception("Empty Queue")
#     for i in range(len(hos_line)):
#         if hos_line[i][0] == key:
#             print(f"found key {key}")
#             hos_line[i][0] = replacement
#             hos_line.sort()
#         else:
#             print(f"{key} not found")







m = myList()
m.addPatient((2,"mary"))
m.addPatient((9,"ian"))
m.addPatient((6,"jane"))
m.addPatient((8,"jane"))
m.addPatient((3,"ane"))
m.addPatient((4,"e"))
# m.sortList(m.storage)
print("sorted list")
print(m.storage)
print(f"is list empty? {m.isEmpty()}")
m.removePatient((6,"jane"))
print(m.storage)
m.replace((2,"mary"),(3,"mary"))#mary be at back
m.replace((9,"ian"),(0,"ian"))
m.replace((8,"jane"),(1,"jane"))
m.replace((4,"e"),(4,"ian"))

print("replacing key")
print(m.storage)
print(m.Queuesize())
print(m.peekQueue())
print("polling queue")
print(m.pollQueue())
print(m.storage)
