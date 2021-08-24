num = int(input())
in1 = []
in3 = []
shownum = []
goto = 0
count = 0
ans = 0
for i in range(num):
    num1 = input()
    in1.append(num1)
in2 = input().split(" ")
while True:
    num3 = int(input())
    if num3 == -1:
        break
    in3.append(num3)

ans = in1+in2+in3
for i in ans:
    if goto == 0:
        shownum.append(i)
        count+=1
        goto+=1
    else:
        shownum.insert(0, i)
        count=0
        goto-=1
print(str(shownum))




