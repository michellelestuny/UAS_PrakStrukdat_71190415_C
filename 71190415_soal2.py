class Node:
    def __init__(self,data,priority) -> None:
        self._data = data
        self._priority = priority
        self._next = None
        self._prev = None
class PQSTugas:
    def __init__(self) -> None:
        self._head = None
        self._tail = None
        self._size = 0
        self._front = None
    def isEmpty(self) -> bool:
        return True if self.front == None else False
    pass
    def printAll(self) -> None:
        for i in self._data[:-1]:
            print("{}," .format(i), end=" ")
        print("{}" .format(self._data[-1]))
        pass
    def _addHead(self, newNode, priority) -> None:
        if self._head is None:
            self._tail = self._head = Node(newNode)
        else:
            self._tail.next = Node(newNode)
            self._tail = self._tail.next
        return self.tail
    def _addTail(self, newNode) -> None:
        pass
        bantu = self._head._prev
        newNode  = bantu
        bantu = self._tail

    def _addMiddle(self, newNode) -> None:
        pass

    def add(self, data, priority) -> None:
        if self.isEmpty() == True:
                self.front = Node(data,priority)
                return 1 
        else:
            if self.front._priority > priority:
                newNode = Node(data,priority)
                newNode.next = self._front
                self._front = newNode
                return 1
            else:
                temp = self.front
                while temp.next:
                    if priority <= temp.next.priority:
                        break
                    temp = temp.next
                newNode = Node(data,priority)
                newNode.next = temp.next
                temp.next = newNode
                return 1
    def remove(self) -> None:
        if self.isEmpty() == True:
            return
        else: 
            self.front = self.front.next
            return 1
    def removePriority(self, priority) -> None:
        priority = 0
        while self._data[priority][1] != priority:
            priority += 1
        del self._data[priority]

if __name__ == "__main__":
 tugasKu = PQSTugas()
 tugasKu.add("StrukDat",1)
 tugasKu.add("Menyapu", 5)
 tugasKu.add("Cuci Baju", 4)
 tugasKu.add("Beli Alat Tulis", 3)
 tugasKu.add("Cuci Sepatu", 4)
 tugasKu.printAll()
 tugasKu.remove()
 tugasKu.printAll()
 tugasKu.removePriority(2)
 tugasKu.removePriority(4)
 tugasKu.printtAll()