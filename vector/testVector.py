from vector.Vector import Vector

A = [1, 2, 3, 4, 5, 6, 7]
v = Vector(capacity=None, size=5, v=1, A=A)
num = v.find(8)
print(num)
# print(v[1])
# v[1] = 6
# print(v[1])
v.insert(9)
print(v[7])
v.insert(8, 0)
print(v[0])
print(v)
print(v.getlist())
v.remove(0)
print(v.getlist())
print(v.size())
v.remove(1, 3)
print(v.getlist())
print(v.size())