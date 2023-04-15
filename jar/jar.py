
class Jar:
    def __init__(self, capacity=12, ):
        self.capacity = capacity

    def __str__(self):
        return "🍪"*self.size

    def deposit(self, n):
        if n > 12:
            raise ValueError
        self.n = n


    def withdraw(self, n): #withdraw = retirar
        if n > deposit:
            raise ValueError
        self.n = n

    @property #All property decorators must have a setter.
    def capacity(self):
        return self._capacity

    @capacity.setter

    @property
    def size(self):
        return self._size

    @size.setter(self, )
    def __add__()
        return n*str("🍪")

    #def __add__(self, deposit, size)
        #size =
          #  if deposit


print(12*str("🍪"))

jar = Jar()
"""
print(str(jar)) #Output: ""

jar.deposit(1)
print(str(jar)) #Output: "🍪"

jar.deposit(11)
print(str(jar)) #Output: "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"
"""