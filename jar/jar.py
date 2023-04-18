
class Jar:
    def __init__(self, capacity=12, size = 0): #This are the characteristics of the object.
        if capacity < 0:
            raise ValueError
        #else:
            #self.capacity = 12
        self._capacity = capacity
        self._size = size

    def __str__(self):
        return "🍪"*self.size

    def deposit(self, n):
        if n + self.size > self.capacity:
            raise ValueError
        else:
            self._size = self._size + n


    def withdraw(self, n): #withdraw = retirar
        if n > self._size:
            raise ValueError
        else:
            self._size = self._size - n

    @property #All property decorators must have a setter.
    def capacity(self):
        return int(self._capacity)

    @capacity.setter
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return int(self._size)

    @size.setter
    def size(self):
        return self._size

    #def __add__(self, deposit, size)
        #size =
          #  if deposit




#print(12*str("🍪"))

#jar = Jar()

#print(str(jar)) #Output: ""

#jar.deposit(1)
#print(str(jar)) #Output: "🍪"

#jar.deposit(11)
#print(str(jar)) #Output: "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

#print(str(jar.capacity))