print("*** Rabbit & Turtle ***")
d, Vr, Vt, Vf = [int(x) for x in input("Enter Input : ").split()]
ans = Vf*d/(Vt-Vr)
print('%.2f' %ans)