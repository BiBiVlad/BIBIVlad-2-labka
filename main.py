from math import pi
x = int(input())
h = 0
list = list()
for i in str(pi):
    h += 1
    list.append(i)
    if h == x+2:
        break

h = ''.join(list)
print(h)