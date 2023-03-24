class StaticArrayList():
  def __init__(self, capacity):
    self._list = [0] * capacity
    self._capacity = capacity
    self._size = 0

  def printSAL(self):
    i = 0
    for i in range(self._capacity):
      print(self._list[i], end=" ")
      i += 1
    print()

  def isFull(self):
    return self._size == self._capacity

  def isEmpty(self):
    return self._size == 0

  def popBack(self):
    if not self.isEmpty():
      self._size += -1
      newList = [0]
      newList = newList * self._capacity
      i = 0
      while i < self._size:
        newList[i] = self._list[i]
        i += 1
      self._list = newList
    else:
      print('List is Empty.')

  def pushBack(self, key):
    if not self.isFull():
      self._list[self._size] = key
      self._size += 1
    else:
      print('There are no remaining spaces.')

  def length(self):
    print('The size is: ' + str(len(self._list)))

  def erase(self, clave):
    relist = [0]
    relist = relist * self._capacity
    i = 0
    while i < self._size:
      if self._list[i] == clave:
        k = i
        while k < self._size:
          relist[k] = self._list[k+1]
          k += 1
        
      else:
        relist[i] = self._list[i]
      i += 1
    self._list = relist


myList = StaticArrayList(5)
myList.pushBack(1)
myList.pushBack(2)
myList.pushBack(2)
myList.pushBack(2)
myList.printSAL()
print('Is the list Full?: ' + str(myList.isFull()))
myList.popBack()
myList.popBack()
myList.printSAL()
myList.erase(2)
myList.printSAL()
myList.length()
print('Is the list Full?: ' + str(myList.isFull()))
