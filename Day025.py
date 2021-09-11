def set_Square(n:list):
    list1 = []
    for i in n:
        show = i**(1/2)-int(i**(1/2))
        if show == 0:
            list1.append(int(i))
    list1.sort()
    return list1
g1 = [1,2,3,4]
g2 = [100,25,36]
g3 = [81,4,1]
print(set_Square(g1))
print(set_Square(g2))
print(set_Square(g3))