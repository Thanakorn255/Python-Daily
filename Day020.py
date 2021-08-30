num = int(input())
x_x = []
y_y = []
count = 0
while count!=num:
    x,y = [int(x) for x in input().split()]
    if count%2 == 0:
        x_x.append(x)
        y_y.append(y)
    else:
        x_x.append(y)
        y_y.append(x)
    count+=1
maxormin = input()
if maxormin == "Zig-Zag":
    print("Output :",min(x_x),max(y_y))
else:
    print("Output :",min(y_y),max(x_x))
