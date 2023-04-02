class Goat:
    legs_num = 4 #атрибут класса
    def __init__(self, height, weight): #специфический метод
        self.height = height
        self.weight = weight
    def __str__(self): #чтобы распечатаать свойства
        s = "weight = {}, height = {}".format(self.weight, self.height)
        return s

Natasha = Goat(20,30)
Veronika = Goat(30,40)
for x in Natasha, Veronika:
    print(x)

Dinochka = Goat(70,21)
Dinochka.horns = 3
print(Dinochka.horns)
Natasha.weight+=1
n = Natasha
n.height+=2
print(n)
n.legs_num +=1 #совершенно другой атрибут, никак не отнсится к классу
"""Именнованные кортежи"""
A = (1,0,3)
r = (A[0]**2, A[1]**2, A[2]**2) #неудобно
from collections import namedtuple
Point = namedtuple("Point", "x y z")
A = Point(1,0,3)
print(A.x)
print(A.y)
print(A.z)

"Связный список"
a = [1]
a.append([2])
#a[1].append([3,a])
a[1].append([3,None])
print(a)
p = a
while p is not None:
    print(p[0])
    p = p[1]

class LinkedList:
    def __init__(self):
        slf._begin = None
    def insert(self,x):
        self._begin = [x,self._begin]
    def pop(self):
        assert self._begin is not None, "List empty"
        x = self._begin[0]
        self._begin =self._begin[1]
        return x