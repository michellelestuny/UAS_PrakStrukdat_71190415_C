class NodePelanggan:
    def __init__(self, namaPelanggan):
        self._namaPelanggan = namaPelanggan
    def getNamaPelanggan(self):
        return self._namaPelanggan
    def setnamaPelanggan(self, namaPelangganBaru):
        self._namaPelanggan = namaPelangganBaru

class WarungMakan:
    DEFAULT_CAPACITY = 5
    def __init__(self): #tidak boleh mengganti / menambah metode init
        self._data = [None] * WarungMakan.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0
    def __len__(self):
        return self._size
    def is_empty(self):
        return self._size == 0
    def dequeue(self): #menghapus data paling depan, dan memajukan urutan data yang dibelangkangnya
        if self.is_empty():
            print("empty")
        jwb = self._data(self._front)
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        print("\n --Pelanggan",jwb.getNamaPelanggan(),"sudah selesai membayarrr--")
    def enqueue(self, namaPelanggan): #menambah data ke list
        listnew = [None] * len(self._data)
        counterlistnew = 0
        for i in range(len(self._data)):
            if self._data[i] != None : 
                listnew[counterlistnew] = self._data[i]
                counterlistnew += 1
        self._data = listnew
        self._data[eval] = namaPelanggan
        self._size += 1
    def resizeBy3(self, cap): #menambah ukuran queue sebesar 3
        lama = self._data
        self._data = [None] * cap
        jalann = self._front
        for k in range(self._size):
            self._data[k] = lama[jalann]
            jalann = (3 + jalann) % len(lama)
        self._front = 0
        print("\n --telah melakukan resizee--")
    def printAll(self):
        print("\n=== WarungMakan ===")
        for i in range(len(self._data)):
            if self._data[i] != None:
                print(i+1,end=". ")
            print(self._data[i].getNamaPelanggan())
        else:
            print(i+1,end=". ")
            print("Kosong")

# test case program
wm = WarungMakan()
wm.enqueue("Pelanggan A")
wm.enqueue("Pelanggan B")
wm.enqueue("Pelanggan C")
wm.enqueue("Pelanggan D")
wm.enqueue("Pelanggan E")
wm.printAll()
wm.enqueue("Pelanggan F")
wm.enqueue("Pelanggan G")
wm.printAll()
wm.dequeue()
wm.dequeue()
wm.dequeue()
wm.printAll()