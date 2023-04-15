
class Jar:
    def __init__(self, capacity=12):
        ...

    def __str__(self):
        ...

    def deposit(self, n):
        if n > 12:
            raise ValueError
        ...

    def withdraw(self, n): #withdraw = retirar
        ...

    @property
    def capacity(self):
        ...

    @property
    def size(self):
        ...
