from math import pi
x = int(input())
list = list()
def p1(x):
    h= 0
    for i in str(pi):
        h += 1
        list.append(i)
        if h == x+2:
            break
    h = ''.join(list)
    return h
print(p1(x))
