
class Jar:
    def __init__(self, capacity=12, size = 0):
        if capacity < 0:
            raise ValueError
        else:
            self._capacity = capacity
            self._size = size

    def __str__(self):
        return "🍪"*self.size

    def deposit(self, n):
        if n + self.size > self.capacity:
            raise ValueError
        self._size += n


    def withdraw(self, n): #withdraw = retirar
        if n > self._size:
            raise ValueError
        self._size -= n

    @property #All property decorators must have a setter.
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self):
        return self._size

    #def __add__(self, deposit, size)
        #size =
          #  if deposit


print(12*str("🍪"))

jar = Jar()

print(str(jar)) #Output: ""

jar.deposit(1)
print(str(jar)) #Output: "🍪"

jar.deposit(11)
print(str(jar)) #Output: "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"
