num = input()
count = 10
sum = 0
for i in num:
    sum = sum + (int(i)*count)
    count-=1
ans=sum%11
if ans == 0:
    num = num+"0"
else:
    num = num + str(11-ans)
print(num)